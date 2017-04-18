# Assignment 0: Welcome to Python!
**Due: 11:59:59 PM, Tue April 11th**

## Overview
This introductory assignment aims to introduce you to a few Python fundamentals. More importantly, the goal of this warmup assignment is to ensure that your local Python installation is set up correctly and that you are familiar with the CS41 submission process.

At a high level, for this assignment you will implement a Python script that answers questions about yourself.

*Expected Time: 1 hour (if it takes much longer than that, email us)*

Note: Get started early! We want to resolve any installation or submission problems earlier rather than later.

## Review

If you would like, get a quick refresher by flipping through our slides from the first week on the [course website.](http://stanfordpython.com/#lectures)

## Starter Files

There are no starter files for this assignment. You will create and submit a file called `intro.py`.

# Program Specification

Your program will prompt a line of input from the user (any prompt is acceptable), check if it matches one of the following questions, and if so, print an answer to the question. 

- What is your name?
- What is your quest?
- What do you do in your free time?
- What else would you like to tell us that you haven't already expressed through the application?
- What are you most excited to learn about this quarter?

Additionally, if the user enters the special input: `"What can you answer?"`, you must print out the list of questions that your program can answer, one question per line.

If the user's input does not exactly match one of these above inputs, your program can do whatever it wants.

## Sample Demonstration

Your program should be able to emulate the following sample runs.

```
$ python3 intro.py
Ask me a question: What is your name?
It is Arthur, King of the Britons.

$ python3 intro.py
Ask me a question: What is your quest?
To seek the holy grail.

$ python3 intro.py
Ask me a question: What is the airspeed velocity of an unladen swallow?
(error: unknown question) What do you mean? African or European swallow?

$ python3 intro.py
Ask me a question: What can you answer?
What is your name?
What is your quest?
What do you do in your free time?
What else would you like to tell us that you haven't already expressed through the application?
What are you most excited to learn about this quarter?
```

In the above cases, the input prompt is `"Ask me a question: "`, and the user types her response to finish the line.

## Extensions
> Extensions on Assignment 0? If you insist.

This section of an assignment handout gives a few of our suggestions if you're looking for ways to go above and beyond the requirements of the assignment. At no point are you required to implement an extension - although they sometimes provide interesting challenges or alternative approaches to problem-solving.

In general, when you submit an extension to an assignment, add `-ext` to the end of the filename. In this case, if you want to submit an extension, you should submit both an unmodified `intro.py` file that implements the unextended assignment and an `intro-ext.py` file that implements your extension.

### Binge-Watch Monty Python Videos on Youtube
Including but not limited to:

- [The Cheese Shop](https://www.youtube.com/watch?v=cWDdd5KKhts)
- [The Bridge of Death](https://www.youtube.com/watch?v=dPOyOM7wxlE)
- [The Dead Parrot](https://www.youtube.com/watch?v=4vuW6tQ0218)

You can tell your family that it's "for class."

### Multiple Questions
Allow the user to ask more than just one question by putting your question-answering logic in a loop. Continue until the user enters an empty line.

### Read Questions and Answers from a File
Store questions and answers in some file format of your devising, and read the questions and answers from the file into some data structure before prompting the user for answers.

### Dialogue
Implement some notion of dialogue, where the user can repeatedly chat with the program, and the program's behavior changes based on the user's inputs.

### Answer More Questions?
Expand the range of questions that can be answered. You can add the classic icebreaker questions "What is your favorite flavor of ice cream" and "If you could have any superpower, what would it be?" Feel free to add any additional questions and answers you'd like.

### Match Flexibility
Use another matching strategy to check if the user has asked a particular question. You can check substrings, regular expressions, edit distance (perhaps edit distance on substrings) or any number of clever metrics.


## Grading

Your grade will be assessed on completion. If you successfully submit a Python program that answers each of the list of questions, you will receive full credit on this assignment.

We will not be evaluating any style on this assignment.

## Submitting

See the [submission instructions](https://github.com/stanfordpython/python-handouts/blob/master/submitting-assignments.md) on the course website.

For assignment 0, the key ideas are:
```
$ ssh <sunetid>@myth.stanford.edu "mkdir -p ~/cs41/assign0"
$ scp <path/to/intro.py> <sunetid>@myth.stanford.edu:~/cs41/assign0/
$ ssh <sunetid>@myth.stanford.edu
<... connect to myth ...>
myth$ cd ~/cs41/assign0/
myth$ /usr/class/cs41/tools/submit
```

> With <3 by @sredmond 
