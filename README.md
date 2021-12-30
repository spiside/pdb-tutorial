# `pdb` 教程

这篇教程的目的是教你基本的 `pdb` 用法，它是 `Python2` 和 `Python3` 的调试器。这篇教程也会涉及到一些有用的小技巧，让你在调试程序的时候轻松很多。

---

这篇教程最好搭配 Python 2.7 或者 Python 3.4 使用，如果 `pdb` 在这两个 Python 版本上表现有所不同，我会突出显示他们的差异。要检查你现在使用的 Python 版本，你可以在你的终端上运行如下的命令：

```shell
python --version
```

现在你知道你的 Python 版本了，让我们开始吧！

## 调试器的功能是什么？

在真正开始学习调试代码之前，我们应该先简要地谈论一下调试代码和使用调试工具的重要性。对我来说，如下的三点展现了调试器的重要性。

通过一个调试器，你可以做到

* 检查一个正在运行的程序的状态
* 在程序投入使用前测试它的代码
* 追踪程序的执行逻辑

通过使用一个调试器，你可以在你的程序的任意一个地方设置[程序断点](https://en.wikipedia.org/wiki/Breakpoint)来停止运行程序，也可以做到上面提到的三点。调试器是很强大的工具，和简单地使用 `print()` 语句相比，它们可以大大加快调试过程。



对于你们当中经验丰富的程序员来说，你们也许会同意我的观点：在最好的程序员和懂得如何有效调试程序的程序员之间是存在相关性的。这里所说的有效调试程序指的是：能够诊断出代码的问题，然后可以用最小的力气解决它。使用一个调试器和学习如何正确使用一个调试器会帮助你成为强大的调试高手。为了能够做到在调试环境中轻松自如你得花上不少时间，不过本教程的目的就是让你在自己的代码里面使用 `pdb` 之前先经历这些！

## 玩游戏

我们已经讨论了调试器的功能，现在到了亲自看看它是如何工作的时候了。首先，如果你还没有克隆这个仓库的话要先克隆。如果你还没有安装 `git` 的话，我推荐你尝试安装并使用它（或者是其他的源代码工具），你可以参考[这里](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)来安装 `git`。在你安装好了 `git` 之后，在你的终端运行如下的命令来克隆仓库：

```shell
git clone https://github.com/spiside/pdb-tutorial
```

**注意：**如果这个命令报错克隆失败的话，你应该看看 Github 的[克隆教程](https://help.github.com/articles/cloning-a-repository/)



现在你克隆好了仓库，让我们来到项目的根目录并看看里面的说明文件：

```shell
cd /path/to/pdb-tutorial
```

`file: instructions.txt`

```
Your boss has given you the following project to fix for a client. It's supposed to be a simple dice
game where the object of the game is to correctly add up the values of the dice for 6 consecutive turns.

The issue is that a former programmer worked on it and didn't know how to debug effectively.
It's now up to you to fix the errors and finally make the game playable.

To play the game you must run the main.py file.
```

这看起来很容易！首先，让我们尝试玩这个游戏并看看哪里出了问题。你可以在你的终端输入如下的命令来运行这个程序：

```shell
python main.py
```

你应该会看到像这样的输出：

```
Add the values of the dice
It's really that easy
What are you doing with your life.
Round 1

---------
|*      |
|       |
|      *|
---------
---------
|*      |
|       |
|      *|
---------
---------
|*     *|
|       |
|*     *|
---------
---------
|*     *|
|       |
|*     *|
---------
---------
|*     *|
|   *   |
|*     *|
---------
Sigh. What is your guess?: 
```

看起来之前的程序员似乎有点...幽默感？尽管如此，让我们来输入 17（因为 17 是骰子的和）。

```
Sigh. What is your guess?: 17
Sorry that's wrong
The answer is: 5
Like seriously, how could you mess that up
Wins: 0 Loses 1
Would you like to play again?[Y/n]: 
```

奇怪。他说答案应该是 5，但显然不对...。好吧，也许骰子的加法是错误的，无论如何我们再玩一次游戏来弄清楚。看起来要再玩一次的命令是 `Y`，所以让我们输入 `Y`

```
Would you like to play again?[Y/n]: Y
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    main()
  File "main.py", line 8, in main
    GameRunner.run()
  File "/Users/Development/pdb-tutorial/dicegame/runner.py", line 62, in run
    i_just_throw_an_exception()
  File "/Users/Development/pdb-tutorial/dicegame/utils.py", line 13, in i_just_throw_an_exception
    raise UnnecessaryError("You actually called this function...")
dicegame.utils.UnnecessaryError: You actually called this function...
```

好吧，这很奇怪，即使我们输入了应该是有效的输入，程序仍然抛出了异常。我认为我们可以下结论说这个程序是有问题的，那么让我们开始调试程序吧！

## PDB 101: `pdb` 介绍

是时候到了使用 python 自带的调试器 `pdb` 的时候了。这个调试器包含在 python 的标准库中，我们就像使用任何一个 python 库一样来使用它。首先，我们应先加载 `pdb` 模块，然后调用它的方法在程序中设置用于调试的程序断点。传统的方法是把加载和调用放在你想要程序暂停运行的地方。这个是你会用到的完整声明语句：

```python
import pdb; pdb.set_trace()
```

[`set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace) 方法在被调用的地方设置了一个程序断点。让我们来打开 `main.py` 文件并在第 8 行添加程序断点：



`file: main.py` 

```python
from dicegame.runner import GameRunner


def main():
    print("Add the values of the dice")
    print("It's really that easy")
    print("What are you doing with your life.")
    import pdb; pdb.set_trace() # add pdb here
    GameRunner.run()


if __name__ == "__main__":
    main()
```

看起来不错，现在让我们再次尝试运行 `main.py` 文件并看看会怎么样。

```shell
python main.py
```

```
Add the values of the dice
It's really that easy
What are you doing with your life.
> /Users/Development/pdb-tutorial/main.py(9)main()
-> GameRunner.run()
(Pdb) 
```

很好，我们现在处于运行程序的中间，可以开始调试程序了。我认为第一个要解决的问题是骰子之间的加法到底是如何定义的。

如果你很熟悉 Python 的解释器，里面有很多知识可以迁移到 `pdb` 调试器中来。但是，当我们学习到高阶部分的时候将会有一些问题。先不管这些，我们来学习一些会帮助我们解决骰子加法问题的命令。

## 5 个会让你“说不出话来”的 `pdb` 命令

下面是直接从 `pdb` 文档中摘录出来的命令，一旦你学会了使用他们，你就无法想象没有他们会是怎么样。

1. `l(ist)` - 展示当前行附近的 11 行，或者是继续之前的展示。
2. `s(tep)` - 执行当前行，会停在第一个可能停下的地方。
3. `n(ext)` - 继续执行程序到当前函数的下一行或者是到它返回结果。
4. `b(reak)` - 设置程序断点 (取决于提供的参数)。
5. `r(eturn)` - 继续执行到当前函数返回结果。

注意这些命令中的后面都用括号括了起来，这表示在 `pdb` 中使用这些命令的时候，括号中的部分是可选的，也就是说是可以省略的。这会节省你打字的时间，但是如果你有变量名是 `l` 或者是 `n` 的话会有大问题，他们会被认为是 `pdb` 的命令而不是变量。举例来说，如果在你的程序中有变量叫做 `c`，你想知道它的值，你如果直接在 `pdb` 里输入 `c` 的话，实际上你是在告诉调试器说要执行 `c(ontinue)` 指令，它会一直运行直到遇到程序断点！



**注意：**我和其他程序员们一样，不建议使用短的变量名，比如 `a`，`b`，`gme`等。这些短变量名没有含义还会让其他人在阅读你的代码的时候感到很困惑。我只是在这里向你们展示你们在 `pdb` 中使用短变量名的时候可能会遇到的问题。



**再次注意：**另外一个有用的命令是 `h(elp) - 不给参数的话，会输出可使用的所有命令。如果提供了命令作为参数，就会输出命令的帮助手册`。这篇教程接下来的部分，我会使用短命令，如果我用到了一个我没有介绍过的命令，我会解释它的功能是什么。那么，让我们开始学习第一个命令吧。

### 1. `l(ist)` 又叫做： 我懒得打开包含源代码的文件

```
l(ist) [first [,last]]
    List source code for the current file. Without arguments, list 11 lines around the current line
    or continue the previous listing. With one argument, list 11 lines starting at that line.
    With two arguments, list the given range; if the second argument is less than the first, it is a count.
```

**注意：**上面的命令描述是调用 `help list` 生成的。如果要得到一样的输出，你可以在 `pdb` 中输入 `help l`。我们可以使用 `list` 命令来检查我们所在的行的源代码。`list` 命令的参数让你可以指定要查看的行的范围，这在你用来查看第三方库的时候很有用（往往代码会很长）。



**注意：**在大于等于 Python 3.2 的版本中，你可以通过输入 `ll`（更长的输出）来看当前函数或者是堆栈帧的源代码。我基本都是使用这个而不是 `l` 命令，因为它相比于展示当前位置附近的 11 行来说，你可以更直观知道你当前处在哪个函数里。



现在让我们尝试使用 `l` 命令。在你已经打开的 `pdb` 调试窗口中，输入 `l` 并查看输出：

```
(Pdb) l
  4     def main():
  5         print("Add the values of the dice")
  6         print("It's really that easy")
  7         print("What are you doing with your life.")
  8         import pdb; pdb.set_trace()
  9  ->     GameRunner.run()
 10     
 11     
 12     if __name__ == "__main__":
 13         main()
[EOF]
```

如果我们想看整个文件，我们可以给 list 命令加上范围参数（1～13），像这样：

```
(Pdb) l 1, 13
  1     from dicegame.runner import GameRunner
  2     
  3     
  4     def main():
  5         print("Add the values of the dice")
  6         print("It's really that easy")
  7         print("What are you doing with your life.")
  8         import pdb; pdb.set_trace()
  9  ->     GameRunner.run()
 10     
 11     
 12     if __name__ == "__main__":
 13         main()
```

不幸的是，我们从这个文件中得不到什么信息，但我们可以看到它调用了 `GameRunner` 类的 `run()` 方法。此时，你可能会想，“哇哦，我要在 `dicegame/runner.py` 文件里面的 run 方法中插入 `pdb` 语句！“这个方法是可行的，但是更轻松的方式是使用我们之后会提到的 `step` 命令。

### 2. `s(tep)` 又叫做： 让我们来看看这个方法做了什么...

```
s(tep)
    Execute the current line, stop at the first possible occasion
    (either in a function that is called or in the current
    function).
```

你的程序现在应该还停留在 `:9` 行，要知道当前在哪一行可以查看 `list` 命令输出的 `->` 箭头指向哪。



让我们来调用 `step` 命令看看会发生什么。

```
(Pdb) s
--Call--
> /Users/Development/pdb-tutorial/dicegame/runner.py(21)run()
-> @classmethod
```

不错！我们目前在 `runner.py` 文件的第 21 行，这一点可以从 `> /Users/Development/pdb-tutorial/dicegame/runner.py(21)run()` 看出来。

问题是，我们没有太多的上下文信息，所以让我们来运行 `list` 命令来检查这个方法。

```
(Pdb) l
 16             total = 0
 17             for die in self.dice:
 18                 total += 1
 19             return total
 20     
 21  ->     @classmethod
 22         def run(cls):
 23             # Probably counts wins or something.
 24             # Great variable name, 10/10.
 25             c = 0
 26             while True:
```

哇哦！现在我们有了 `run()` 方法的更多上下文信息。但我们现在还在 `:21` 行。让我们再次执行 `step` 命令来进入到这个方法内部，然后用 `list` 命令查看我们当前的位置。

```
(Pdb) s
> /Users/Development/pdb-tutorial/dicegame/runner.py(25)run()
-> c = 0
(Pdb) l
 20     
 21         @classmethod
 22         def run(cls):
 23             # Probably counts wins or something.
 24             # Great variable name, 10/10.
 25  ->         c = 0
 26             while True:
 27                 runner = cls()
 28     
 29                 print("Round {}\n".format(runner.round))
 30  
```

正如我们所看到的，我们正处于一个糟糕的变量名 `c` 上，如果我们尝试调用它将会产生很大的问题（回忆之前我们关于 `c(ontinue)` 命令的讨论）。我们正处于 `while` 循环前，所以让我们来进入到循环里面看看我们能发现什么。

### 3. `n(ext)` 又叫做： 我希望当前的行不要抛出异常

```
n(ext)
    Continue execution until the next line in the current function
    is reached or it returns.
```

在当前行输入 `n(ext)` 命令，然后输入 `list`（注意这个模式），然后让我们看看发生了什么。



**译者注：**在我用的 Python 3.8.10 上，此时我停留在了 `runner = cls()` 这一行

```
(Pdb) n
> /Users/Development/pdb-tutorial/dicegame/runner.py(27)run()
-> while True:
(Pdb) l
 21         @classmethod
 22         def run(cls):
 23             # Probably counts wins or something.
 24             # Great variable name, 10/10.
 25             c = 0
 26  ->         while True:
 27                 runner = cls()
 28     
 29                 print("Round {}\n".format(runner.round))
 30     
 31                 for die in runner.dice:
```

现在我们停在了 `while True` 语句！我们可以一直调用 `next` 命令直到程序抛出异常或者是结束运行。再调用 3 次 `next` 命令就来到了 `for` 语句，然后调用 `list` 命令展示当前行的附近行。



**译者注：**因为之前直接跳到了 `runner = cls()` 这一行，所以在这里我只要调用 2 次 `next` 就到了 `for` 语句

```
(Pdb) n
> /Users/Development/pdb-tutorial/dicegame/runner.py(27)run()
-> runner = cls()
(Pdb) n
> /Users/Development/pdb-tutorial/dicegame/runner.py(29)run()
-> print("Round {}\n".format(runner.round))
(Pdb) n
Round 1

> /Users/Development/pdb-tutorial/dicegame/runner.py(31)run()
-> for die in runner.dice:
(Pdb) l
 26             while True:
 27                 runner = cls()
 28     
 29                 print("Round {}\n".format(runner.round))
 30     
 31  ->             for die in runner.dice:
 32                     print(die.show())
 33     
 34                 guess = input("Sigh. What is your guess?: ")
 35                 guess = int(guess)
```

如果你继续输入 `next` 命令，你会遍历完这个 `for` 循环，遍历的长度等于 `runner.dice` 的长度。我们可以在 `pdb` 中用 `len` 方法来看看 `runner.dice` 的长度，应该会返回 5。

```
(Pdb) len(runner.dice)
5
```

因为这个长度*只有* 5，我们可以调用 5 次 `next` 命令来走完这个循环，但如果长度是 50 甚至是 10000 呢！

更好的方法应该是设置一个程序断点，然后调用 `continue` 命令一直运行到程序断点处。

### 4. `b(reak)` 又叫做：我再也不想输入 `n` 命令了

```
b(reak) [ ([filename:]lineno | function) [, condition] ]
    Without argument, list all breaks.

    With a line number argument, set a break at this line in the
    current file.  With a function name, set a break at the first
    executable line of that function.  If a second argument is
    present, it is a string specifying an expression which must
    evaluate to true before the breakpoint is honored.

    The line number may be prefixed with a filename and a colon,
    to specify a breakpoint in another file (probably one that
    hasn't been loaded yet).  The file is searched for on
    sys.path; the .py suffix may be omitted.
```

在这篇教程中，我们只需要看 `b(reak)` 命令描述的前两段。就像我在前面的部分提到的，我们想要通过设置程序断点的方式来执行完 `for` 循环，然后接着看 `run()` 方法的其他部分。因为 `:34` 行有 `input` 函数，程序会暂停并等待用户输入，所以让我们停在 `:34` 行。为了做到这一点，我们可以输入 `b 34` 然后输入 `continue` 来运行到程序断点处。

```
(Pdb) b 34
Breakpoint 1 at /Users/Development/pdb-tutorial/dicegame/runner.py(34)run()
(Pdb) c

[...] # prints some dice

> /Users/Development/pdb-tutorial/dicegame/runner.py(34)run()
-> guess = input("Sigh. What is your guess?: ")
```

我们也可以通过不带参数调用 `break` 命令来看看我们设置好的程序断点。

```
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /Users/Development/pdb-tutorial/dicegame/runner.py:34
    breakpoint already hit 1 time
```

如果要删除你的程序断点，你可以使用 `cl(ear)` 命令，参数是上面输出的程序断点行的最左边（也就是 1）。现在让我们调用参数为 1 的 `clear` 命令来删除刚才设置的程序断点。



**注意：**如果你没有提供任何参数给 `clear` 命令，那么就会清空所有的程序断点。

```
(Pdb) cl 1
Deleted breakpoint 1 at /Users/Development/pdb-tutorial/dicegame/runner.py:34
```

现在我们可以调用 `next` 命令来执行 `input()` 函数。让我们猜测骰子和为 10 并输入我们的猜测，一旦我们回到 `pdb` 中，我们可以调用 `list` 命令来看看接下来的几行。

```
(Pdb) n
Sigh. What is your guess?: 10
> /Users/Development/pdb-tutorial/dicegame/runner.py(35)run()
-> guess = int(guess)
(Pdb) l
 30     
 31                 for die in runner.dice:
 32                     print(die.show())
 33     
 34                 guess = input("Sigh. What is your guess?: ")
 35  ->             guess = int(guess)
 36     
 37                 if guess == runner.answer():
 38                     print("Congrats, you can add like a 5 year old...")
 39                     runner.wins += 1
 40                     c += 1



```

记住我们是在尝试找出第一次玩游戏的时候我们猜测的骰子和不对的原因。这看起来似乎是 `guess == runner.answer` 这里的等于判断出了问题。我们应该仔细检查一下看看 `runner.answer()` 这个方法做了什么，以防万一可能会遇到错误。调用一次 `next` 命令然后调用 `step` 命令来*进入*到 `runner.answer()` 方法内部。

```
(Pdb) s
--Call--
> /Users/spiro/Development/mobify/engineering-meeting/pdb-tutorial/dicegame/runner.py(15)answer()
-> def answer(self):
(Pdb) l
 10         def reset(self):
 11             self.round = 1
 12             self.wins = 0
 13             self.loses = 0
 14     
 15  ->     def answer(self):
 16             total = 0
 17             for die in self.dice:
 18                 total += 1
 19             return total
 20  
```

我想我找到了问题根源！在第 18 行，它在计算 `total` 的时候看起来不是我们想象的那种骰子的加法。让我们来检查一下 `die` 有没有什么属性等于骰子本身的值看能不能解决这个问题。如果要到第 18 行，你可以通过设置一个程序断点，也可以一直调用 `next` 命令直到你到了循环到第一次迭代。一旦你到了 `:18` 行，让我们对 `die` 实例调用一下 `dir()` 函数看看它有什么属性和方法。

```
-> total += 1
(Pdb) dir(die)
['__class__', '__delattr__', [...], 'create_dice', 'roll', 'show', 'value']
```

它有一个属性叫做 `value`！让我们调用一下它看看返回了什么（注意，你这里显示的值可能跟我的不同）。同时让我们也调用一下它的 `show()` 方法显示骰子图案，确保显示的结果和它的 `value` 值一样。

```
(Pdb) die.value
2
(Pdb) die.show()
'---------\n|*      |\n|       |\n|      *|\n---------'
```

**注意：**如果你想要换行符 `\n` 真的有换行的效果，你可以执行 `print(die.show())`。



这看起来一切正常，骰子的 `value` 值和 `show()` 方法输出的是一样的，我们准备修复 answer 方法。但是，我们中的一些人可能想要继续调试程序来一次性找出所有的程序错误。不幸的是，我们再一次卡在了 for 循环里，你可能想到了在第 `:19` 行设置一个程序断点然后调用 `continue` 命令，但实际上有更好的方法。

### 5. `r(eturn)` 又叫做：我想退出这个函数

```
r(eturn)
    Continue execution until the current function returns.
```

`return` 是一个*强大的用户命令*，让你可以直接检查函数的最后返回的结果。尽管你可以在调用 return 的地方设置一个程序断点，但如果一个函数里有多个 return 语句的话，还是在 pdb 里面使用 `return` 命令会好一些，因为它对一个 return 语句只会遵循一条执行路径。让我们调用一下 `return` 命令到函数的末尾。

```
(Pdb) r
--Return--
> /Users/Development/pdb-tutorial/dicegame/runner.py(19)answer()->5
-> return total
(Pdb) l
 14     
 15         def answer(self):
 16             total = 0
 17             for die in self.dice:
 18                 total += 1
 19  ->         return total
 20     
 21         @classmethod
 22         def run(cls):
 23             # Probably counts wins or something.
 24             # Great variable name, 10/10.
(Pdb) 
```

如果要检查返回的 `total` 变量的值，你可以在这里输入 `total` 或者直接看 `--Return--` 下面的语句（最右边）。现在，为了回到 `run()` 方法里，让我们调用 `next` 命令，就会回到原来的地方。



此时，你可以通过调用 `exit()` 命令**或者**按下 `CTRL+D`（和在 Python REPL 环境中一样）。有了这 5 个命令，你应该能弄明白其他的一些 bug，然后可以进阶学习更高阶的 `pdb` 例子。

## 高阶 `pdb` 

这里有一些你可以使用的高阶的 `pdb` 命令。

### `!` 命令

```
!
  Execute the (one-line) statement in the context of the current stack frame.
```

`! `命令是在告诉 `pdb` 接下来的语句是 Python 命令而不是 `pdb` 命令。在带有变量名为 `c` 的 `run()` 方法中这很有用。就像我在教程一开始说的，直接在 `pdb` 里面输入 `c` 会被认为是要执行 `continue` 指令。进入 `pdb` 调试模式，停在 `runner.py` 的 `:26` 行，然后可以运行 `!c` 看看会发生什么。

```
(Pdb) !c
0
```

我们得到了预料中的值，因为在 `:25` 行执行了 `c = 0`！

### `pdb` Post Mortem

```
pdb.post_mortem(traceback=None)
    Enter post-mortem debugging of the given traceback object. If no traceback is given, it uses the one of the exception that is currently being handled
    (an exception must be being handled if the default is to be used).

pdb.pm()
    Enter post-mortem debugging of the traceback found in sys.last_traceback. 
```

尽管这两个方法可能看上去一样，但是 `post_mortem()` 和 `pm()` 产生的异常信息轨迹不一样。我通常在 `except` 的代码块里面使用 `post_mortem()`。

但是，我也会谈到 `pm()`，因为我发现它更强大。让我们来尝试这个方法并看看在实践中它是怎么工作的。



先打开终端并进入到项目的根目录下，然后输入 `python` 进 python REPL 交互模式。然后，让我们从 `main` 模块里面载入 `main` 方法，同时要载入 `pdb`。接下来玩游戏直到我们在尝试输入 `Y` 继续游戏的时候抛出异常。

```
>>> import pdb
>>> from main import main
>>> main()
[...]
Would you like to play again?[Y/n]: Y
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    main()
  File "main.py", line 8, in main
    GameRunner.run()
  File "/Users/Development/pdb-tutorial/dicegame/runner.py", line 62, in run
    i_just_throw_an_exception()
  File "/Users/Development/pdb-tutorial/dicegame/utils.py", line 13, in i_just_throw_an_exception
    raise UnnecessaryError("You actually called this function...")
dicegame.utils.UnnecessaryError: You actually called this function...
```

现在，让我们从 `pdb` 模块中调用 `pm()` 方法看看会发生什么。

```
>>> pdb.pm()
> /Users/Development/pdb-tutorial/dicegame/utils.py(13)i_just_throw_an_exception()
-> raise UnnecessaryError("You actually called this function...")
(Pdb) 
```

看看！在 `pdb` 环境中我们停在了最后一个抛出异常的地方的前面。在这里我们可以在程序出错之前检查程序的状态。



**注意：**你也可以使用 `python -m pdb main.py` 来启动 `main.py` 脚本，然后输入 `continue` 运行程序直到抛出异常，Python 会在没有捕获的异常上自动进入 `post_mortem` 模式。

## 写在最后

恭喜你坚持到了最后，谢谢你一路学习了这篇教程！如果你有任何意见、批评或者额外的高阶例子想提供，欢迎你提交 pull request。

