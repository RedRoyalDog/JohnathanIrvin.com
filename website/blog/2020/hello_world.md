---
title: Hello World
date: 2020-10-10
description: Symbolic "Hello World" introductory post inspired by an introductory program first found in 1972 in A Tutorial Introduction to the Language B by Bell Laboratories.
---

For many programmers, the first program they write in any given language is the "Hello World" program first found in *[A Tutorial Introduction to the Language B by Bell Laboratories](https://www.bell-labs.com/usr/dmr/www/bintro.html)*. It seemed apt to label this article accordingly and incorporate "Hello World" into the content. As an homage to the history of programming, let's write this simple program.

## Prerequisites

We will need a text editor. A text editor is a program that allows you to edit just the letters of a file without adding any additional information. This is not to be confused with Microsoft Word or a similar tool known as a Word Processor. We will ignore Word Processors and focus on text editors. You may use any simple text editor program; examples include [Microsoft Notepad](https://en.wikipedia.org/wiki/Microsoft_Notepad), [Notepad++](https://notepad-plus-plus.org/), [Vim](https://www.vim.org/), and [GNU Nano](https://www.nano-editor.org/). I will use Vim. Installing and using your preferred text editor will not be explained in this article.

This example will be using the programming language [Python](https://www.python.org/). It is not required to know Python or have any prior programming experience to understand and create our first program. Writing your first program requires that you have your environment set up to run Python. To do so, follow the [Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Download) on the Python wiki or follow the [Python3 Installation and Setup Guide by Real Python](https://realpython.com/installing-python/). I recommend the latter.

## First Program

Writing and executing a simple "Hello World" program is fairly simple. Most languages require you to tell the computer using a specific command that you would like to output some characters, in this case, "Hello World," to the screen. The ```print``` command allows us to output some text to the screen. Please note that we don't always output the screen (the terminal), and in the past, we've output to a physical printer or similar device. Using your preferred text editor, write the following in a new file named ```hello_world.py```:

```python
print('Hello World!')
```

Save your work, and close the text editor. Open up a terminal application like Powershell on Windows or bash on Ubuntu. If you're on Windows, it is as easy as hitting your Windows Key and searching for `Powershell` in your search. On Ubuntu, you can press your corresponding key to open up the search and look for `Terminal`. One the application appears, click it to start the terminal application. One the terminal has started, type ```python hello_world.py``` and press enter. If all has gone well, you should see `Hello World!` appear in your terminal.

The following image will illustrate by using Vim, the text editor I mentioned before, to create a new file, save it, and then run our program using Python:

![Animated image displaying "hello world"](./images/hello_world.svg)

## Conclusion

We've barely scratched the surface of programming. Ask yourself a few of the following questions: What exactly is `print`? Can I change `Hello World!` to any text I'd like? Try changing `Hello World!` to `Hello Johnny!` and rerunning the program. What happened? Is there a way that I could have a different output  time I run the program? While the `Hello World!` program ensures that our environment is set up correctly; it doesn't do much.

What's next? I recommend researching variables in Python.