# `pdb` Tutorial

The purpose of this tutorial is to teach you the basics of `pdb`, the **P**ython **D**e**B**ugger for [Python2](https://docs.python.org/2/library/pdb.html)
and [Python3](https://docs.python.org/3/library/pdb.html).
It will also include some helpful tricks to make your debugging sessions a lot less stressful.

--- 

#### Other translations

The tutorial is written in english, but there are other translations available with help
from the Python community:

- [Korean](https://github.com/mingrammer/pdb-tutorial)
- [Chinese](https://github.com/MartinLwx/pdb-tutorial)

If you would like to see another other translation, or are interested in helping out with translating the tutorial,
feel free to add to the [ongoing issues thread](https://github.com/spiside/pdb-tutorial/issues/9).

---


The tutorial works best if you use Python 2.7 or Python 3.4 and I will highlight the
differences between the two versions if a `pdb`
command differs. To check what version of python you're using, type the following in your terminal:

```shell
python --version
```

Now that you know your version, let's get to it!


## What is the purpose of a debugger?

Before jumping into the code, we should have a brief discussion about the importance of debugging and using
a debugging tool. For me, these three points highlight the importance of a debugger.

With a debugger, you can:
* Explore the state of a running program
* Test implementation code before applying it
* Follow the program's execution logic

Using a debugger, you can set a [breakpoint](https://en.wikipedia.org/wiki/Breakpoint) at any point of
your program to stop it and apply the three points above. Debuggers are very powerful tools and they
can speed up the debugging process a lot faster than using simple `print()` statements everywhere.

For those of you who are veteran programmers, you might agree with me that there is a
correlation between the best programmers and the ones that know how to debug effectively. By debugging
effectively, I mean being able to diagnose a problem and then treat the error with minimal difficulty. 
Using a debugger and learning how to use it properly will help you become an effective debugger. It will
take some time before you feel comfortable navigating around in a debugging environment but the purpose
of this tutorial is to get your feet wet before you start using `pdb` in your own code base!


## Playing the Game

So we already talked about the purpose of a debugger and now it's time to see it in action. First, you
should clone this repo if you haven't already done so. If you don't have `git` installed, I recommend using
it (or some version of source control) and you can find out details on how to install `git` [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Once you have `git` installed, clone the repo by entering the following in your terminal:

```shell
git clone https://github.com/spiside/pdb-tutorial
```

**NB**: If that didn't work for you, you should follow Github's [cloning tutorial](https://help.github.com/articles/cloning-a-repository/).

Now that you have the repo cloned, let's navigate to the root of the project and take a look at the instructions given:

```shell
cd /path/to/pdb-tutorial
```

`file: instructions.txt`
```
Your boss has given you the following project to fix for a client. It's supposed to be a simple dice
game where the objective of the game is to correctly add up the values of the dice for 6 consecutive turns.

The issue is that a former programmer worked on it and didn't know how to debug effectively.
It's now up to you to fix the errors and finally make the game playable.

To play the game you must run the main.py file.
```

Seems easy enough! To begin, let's try playing the game to see what's wrong. To run the program, type the following in your
terminal:

```shell
python main.py
``` 

You should see something like this:

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

Seems like the previous programmer had a sense of...humor? Nonetheless, let's enter 17 (since that is the total value of the dice).

```
Sigh. What is your guess?: 17
Sorry that's wrong
The answer is: 5
Like seriously, how could you mess that up
Wins: 0 Loses 1
Would you like to play again?[Y/n]: 
```

Weird. It said the answer is 5 but that's clearly wrong... Alright, maybe the dice addition is wrong but let's play the game again to
figure it out. Looks like the prompt to play again is `'Y'` so let's enter that now.

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

Ok weird, there was an exception that was thrown even though we used what was supposed to be a valid input. I think it's safe to
say that the program is broken so let's start the debugging process! 


## PDB 101: Intro to `pdb`

It's time to finally work with python's very own debugger `pdb`. The debugger is included in python's standard library and we
use it the same way we would with any python library. First, we have to import the `pdb` module and then call one of its methods
to add a debugging breakpoint in the program. The conventional way to do this is to add the import **and** call the method at the same line you
would like to stop at. This is the full statement you would want to include:

```python
import pdb; pdb.set_trace()
```

Starting from version 3.7: The built-in function `breakpoint()` can be used instead of using `import pdb; pdb.set_trace()`

```python
breakpoint()
```

The methods [`set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace) and [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint) hard code a breakpoint
where the method was called. Let's use the `set_trace()` method for this tutorial since it is supported in all python versions. Let's try it now by opening up the `main.py` file and adding the breakpoint
on line 8:

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

Cool, now let's try to run `main.py` again and see what happens.

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

There we go! We are now in the middle of the running program and we can start poking around. I think the first issue we should
solve is the proper summation of the dice values.

If you are familiar with Python's interpreter, a lot of that knowledge can be transferred to the `pdb` debugger. However, there will be
a couple gotchas that we will get to in the advanced section. Regardless, let's learn a couple commands that will help us solve the
addition issue.


## The 5 `pdb` commands that will leave you "speechless"

Taken directly from the `pdb` documentation, these are the five commands that, once you learn them, you won't know how you lived
without them.

1. `l(ist)` - Displays 11 lines around the current line or continue the previous listing.
2. `s(tep)` - Execute the current line, stop at the first possible occasion.
3. `n(ext)` - Continue execution until the next line in the current function is reached or it returns.
4. `b(reak)` - Set a breakpoint (depending on the argument provided).
5. `r(eturn)` - Continue execution until the current function returns.

Notice that there are brackets around the last part of every keyword. The brackets indicate that the rest of the word is _optional_ when
using the command prompt for `pdb`. This saves typing but a major gotcha is if you have a variable name such as `l` or `n`, then the
`pdb` command takes precedence. That is, say you have a variable named `c` in your program and you want to know the value of `c`. Well,
if you type `c` in `pdb`, you will actually be issuing the `c(ontinue)` keyword which executes the program and only stops if it encounters
a break point!

**NB**: I, and many other programmers, discourage the use of short variable names such as `a`, `b`, `gme`, etc. These carry no meaning
and will confuse other people reading your code. I'm only demonstrating the issues you may encounter with `pdb` in the presence of
shortened variable names.

**NNB**: Another helpful tool is the following:
`h(elp) - Without argument, print the list of available commands. With a command as an argument, print help about that command.`

For the rest of the tutorial, I will be using the shortened version of the commands and if I use a command that I have not introduced
here, I will explain what it does. So, let's begin with the first one.

### 1. l(ist) a.k.a. I'm too lazy to open the file containing the source code

```
l(ist) [first [,last]]
    List source code for the current file. Without arguments, list 11 lines around the current line
    or continue the previous listing. With one argument, list 11 lines starting at that line.
    With two arguments, list the given range; if the second argument is less than the first, it is a count.
```

**NB**: The above description was generated by calling `help` on `list`. To get the same output, in the `pdb` REPL type `help l`.

Using `list`, we can examine the source code of the current file we are in. The arguments for `list` lets you specify a given range
of lines you wish to see which can be helpful if you are in some weird 3rd party package and you are trying to figure out why they
can't get string encoding working _true story_.

**NB**: In Python 3.2 and above, you can type `ll` (long list) which shows you source code for the current function or frame. I use
this all the time instead of `l` since it's much better knowing which function you are in than an arbitrary 11 lines around your
current position.

Let's try using `l` now. In your already open `pdb` prompt, type in `l` and look at the output:

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

If we want to see the whole file, we can call the list function with the range 1 to 13 like so:

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

Unfortunately, we don't get that much information from this file alone but we do see that it is calling the `run()` method of the `GameRunner`
class. At this point, you might be thinking, "Awesome, I'll just set a `pdb` in the run method in the `dicegame/runner.py` file !" That will
work, but there's an even easier way using the `step` command we will discuss next.

### 2. `s(tep)` a.k.a let's see what this method does...

```
s(tep)
    Execute the current line, stop at the first possible occasion
    (either in a function that is called or in the current
    function).
```

Your current line of execution should still be on `:9` and you can tell the current line by looking at the `->` outputted by the `list` command. 
Let's call the `step` command and see what happens.

```
(Pdb) s
--Call--
> /Users/Development/pdb-tutorial/dicegame/runner.py(21)run()
-> @classmethod
```

Nice! We're currently in the `runner.py` file on line 21 which we can tell from this line:
`> /Users/Development/pdb-tutorial/dicegame/runner.py(21)run()`.
The problem is, we don't have much context so run the `list` command to checkout the method.

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

Awesome! Now we have some more context on the `run()` method but we are currently on `:21`. Let's `step` in one more time so that we enter the method itself and
then run the list command to see our current position.

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

As we can see, we are on a terribly named `c` variable that will cause us a major issue if we try to call it (remember the comment from earlier regarding the
`c(ontinue)` command). We are just before the `while` loop so let's enter the loop and see what else we can uncover.

### 3. `n(ext)` a.k.a I hope this current line doesn't throw an exception

```
n(ext)
    Continue execution until the next line in the current function
    is reached or it returns.
```

From the current line, type the `n(ext)` command followed by `list` (notice a pattern) and let's observe what happens.

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

Now our current line on the `while True` statement! We can keep calling `next` indefinitely until the program throws an exception or terminates. Call `next` 3 more
times to get to the `for` loop and then follow up `next` with `list`.

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

At this current point, if you continue to type the `next` command you will then iterate through the `for` loop for the length of the `runner.dice`
attribute. We can take a look at the length of the `runner.dice` by calling the `len()` function around it in the `pdb` REPL which should return 5.

```
(Pdb) len(runner.dice)
5
```

Since the length is _only_ 5 items, we could iterate through the loop by calling `next` 5 times, but let's say there were 50 items to iterate over, or even 10,000!
A better option would be to set a break point and then `continue` to that break point instead.


### 4. `b(reak)` a.k.a I don't want to type `n` anymore

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

We're only going to pay attention to the first two paragraphs of `b(reak)`'s description in this tutorial. Like I mentioned in the previous section, we want
to set a break point past the `for` loop so we can continue to navigate through the `run()` method. Let's stop on `:34` since this has the input function
which will break and wait for a user input anyways. To do this, we can type `b 34` and then `continue` to the break point.

```
(Pdb) b 34
Breakpoint 1 at /Users/Development/pdb-tutorial/dicegame/runner.py(34)run()
(Pdb) c

[...] # prints some dice

> /Users/Development/pdb-tutorial/dicegame/runner.py(34)run()
-> guess = input("Sigh. What is your guess?: ")
```

We can also take a look at the break points that we have set by calling `break` without any arguments.

```
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /Users/Development/pdb-tutorial/dicegame/runner.py:34
    breakpoint already hit 1 time
```

To clear your break points, you can use the `cl(ear)` command followed by the breakpoint number which is found in the leftmost column of the above
output. Let's clear the breakpoint now by calling the `clear` command followed by 1.

**NB**: You can also clear all the breakpoints if you don't provide any arguments to the `clear` command.

```
(Pdb) cl 1
Deleted breakpoint 1 at /Users/Development/pdb-tutorial/dicegame/runner.py:34
```

From here we can call `next` and execute the `input()` function. Let's just type 10 for our guess and once we are back in the `pdb` REPL, call `list` so we can see
the next few lines.

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

Remember that we are trying to find out why our guess wasn't correct on our first playthrough. It seemed like there was an error with the `guess == runner.answer`
equality condition. We should check to see what the `runner.answer()` method is doing in case there might be an error there. Call `next` and then let's call `step`
to _step_ into the `runner.answer()` method.

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

I think I found the issue! On line 18, it doesn't look like the `total` variable is adding up the values of the dice like we want it to. Let's see if we can fix that by
checking whether a `die` has an attribute which would contain its value. To get to line 18, you can either set a break point or just call `next` until you
hit the first iteration. Once you're on `:18`, let's call the `dir()` function on the `die` instance and check what methods and attributes it has.

```
-> total += 1
(Pdb) dir(die)
['__class__', '__delattr__', [...], 'create_dice', 'roll', 'show', 'value']
``` 

There is a `value` attribute after all! Let's call that and see what returns (remember, this value will probably be different than mine). And just for fun,
let's make sure it is equal to the value that the die is showing by calling the `show()` method as well.

```
(Pdb) die.value
2
(Pdb) die.show()
'---------\n|*      |\n|       |\n|      *|\n---------'
```

**NB**: If you want the newline character `\n` to print as a newline, call `print()` with `die.show()` as its argument.

It looks like it works as expected and we're ready to fix the answer method. However, some of us may want to continue with the debugging process and catch all the
errors in one go. Unfortunately, we are once again stuck in this for loop. You might think to set a break point at `:19` and then call `continue` but there is actually
a better way in this case.

### 5. `r(eturn)` a.k.a. I want to get out of this function

```
r(eturn)
    Continue execution until the current function returns.
```

The `return` is a great _power user_ command that let's you examine the final outcome of a function. While you could set a breakpoint at the return call, the
`return` pdb command will help if there are multiple return statements in a single function since it only follows the path of execution for a single return. Let's
call the `return` command and get to the end of the function.

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

To check the value of the returned `total` variable, you can call `total` here or look at the final value in line below the `--Return--` output. Now, to return back
to the `run()` method, call the `next` command and you'll be back in your happy place.

At this point, you can exit the `pdb` debugger by calling `exit()` **OR** `CTRL+D` (same as the Python REPL). With these five commands, you should be able to figure
out a couple other bugs and then follow along with a bit more advanced `pdb` examples.


## Advanced `pdb` topics

Here are a couple advanced `pdb` commands that you can also use.

### The `!` (bang) command

```
!
  Execute the (one-line) statement in the context of the current stack frame.
```

The bang command (`!`) lets `pdb` know that the following statement will be a Python command and not a `pdb` command. Where this is helpful is in the `run()` method
with the `c` variable. Like I mentioned in the beginning of the tutorial, calling `c` in `pdb` will issue the `continue` command. Navigating in your `pdb` REPL, stop
at `:26` in the `runner.py` file and from that point you can prefix `c` with the `!` command and see what happens. 

### The `commands` command

```
commands [bpnumber]
        (com) ...
        (com) end
        (Pdb)

        Specify a list of commands for breakpoint number bpnumber.
```

`commands` will run python code or pdb commands that you specified whenever the stated breakpoint number is hit. Once you start the `commands` block, the prompt changes to `(com)`. The code/commands you write here function as if you had typed them at the `(Pdb)` prompt after getting to that breakpoint. Writing `end` will terminate the command and the prompt changes back to `(Pdb)` from `(com)`. I have found this of great use when I need to monitor certain variables inside of a loop as I don't need to print the values of the variables repeatedly. Let's see an example. Make sure to be at the root of the project in your terminal and type the following:

```
python -m pdb main.py
```

Reach line `:8` and `s(tep)` into the `run()` method of the GameRunner class. Then, set up a breakpoint at `:17`.
```
> /Users/Development/pdb-tutorial/main.py(8)main()
-> GameRunner.run()  #This is line 8 in main.py
(Pdb) s      
--Call--
> /Users/Development/pdb-tutorial/dicegame/runner.py(21)run()
-> @classmethod 
(Pdb) b 17
Breakpoint 4 at /Users/Development/pdb-tutorial/dicegame/runner.py:17
```
This sets up the breakpoint, which has been given the number `4`, at the start of the loop inside the `answer()` method which is used to calculate the total values of the dice. Now, let's us use `commands` to print the value of the variable `total` when we hit this breakpoint. 

```
(Pdb) commands 4
(com) print(f"The total value as of now is {total}")
(com) end
```
We have now set up `commands` for breakpoint number 4 which will execute when we reach this breakpoint. Let us `c(ontinue)` and reach this breakpoint.  

```
(Pdb) c
[...] # You will have to guess a number
The total value as of now is 0
> /Users/Development/pdb-tutorial/dicegame/runner.py(17)answer()
-> for die in self.dice:
(Pdb)
```

We see that out print statement executed upon reaching this breakpoint. Let's `c(ontinue)` again and see what happens.

```
(Pdb) c
[...] 
The total value as of now is 1
> /Users/Development/pdb-tutorial/dicegame/runner.py(17)answer()
-> for die in self.dice:
(Pdb)
```
The `commands` command executes upon reaching the breakpoint again. You can see how this might be useful especially during loops.

### `pdb` Post Mortem

```
pdb.post_mortem(traceback=None)
    Enter post-mortem debugging of the given traceback object. If no traceback is given, it uses the one of the exception that is currently being handled
    (an exception must be being handled if the default is to be used).

pdb.pm()
    Enter post-mortem debugging of the traceback found in sys.last_traceback. 
```

While both methods may look the same, `post_mortem() and pm()` differ by the traceback they are given. I commonly use `post_mortem()` in the `except` block.
However, we will cover the `pm()` method since I find it to be a bit more powerful. Let's try and see how this works in practice.

Open up the python REPL by typing `python` in your shell in the root of this project. From there, let's import the `main` method from the `main` module and import `pdb`
as well. Play the game until the we get the exception after trying to type `Y` to continue the game.

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

Now, let's call the `pm()` method from the `pdb` module and see what happens.

```
>>> pdb.pm()
> /Users/Development/pdb-tutorial/dicegame/utils.py(13)i_just_throw_an_exception()
-> raise UnnecessaryError("You actually called this function...")
(Pdb) 
```

Look at that! We recover from the point where the last exception was thrown and are placed in the `pdb` prompt. From here, we can examine the state the program was in
before it crashed which will help you in your investigation.

**NB**: You can also start the `main.py` script using `python -m pdb main.py` and `continue` until an exception is thrown. Python will automatically enter `post_mortem`
mode at the uncaught exception.


## The End

Congrats on making it to the end and thank you for following along in this tutorial! If you have any comments, critiques, or additional advanced examples, I'm open to pull requests.

