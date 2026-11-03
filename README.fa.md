<div dir="rtl" lang="fa">

# آموزش `pdb`

هدف این آموزش، آشنایی با مبانی `pdb`، اشکال‌زدای پایتون (**P**ython **D**e**B**ugger)، در [پایتون ۲](https://docs.python.org/2/library/pdb.html) و [پایتون ۳](https://docs.python.org/3/library/pdb.html) است. همچنین چند ترفند کاربردی یاد می‌گیرید تا هنگام اشکال‌زدایی کمتر دچار دردسر شوید.

> یادداشت ترجمه: دستورها، کد و خروجی نمونه‌ها به زبان اصلی حفظ شده‌اند تا با اجرای پروژه مطابقت داشته باشند. شمارهٔ خط‌ها و نسخه‌های پایتون نیز مطابق آموزش اصلی هستند.

---

#### ترجمه‌های دیگر

این آموزش در اصل به [انگلیسی](README.md) نوشته شده است و با کمک جامعهٔ پایتون، ترجمه‌های دیگری هم دارد:

- [کره‌ای](https://github.com/mingrammer/pdb-tutorial)
- [چینی](https://github.com/MartinLwx/pdb-tutorial)
- [روسی](https://github.com/0xfadeef/pdb-tutorial)

اگر دوست دارید ترجمهٔ دیگری از این آموزش ببینید یا در ترجمهٔ آن همکاری کنید، در [گفت‌وگوی مربوط به ترجمه‌ها](https://github.com/spiside/pdb-tutorial/issues/9) شرکت کنید.

---

این آموزش برای پایتون ۲٫۷ یا ۳٫۴ نوشته شده است. هر جا رفتار یک دستور `pdb` در این دو نسخه متفاوت باشد، تفاوت را توضیح می‌دهیم. برای بررسی نسخهٔ پایتون خود، دستور زیر را در ترمینال وارد کنید:

<div dir="ltr">

```shell
python --version
```

</div>

حالا که نسخهٔ پایتون را می‌دانید، شروع کنیم!

## اشکال‌زدا چه کاربردی دارد؟

پیش از ورود به کد، بهتر است کمی دربارهٔ اهمیت اشکال‌زدایی و استفاده از ابزار مناسب آن صحبت کنیم. از نظر من، سه مورد زیر اهمیت اشکال‌زدا را نشان می‌دهند.

با اشکال‌زدا می‌توانید:

- وضعیت یک برنامهٔ در حال اجرا را بررسی کنید.
- کدی را پیش از اعمال در برنامه آزمایش کنید.
- منطق اجرای برنامه را دنبال کنید.

با استفاده از اشکال‌زدا می‌توانید در هر جای برنامه یک [نقطهٔ توقف](https://en.wikipedia.org/wiki/Breakpoint) تعیین کنید تا اجرای برنامه متوقف شود و سه کار بالا را انجام دهید. اشکال‌زداها ابزارهای بسیار قدرتمندی هستند و در مقایسه با پخش کردن دستورهای `print()` در سراسر کد، می‌توانند روند پیدا کردن خطا را بسیار سریع‌تر کنند.

اگر برنامه‌نویس باتجربه‌ای باشید، احتمالاً با من موافقید که میان مهارت برنامه‌نویسی و توانایی اشکال‌زدایی مؤثر ارتباطی وجود دارد. منظورم از اشکال‌زدایی مؤثر این است که بتوانید مشکل را تشخیص دهید و با کمترین دردسر برطرفش کنید. یادگیری استفادهٔ درست از اشکال‌زدا به شما در رسیدن به این مهارت کمک می‌کند. عادت کردن به جابه‌جایی در محیط اشکال‌زدایی کمی زمان می‌برد؛ هدف این آموزش این است که پیش از استفاده از `pdb` در کدهای خودتان، کمی با آن تمرین کنید!

## اجرای بازی

حالا که دربارهٔ کاربرد اشکال‌زدا صحبت کردیم، وقت آن است که آن را در عمل ببینیم. ابتدا اگر هنوز این مخزن را دریافت نکرده‌اید، آن را کلون کنید. اگر `git` ندارید، پیشنهاد می‌کنم از آن یا ابزار دیگری برای کنترل نسخه استفاده کنید. راهنمای نصب `git` را می‌توانید [اینجا](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) بخوانید. پس از نصب، دستور زیر را در ترمینال وارد کنید:

<div dir="ltr">

```shell
git clone https://github.com/spiside/pdb-tutorial
```

</div>

**نکته:** اگر این دستور برای شما کار نکرد، [راهنمای کلون کردن مخزن در گیت‌هاب](https://help.github.com/articles/cloning-a-repository/) را دنبال کنید.

حالا به پوشهٔ اصلی پروژه بروید و دستورالعمل تمرین را بخوانید:

<div dir="ltr">

```shell
cd /path/to/pdb-tutorial
```

</div>

فایل اصلی: `instructions.txt`؛ [ترجمهٔ فارسی دستورالعمل](instructions.fa.txt):

مدیرتان این پروژه را به شما سپرده است تا برای یک مشتری اصلاحش کنید. قرار است یک بازی سادهٔ تاس باشد که در آن باید مجموع مقدار تاس‌ها را در ۶ نوبت پیاپی درست حساب کنید.

مشکل این است که برنامه‌نویس قبلی روش اشکال‌زدایی مؤثر را نمی‌دانسته است. حالا نوبت شماست که خطاها را برطرف کنید و بازی را بالاخره قابل اجرا کنید.

برای اجرای بازی باید فایل main.py را اجرا کنید.

به نظر آسان می‌رسد! ابتدا بازی را اجرا کنیم تا ببینیم چه مشکلی دارد. برای اجرای برنامه، دستور زیر را در ترمینال وارد کنید:

<div dir="ltr">

```shell
python main.py
```

</div>

باید خروجی‌ای شبیه این ببینید:

<div dir="ltr">

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

</div>

انگار برنامه‌نویس قبلی کمی... شوخ‌طبع بوده است؟ به‌هرحال، عدد 17 را وارد کنیم، چون مجموع مقدار تاس‌ها همین است.

<div dir="ltr">

```
Sigh. What is your guess?: 17
Sorry that's wrong
The answer is: 5
Like seriously, how could you mess that up
Wins: 0 Loses 1
Would you like to play again?[Y/n]: 
```

</div>

عجیب است. برنامه می‌گوید پاسخ 5 است، ولی واضح است که اشتباه می‌کند! شاید محاسبهٔ مجموع تاس‌ها مشکل دارد؛ برای بررسی، یک بار دیگر بازی کنیم. ظاهراً برای بازی دوباره باید `'Y'` را وارد کنیم. همین کار را انجام می‌دهیم.

<div dir="ltr">

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

</div>

عجیب‌تر شد! با اینکه ورودی ظاهراً معتبر بود، برنامه یک استثنا ایجاد کرد. حالا دیگر می‌توانیم با اطمینان بگوییم برنامه خراب است؛ پس اشکال‌زدایی را شروع کنیم!

## مبانی `pdb`: آشنایی با اشکال‌زدای پایتون

بالاخره وقت کار با `pdb`، اشکال‌زدای خود پایتون، رسیده است. این ابزار بخشی از کتابخانهٔ استاندارد پایتون است و مانند کتابخانه‌های دیگر از آن استفاده می‌کنیم. ابتدا ماژول `pdb` را وارد می‌کنیم و سپس یکی از توابع آن را فراخوانی می‌کنیم تا یک نقطهٔ توقف در برنامه قرار دهیم. روش رایج این است که دستور وارد کردن ماژول **و** فراخوانی تابع را در همان خطی بنویسیم که می‌خواهیم اجرای برنامه در آن متوقف شود:

<div dir="ltr">

```python
import pdb; pdb.set_trace()
```

</div>

از پایتون ۳٫۷ به بعد، می‌توانید به‌جای `import pdb; pdb.set_trace()` از تابع داخلی `breakpoint()` استفاده کنید:

<div dir="ltr">

```python
breakpoint()
```

</div>

توابع [`set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace) و [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint) نقطهٔ توقف را مستقیماً در محل فراخوانی در کد قرار می‌دهند. در این آموزش از `set_trace()` استفاده می‌کنیم، چون در همهٔ نسخه‌های پایتون مورد بحث پشتیبانی می‌شود. فایل `main.py` را باز کنید و در خط 8 نقطهٔ توقف را اضافه کنید:

فایل: `main.py`

<div dir="ltr">

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

</div>

خوب، دوباره `main.py` را اجرا کنیم و ببینیم چه اتفاقی می‌افتد.

<div dir="ltr">

```shell
python main.py
```

</div>



<div dir="ltr">

```
Add the values of the dice
It's really that easy
What are you doing with your life.
> /Users/Development/pdb-tutorial/main.py(9)main()
-> GameRunner.run()
(Pdb) 
```

</div>

عالی! حالا در میانهٔ اجرای برنامه هستیم و می‌توانیم وضعیت آن را بررسی کنیم. به نظرم اولین مشکلی که باید حل کنیم، محاسبهٔ درست مجموع مقدار تاس‌هاست.

اگر با مفسر پایتون آشنا باشید، بخش زیادی از دانسته‌هایتان در `pdb` هم کاربرد دارد. البته چند نکتهٔ غافلگیرکننده وجود دارد که در بخش پیشرفته به آن‌ها می‌رسیم. فعلاً چند دستور یاد بگیریم که به حل مشکل جمع کمک می‌کنند.

## پنج دستور `pdb` که شما را شگفت‌زده می‌کنند

این پنج دستور از مستندات `pdb` گرفته شده‌اند. وقتی آن‌ها را یاد بگیرید، تعجب می‌کنید که قبلاً چطور بدون آن‌ها کار می‌کردید!

1. `l(ist)` — نمایش 11 خط پیرامون خط فعلی یا ادامهٔ فهرست قبلی.
2. `s(tep)` — اجرای خط فعلی و توقف در اولین فرصت ممکن.
3. `n(ext)` — ادامهٔ اجرا تا رسیدن به خط بعدی در تابع فعلی یا بازگشت آن تابع.
4. `b(reak)` — تعیین نقطهٔ توقف، بر اساس آرگومان داده‌شده.
5. `r(eturn)` — ادامهٔ اجرا تا بازگشت تابع فعلی.

بخش پایانی هر دستور داخل پرانتز آمده است. این یعنی هنگام وارد کردن دستور در محیط `pdb`، نوشتن آن بخش _اختیاری_ است. این کار تایپ را کمتر می‌کند، اما یک نکتهٔ مهم دارد: اگر نام متغیری مانند `l` یا `n` باشد، دستور `pdb` اولویت دارد. مثلاً فرض کنید متغیری به نام `c` دارید و می‌خواهید مقدارش را ببینید. اگر در `pdb` بنویسید `c`، در واقع دستور `c(ontinue)` اجرا می‌شود و برنامه تا رسیدن به نقطهٔ توقف بعدی به کار خود ادامه می‌دهد!

**نکته:** من و بسیاری از برنامه‌نویسان دیگر، استفاده از نام‌های کوتاه و نامفهومی مانند `a`، `b` و `gme` را توصیه نمی‌کنیم. چنین نام‌هایی معنای روشنی ندارند و خوانندهٔ کد را سردرگم می‌کنند. اینجا فقط مشکلاتی را نشان می‌دهم که این نام‌ها ممکن است هنگام کار با `pdb` ایجاد کنند.

**نکتهٔ دیگر:** دستور `h(elp)` هم مفید است: بدون آرگومان، فهرست دستورهای موجود را نمایش می‌دهد؛ اگر نام دستوری را به آن بدهید، راهنمای همان دستور را چاپ می‌کند.

در ادامه از شکل کوتاه دستورها استفاده می‌کنم. هر دستور تازه‌ای هم که به کار ببرم، توضیح خواهم داد. از اولین دستور شروع کنیم.

### ۱. دستور `l(ist)`؛ وقتی حوصلهٔ باز کردن فایل کد را نداریم

<div dir="ltr">

```
l(ist) [first [,last]]
    List source code for the current file. Without arguments, list 11 lines around the current line
    or continue the previous listing. With one argument, list 11 lines starting at that line.
    With two arguments, list the given range; if the second argument is less than the first, it is a count.
```

</div>

راهنمای دستور: کد فایل فعلی را نشان می‌دهد. بدون آرگومان، 11 خط پیرامون خط فعلی یا ادامهٔ فهرست قبلی نمایش داده می‌شود. با یک آرگومان، 11 خط از شمارهٔ مشخص‌شده نمایش داده می‌شود. با دو آرگومان، بازهٔ مشخص‌شده نمایش داده می‌شود؛ اگر عدد دوم از اول کوچک‌تر باشد، به‌عنوان تعداد خط‌ها در نظر گرفته می‌شود.

**نکته:** متن بالا خروجی دستور `help` برای `list` است. برای دیدن همین خروجی، در محیط تعاملی `pdb` بنویسید `help l`.

دستور `list` کد فایل فعلی را نمایش می‌دهد. آرگومان‌های آن اجازه می‌دهند بازهٔ خط‌های مورد نظر را مشخص کنید. این قابلیت وقتی در یک بستهٔ جانبی ناآشنا دنبال علت درست کار نکردن کدگذاری رشته‌ها می‌گردید، بسیار مفید است؛ _این اتفاق واقعاً برایم افتاده است!_

**نکته:** در پایتون ۳٫۲ و بالاتر، دستور `ll` یا «فهرست بلند» کد تابع یا قاب پشتهٔ فعلی را نشان می‌دهد. من معمولاً به‌جای `l` از آن استفاده می‌کنم، چون دیدن کل تابع بسیار مفیدتر از دیدن 11 خط پیرامون موقعیت فعلی است.

حالا در محیط بازِ `pdb`، دستور `l` را وارد کنید و خروجی را ببینید:

<div dir="ltr">

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

</div>

برای دیدن کل فایل، می‌توانیم بازهٔ 1 تا 13 را به دستور `list` بدهیم:

<div dir="ltr">

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

</div>

این فایل به‌تنهایی اطلاعات زیادی به ما نمی‌دهد، اما می‌بینیم که متد `run()` از کلاس `GameRunner` را فراخوانی می‌کند. شاید فکر کنید: «خوب، یک نقطهٔ توقف `pdb` در متد `run` در فایل `dicegame/runner.py` می‌گذارم!» این روش جواب می‌دهد، اما راه آسان‌تری هم هست: دستور `step` که در ادامه می‌بینیم.

### ۲. دستور `s(tep)`؛ ببینیم این متد چه می‌کند...

<div dir="ltr">

```
s(tep)
    Execute the current line, stop at the first possible occasion
    (either in a function that is called or in the current
    function).
```

</div>

راهنمای دستور: خط فعلی را اجرا می‌کند و در اولین فرصت ممکن، چه در تابع فراخوانی‌شده و چه در تابع فعلی، متوقف می‌شود.

موقعیت اجرا هنوز باید روی خط 9 باشد. علامت `->` در خروجی `list` خط فعلی را مشخص می‌کند. دستور `step` را اجرا کنیم و نتیجه را ببینیم.

<div dir="ltr">

```
(Pdb) s
--Call--
> /Users/Development/pdb-tutorial/dicegame/runner.py(21)run()
-> @classmethod
```

</div>

عالی! اکنون در خط 21 فایل `runner.py` هستیم. این را از خط زیر می‌فهمیم:

`> /Users/Development/pdb-tutorial/dicegame/runner.py(21)run()`

ولی هنوز کد اطراف را نمی‌بینیم. دستور `list` را اجرا کنید تا متد را بررسی کنیم.

<div dir="ltr">

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

</div>

حالا اطلاعات بیشتری از متد `run()` داریم، اما هنوز روی خط 21 هستیم. یک بار دیگر `step` را اجرا کنیم تا وارد خود متد شویم، سپس با `list` موقعیت فعلی را ببینیم.

<div dir="ltr">

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

</div>

همان‌طور که می‌بینید، به متغیر بدنام‌گذاری‌شدهٔ `c` رسیده‌ایم؛ تلاش برای دیدن مقدار آن می‌تواند دردسرساز شود. توضیح قبلی دربارهٔ دستور `c(ontinue)` را به یاد دارید؟ اکنون درست پیش از حلقهٔ `while` هستیم. وارد حلقه شویم و ببینیم چه چیز دیگری پیدا می‌کنیم.

### ۳. دستور `n(ext)`؛ امیدوارم این خط استثنا ایجاد نکند!

<div dir="ltr">

```
n(ext)
    Continue execution until the next line in the current function
    is reached or it returns.
```

</div>

راهنمای دستور: اجرا را تا رسیدن به خط بعدی در تابع فعلی یا بازگشت آن تابع ادامه می‌دهد.

از موقعیت فعلی، دستور `n(ext)` و سپس `list` را وارد کنید و نتیجه را ببینید. الگوی کار را متوجه شدید؟

**نکته:** دستور `n(ext)` فراخوانی تابع را اجرا می‌کند و از آن عبور می‌کند، ولی `s(tep)` وارد تابع فراخوانی‌شده می‌شود و در اولین خط آن توقف می‌کند.

<div dir="ltr">

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

</div>

حالا روی دستور `while True` هستیم! می‌توانیم بارها `next` را اجرا کنیم تا برنامه پایان یابد یا استثنایی رخ دهد. سه بار دیگر `next` را اجرا کنید تا به حلقهٔ `for` برسید، سپس `list` را وارد کنید.

<div dir="ltr">

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

</div>

از اینجا به بعد، با تکرار دستور `next`، حلقهٔ `for` به تعداد اعضای `runner.dice` پیموده می‌شود. برای دیدن تعداد اعضا، در محیط تعاملی `pdb` تابع `len()` را روی `runner.dice` فراخوانی کنید؛ نتیجه باید 5 باشد.

<div dir="ltr">

```
(Pdb) len(runner.dice)
5
```

</div>

چون _فقط_ 5 عضو داریم، می‌توانیم با تکرار `next` از حلقه عبور کنیم. اما اگر 50 یا حتی 10,000 عضو داشتیم چه؟ راه بهتر این است که یک نقطهٔ توقف تعیین کنیم و با `continue` تا آن نقطه پیش برویم.

### ۴. دستور `b(reak)`؛ دیگر نمی‌خواهم `n` تایپ کنم

<div dir="ltr">

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

</div>

راهنمای دستور: بدون آرگومان، همهٔ نقطه‌های توقف را فهرست می‌کند. با شمارهٔ خط، در همان خط از فایل فعلی نقطهٔ توقف می‌گذارد. با نام تابع، در اولین خط قابل اجرای آن تابع توقف می‌گذارد. آرگومان دوم، در صورت وجود، رشته‌ای حاوی یک عبارت شرطی است؛ توقف فقط زمانی انجام می‌شود که نتیجهٔ شرط درست باشد.

برای تعیین نقطهٔ توقف در فایلی دیگر، حتی فایلی که هنوز بارگذاری نشده است، می‌توانید نام فایل و دونقطه را پیش از شمارهٔ خط بیاورید. فایل در مسیرهای `sys.path` جست‌وجو می‌شود و پسوند `.py` را می‌توان حذف کرد.

در این آموزش فقط روی دو بند اول راهنمای `b(reak)` تمرکز می‌کنیم. همان‌طور که گفتیم، می‌خواهیم پس از حلقهٔ `for` یک نقطهٔ توقف بگذاریم تا بررسی متد `run()` را ادامه دهیم. خط 34 جای مناسبی است، چون تابع دریافت ورودی در آن قرار دارد و در هر صورت منتظر ورودی کاربر می‌ماند. دستور `b 34` را وارد کنید و سپس با `continue` تا آن نقطه پیش بروید.

<div dir="ltr">

```
(Pdb) b 34
Breakpoint 1 at /Users/Development/pdb-tutorial/dicegame/runner.py(34)run()
(Pdb) c

[...] # prints some dice

> /Users/Development/pdb-tutorial/dicegame/runner.py(34)run()
-> guess = input("Sigh. What is your guess?: ")
```

</div>

با اجرای `break` بدون آرگومان می‌توانیم فهرست نقطه‌های توقف تعیین‌شده را هم ببینیم.

<div dir="ltr">

```
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /Users/Development/pdb-tutorial/dicegame/runner.py:34
    breakpoint already hit 1 time
```

</div>

برای حذف نقطهٔ توقف، دستور `cl(ear)` را همراه با شمارهٔ آن وارد کنید. شماره در ستون سمت چپ خروجی بالا دیده می‌شود. اکنون با دستور `clear` و شمارهٔ 1، این نقطهٔ توقف را حذف کنیم.

**نکته:** اگر به `clear` آرگومانی ندهید، می‌توانید همهٔ نقطه‌های توقف را حذف کنید.

<div dir="ltr">

```
(Pdb) cl 1
Deleted breakpoint 1 at /Users/Development/pdb-tutorial/dicegame/runner.py:34
```

</div>

حالا با `next` تابع `input()` را اجرا کنیم. عدد 10 را به‌عنوان حدس وارد کنید. پس از بازگشت به محیط تعاملی `pdb`، دستور `list` را اجرا کنید تا چند خط بعدی را ببینیم.

<div dir="ltr">

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

</div>

یادتان باشد می‌خواهیم بفهمیم چرا در اولین اجرای بازی، حدس ما نادرست تشخیص داده شد. ظاهراً شرط برابری `guess == runner.answer()` مشکل دارد. بهتر است متد `runner.answer()` را بررسی کنیم؛ شاید خطا آنجا باشد. ابتدا `next` و سپس `step` را اجرا کنید تا وارد این متد شویم.

<div dir="ltr">

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

</div>

فکر می‌کنم مشکل را پیدا کردیم! در خط 18، متغیر `total` ظاهراً مقدار تاس‌ها را آن‌طور که می‌خواهیم جمع نمی‌کند. بررسی کنیم آیا شیء `die` ویژگی‌ای دارد که مقدار تاس را نگه دارد. برای رسیدن به خط 18، یک نقطهٔ توقف بگذارید یا `next` را تکرار کنید تا به اولین دور حلقه برسید. سپس تابع `dir()` را روی نمونهٔ `die` فراخوانی کنید تا متدها و ویژگی‌های آن را ببینیم.

<div dir="ltr">

```
-> total += 1
(Pdb) dir(die)
['__class__', '__delattr__', [...], 'create_dice', 'roll', 'show', 'value']
```

</div>

بله، ویژگی `value` وجود دارد! مقدارش را ببینیم؛ البته احتمالاً مقدار تاس شما با تاس من فرق می‌کند. برای اطمینان، متد `show()` را هم فراخوانی کنیم و ببینیم این مقدار با شکل تاس مطابقت دارد یا نه.

<div dir="ltr">

```
(Pdb) die.value
2
(Pdb) die.show()
'---------\n|*      |\n|       |\n|      *|\n---------'
```

</div>

**نکته:** اگر می‌خواهید نویسهٔ `\n` واقعاً به‌صورت خط جدید نمایش داده شود، `die.show()` را به تابع `print()` بدهید.

ظاهراً همه‌چیز مطابق انتظار است و می‌توانیم متد `answer` را اصلاح کنیم. بااین‌حال، شاید بخواهید اشکال‌زدایی را ادامه دهید و همهٔ خطاها را یک‌جا پیدا کنید. متأسفانه دوباره داخل حلقهٔ `for` گیر افتاده‌ایم. شاید به فکر تعیین نقطهٔ توقف در خط 19 و اجرای `continue` بیفتید، اما اینجا راه بهتری هم هست.

### ۵. دستور `r(eturn)`؛ می‌خواهم از این تابع بیرون بیایم

<div dir="ltr">

```
r(eturn)
    Continue execution until the current function returns.
```

</div>

راهنمای دستور: اجرا را تا بازگشت تابع فعلی ادامه می‌دهد.

دستور `return` ابزاری عالی برای کاربران حرفه‌ای است که می‌خواهند نتیجهٔ نهایی یک تابع را بررسی کنند. البته می‌توانید روی دستور بازگشت تابع نقطهٔ توقف بگذارید، اما اگر تابع چند دستور `return` داشته باشد، دستور `return` در `pdb` کار را آسان‌تر می‌کند: مسیر واقعی اجرا را تا همان بازگشتی دنبال می‌کند که قرار است رخ دهد. حالا این دستور را اجرا کنیم و به انتهای تابع برسیم.

<div dir="ltr">

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

</div>

برای بررسی مقدار بازگشتی `total`، می‌توانید همین‌جا نام `total` را وارد کنید یا مقدار نهایی را در خط زیر `--Return--` ببینید. سپس برای بازگشت به متد `run()`، دستور `next` را اجرا کنید.

اکنون می‌توانید با `exit()` **یا** `CTRL+D` از اشکال‌زدای `pdb` خارج شوید، درست مانند محیط تعاملی پایتون. با این پنج دستور باید بتوانید چند خطای دیگر را پیدا کنید و بعد سراغ مثال‌های پیشرفته‌تر بروید.

## مباحث پیشرفتهٔ `pdb`

در ادامه چند قابلیت پیشرفتهٔ دیگر `pdb` را می‌بینیم.

### دستور `!` یا bang

<div dir="ltr">

```
!
  Execute the (one-line) statement in the context of the current stack frame.
```

</div>

راهنمای دستور: یک دستور تک‌خطی پایتون را در محیط قاب فعلی پشته اجرا می‌کند.

علامت `!` به `pdb` می‌گوید عبارت پس از آن کد پایتون است، نه دستور اشکال‌زدا. این قابلیت برای متغیر `c` در متد `run()` به کار می‌آید. همان‌طور که در ابتدای آموزش گفتیم، وارد کردن `c` در `pdb` دستور `continue` را اجرا می‌کند. در محیط تعاملی `pdb` به خط 26 فایل `runner.py` بروید و پیش از `c` علامت `!` بگذارید تا نتیجه را ببینید.

<div dir="ltr">

```
 (Pdb) !c
 0
```

</div>

نتیجه همان چیزی است که انتظار داشتیم، چون در خط 25 مقداردهی `c = 0` انجام شده است!

### دستور `commands`

<div dir="ltr">

```
commands [bpnumber]
        (com) ...
        (com) end
        (Pdb)

        Specify a list of commands for breakpoint number bpnumber.
```

</div>

راهنمای دستور: فهرستی از دستورها را برای نقطهٔ توقف با شمارهٔ `bpnumber` مشخص می‌کند.

دستور `commands` مشخص می‌کند هر بار که اجرا به یک نقطهٔ توقف معین رسید، چه کد پایتون یا دستورهای `pdb` اجرا شوند. با شروع بلوک `commands`، اعلان به `(com)` تغییر می‌کند. کد و دستورهایی که اینجا می‌نویسید، درست مانند زمانی اجرا می‌شوند که پس از رسیدن به آن نقطهٔ توقف، آن‌ها را در اعلان `(Pdb)` وارد کرده باشید. با نوشتن `end`، تعریف دستورها پایان می‌یابد و اعلان دوباره از `(com)` به `(Pdb)` برمی‌گردد. این قابلیت برای زیر نظر گرفتن متغیرها درون حلقه بسیار مفید است، چون دیگر لازم نیست هر بار خودتان مقدارشان را چاپ کنید. یک مثال ببینیم. در ترمینال به پوشهٔ اصلی پروژه بروید و بنویسید:

<div dir="ltr">

```
python -m pdb main.py
```

</div>

به خط 8 برسید و با `s(tep)` وارد متد `run()` از کلاس `GameRunner` شوید. سپس در خط 17 یک نقطهٔ توقف تعیین کنید.

<div dir="ltr">

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

</div>

به این ترتیب، نقطهٔ توقفی با شمارهٔ `4` در ابتدای حلقهٔ متد `answer()` قرار می‌گیرد؛ همان متدی که مجموع مقدار تاس‌ها را حساب می‌کند. حالا با `commands` مشخص کنیم که هنگام رسیدن به این نقطه، مقدار متغیر `total` چاپ شود.

<div dir="ltr">

```
(Pdb) commands 4
(com) print(f"The total value as of now is {total}")
(com) end
```

</div>

اکنون دستورهای مربوط به نقطهٔ توقف شمارهٔ 4 را تعریف کرده‌ایم تا با رسیدن به آن اجرا شوند. با `c(ontinue)` تا این نقطه پیش برویم.

<div dir="ltr">

```
(Pdb) c
[...] # You will have to guess a number
The total value as of now is 0
> /Users/Development/pdb-tutorial/dicegame/runner.py(17)answer()
-> for die in self.dice:
(Pdb)
```

</div>

می‌بینیم که به‌محض رسیدن به نقطهٔ توقف، دستور چاپ اجرا شد. دوباره `c(ontinue)` را اجرا کنیم و نتیجه را ببینیم.

<div dir="ltr">

```
(Pdb) c
[...] 
The total value as of now is 1
> /Users/Development/pdb-tutorial/dicegame/runner.py(17)answer()
-> for die in self.dice:
(Pdb)
```

</div>

با رسیدن دوباره به نقطهٔ توقف، دستورهای تعریف‌شده در `commands` دوباره اجرا می‌شوند. می‌بینید که این قابلیت، به‌ویژه در حلقه‌ها، چقدر می‌تواند مفید باشد.

### اشکال‌زدایی پس از وقوع خطا با `pdb`

<div dir="ltr">

```
pdb.post_mortem(traceback=None)
    Enter post-mortem debugging of the given traceback object. If no traceback is given, it uses the one of the exception that is currently being handled
    (an exception must be being handled if the default is to be used).

pdb.pm()
    Enter post-mortem debugging of the traceback found in sys.last_traceback. 
```

</div>

راهنمای توابع: `pdb.post_mortem(traceback=None)` اشکال‌زدایی پس از خطا را با شیء ردگیری پشتهٔ داده‌شده آغاز می‌کند. اگر آرگومانی ندهید، از ردگیری استثنایی استفاده می‌کند که در همان لحظه در حال مدیریت است؛ بنابراین برای استفاده از حالت پیش‌فرض باید در حال مدیریت یک استثنا باشید.

تابع `pdb.pm()` اشکال‌زدایی پس از خطا را با ردگیری موجود در `sys.last_traceback` آغاز می‌کند.

هرچند `post_mortem()` و `pm()` شبیه هم به نظر می‌رسند، تفاوتشان در ردگیری پشته‌ای (`traceback`) است که استفاده می‌کنند. من معمولاً `post_mortem()` را در بلوک `except` به کار می‌برم. بااین‌حال، اینجا `pm()` را بررسی می‌کنیم، چون از نظر من کمی توانمندتر است. ببینیم در عمل چطور کار می‌کند.

در پوشهٔ اصلی پروژه، دستور `python` را در ترمینال وارد کنید تا محیط تعاملی پایتون باز شود. سپس تابع `main` را از ماژول `main` و خود ماژول `pdb` را وارد کنید. بازی را ادامه دهید تا با وارد کردن `Y` برای بازی دوباره، همان استثنا رخ دهد.

<div dir="ltr">

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

</div>

حالا تابع `pm()` از ماژول `pdb` را فراخوانی کنیم و ببینیم چه اتفاقی می‌افتد.

<div dir="ltr">

```
>>> pdb.pm()
> /Users/Development/pdb-tutorial/dicegame/utils.py(13)i_just_throw_an_exception()
-> raise UnnecessaryError("You actually called this function...")
(Pdb) 
```

</div>

دیدید؟ از محل وقوع آخرین استثنا وارد محیط `pdb` شدیم. حالا می‌توانیم وضعیت برنامه را پیش از توقف ناشی از خطا بررسی کنیم؛ این کار به پیدا کردن علت مشکل کمک می‌کند.

**نکته:** می‌توانید اسکریپت `main.py` را با `python -m pdb main.py` اجرا کنید و با `continue` پیش بروید تا استثنایی رخ دهد. پایتون هنگام وقوع استثنای مدیریت‌نشده، خودکار وارد حالت اشکال‌زدایی پس از خطا می‌شود.

## پایان

تبریک می‌گویم که به پایان رسیدید و ممنون که این آموزش را دنبال کردید! اگر نظر، نقد یا مثال پیشرفتهٔ دیگری دارید، از پول ریکوئست شما استقبال می‌کنم.

</div>
