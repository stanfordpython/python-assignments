# Assignment 0: Welcome to Python!
> Due: 11:59 PM, Tuesday Jan 21

## Overview

This introductory assignment aims to give you practice with a few of the Python fundamentals we've covered in class. More importantly, the goal of this warmup assignment is to ensure that your local Python installation is set up correctly and that you are familiar with the CS41 submission process.

At a high level, in this assignment you will write code to calculate coconut-carrying capacity, play the part of a cheese shop owner, and challenge knights to cross the Bridge of Death.

- *Expected Time: 1.5 hours*
- *Max Time: 3 hours*

Note: Get started early! We want to resolve any installation or submission problems earlier rather than later.

## Review

If you would like to, get a quick refresher by flipping through our slides from the first week on the [course website](https://stanfordpython.com/#lectures).

## Installing Python

Follow our instructions for installing Python and setting up a virtual environment.

- For macOS users, follow [these instructions](https://github.com/stanfordpython/python-handouts/blob/master/installing-python-macos.md)
- For Linux users, follow [these instructions](https://github.com/stanfordpython/python-handouts/blob/master/installing-python-linux.md)
- For Windows users, follow [these instructions](https://github.com/stanfordpython/python-handouts/blob/master/installing-python-windows.md)

**IMPORTANT: Every time you open a new terminal session, you will need to activate your virtual environment again.**

## Starter Files

There are no starter files for this assignment. You will create and submit a files named `coconuts.py`, `cheese.py`, and `bridge.py`.

A reasonable starter file might look like:

```python
#!/usr/bin/env python3
"""Module-level comment."""

# Write additional code and functions here.

def main():
    # Write the main execution of your program here.
    
if __name__ == '__main__':
    main()
```

# Program Specifications

This assignment consists of three parts:

1. Coconut-Carrying Capacities,
2. The Cheese Shop, and
3. The Bridge of Death.

As a reminder, the interactive interpreter is your best friend! Use it heavily when experimenting with and exploring Python.

## Coconut-Carrying Capacities

Before anything else, watch [this three-minute video](https://www.youtube.com/watch?v=zqtS9xyl0f4) on Youtube. The transcript can be found [here](http://www.montypython.net/scripts/HG-cocoscene.php).

We're going to help the guards out and compute whether a collection of swallows can carry a collection of coconuts between them. We know that "a five ounce bird could not carry a one pound coconut," so we will assume that a 5.5 ounce bird can carry a one pound coconut. More specifically, we will assume that every 5.5 ounces of bird can carry one pound of coconut.

Create a file named `coconuts.py` in which we will write our program. In this portion of the assignment, we will ask the user for two numbers: the total ounces of birds that are carrying coconuts, and the total weight in pounds of the coconuts.

Prompt the user for the number of ounces of bird by asking: `"How many ounces of birds are carrying the coconuts? "`. Prompt the user for the number of pounds of coconut by asking: `"How many pounds of coconuts are there? "`. Remember to convert these values to `float`s! You can assume that the user input is formatted correctly.

If the total number of ounces of birds divided by the number of pounds of coconuts is at least 5.5 (including the value 5.5), then we will print out `"Yes! Carrying the coconuts is possible."`. Otherwise, print out `"No. Carrying the coconuts is impossible."`

### Sample Runs

Your program should be able to emulate the following sample runs. *Make sure to activate your virtual environment before executing these lines of code!*

```
(cs41-env)$ python coconuts.py
How many ounces of birds are carrying the coconuts? 5
How many pounds of coconuts are there? 1
No. Carrying the coconuts is impossible.

(cs41-env)$ python coconuts.py
How many ounces of birds are carrying the coconuts? 6.2
How many pounds of coconuts are there? 1.1
Yes! Carrying the coconuts is possible.

(cs41-env)$ python coconuts.py
How many ounces of birds are carrying the coconuts? 17
How many pounds of coconuts are there? 3
Yes! Carrying the coconuts is possible.

(cs41-env)$ python coconuts.py
How many ounces of birds are carrying the coconuts? 12.5
How many pounds of coconuts are there? 2.5
No. Carrying the coconuts is impossible.
```

### Hints

In all portions of this assignment, you may find it tedious to repeatedly enter inputs. You can create a file, for example called `coconuts-input.txt`, and populate it with the two lines `17` and `3` so that the file looks like:

```
17
3
```

Now, you can run the program with predetermined input by running:

```
(cs41-env)$ python3 coconuts.py < coconuts-input.txt
How many ounces of birds are carrying the coconuts? How many pounds of coconuts are there? Yes! Carrying the coconuts is possible.
```

The formatting will be compressed, and a little harder to read, but this debugging trick might be an efficiency gain for you in the later parts of the assignment.

## The Cheese Shop

Before anything else, watch [this five-minute video](https://www.facebook.com/MontyPython/videos/567922730042254/) (cw: gun violence) on Facebook. The transcript can be found [here](http://www.montypython.net/scripts/cheese.php).

In this part of the assignment, you will play the part of the Michael Palin, the owner of the National Cheese Emporium.

Unlike the owner in the sketch, you *do* have some cheeses, and you will repeatedly ask the user what cheese they would like, and then you will respond whether or not you have that cheese.

Make a list of `cheeses` containing `"Muenster"`, `"Cheddar"`, and `"Red Leicester"`; these are the cheeses you have in your shop.

Begin by printing the string `"Good morning. Welcome to the National Cheese Emporium!"` to the console.

Next, in a loop, we will repeatedly ask the user which cheese they would like to buy. If the user enters the exact name of a cheese that you have, affirm that you have the cheese they asked for in the format `"We have {}, yessir."`. If the user does not enter the exact name of a cheese that you have, say that you don't have that cheese in the form `"I'm afraid we don't have any {}."` and then reprompt the user to ask for another cheese.

The user is also allowed to enter special questions. If the user enters either of the strings `"You... do have some cheese, don't you?"` or `"Have you in fact got any cheese here at all?"`, you must reply by listing the number of cheeses that you have in the format `"We have {} cheese(s)!"`, along with the name of each type of cheese you have, one on each line.

### Sample Usage

Your program should be able to emulate the following sample runs. *Make sure to activate your virtual environment before executing these lines of code!*

```
(cs41-env)$ python cheese.py
Good morning. Welcome to the National Cheese Emporium!
What would you like? Red Windsor
I'm afraid we don't have any Red Windsor.
What would you like? Lancashire
I'm afraid we don't have any Lancashire.
What would you like? cheddar
I'm afraid we don't have any cheddar.
What would you like? Cheddar
We have Cheddar, yessir.

(cs41-env)$ python cheese.py
Good morning. Welcome to the National Cheese Emporium!
What would you like? Red Windsor
I'm afraid we don't have any Red Windsor.
What would you like? cHeDdAr
I'm afraid we don't have any cHeDdAr.
What would you like? Have you in fact got any cheese here at all?
We have 3 cheese(s)!
Muenster
Cheddar
Red Leicester
What would you like? exit
I'm afraid we don't have any exit.
What would you like? LET ME OUT
I'm afraid we don't have any LET ME OUT.
What would you like? Cheddar
We have Cheddar, yessir.
```

For anything that is not specified in the above specification, your program can behave in anyway you'd like. For example, you can customize the prompts and messages.

### Hints

You can check that an element is contained in a collection by using the keyword `in`. You can use assignment expressions to assign a value to a variable in a loop condition.

## Keeper of the Bridge of Death

Before anything else, watch [this four-minute video](https://www.youtube.com/watch?v=dPOyOM7wxlE) on Youtube. The transcript can be found [here](http://www.montypython.net/scripts/HG-bridgescene.php).

In this assignment, you program will play the part of the Keeper of the Bridge of Death (a.k.a. the old person from Scene 24), and the user will play the part of the travelling knights. In this part of the assignment, you will gain practice with file reading, lists and strings.

First, create a file called `answers.txt` containing the following input:

```
your favorite color? blue
the capital of Assyria? ashur|kalhu|dur-sharrukin|nineveh|harra
your favorite color? blue|green
the airspeed velocity of an unladen swallow? 24mph|11mps
```

Each line of the file has the following format:

```
question? one possible response|another response|a third response
```
where the question is separated from the responses by the two-character string `"? "` and the options themselves are separated by the pipe character (`"|"`). You can assume that the file is well-formatted. You can also assume that no question or response will contain a `'?'` or a `'|'` (they may contain any other characters, including spaces).

As the Keeper of the Bridge of Death, you will ask travellers three questions each. Two of those will be the same, for every traveller, and then you'll ask a trick question. The `answers.txt` files provides the trick questions that you will ask. It also specifies how many travellers there will be: the number of travellers will be equal to the number of trick questions.

For each traveller, begin by printing a warning message: `"Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see."`.

Next, we will ask the travellers a series of questions. Each time, we will ask some question, prompting the user for input. Strip the user's input of any trailing spaces, `'.'`, or `'!'` characters.

Each traveller who wants to cross the bridge will be asked three questions. The first is `"What is your name? "`. The second is `"What is your quest? "`. The third will be drawn from the `answers.txt` file. To form the trick question, you'll ask the question from `answers.txt`, formatted as `"What is {question}? "`, where `question` refers to the format specification above.

For the trick question, the list of possible answers follows the question in the `answers.txt` file. If the user's input does not *contain* any of our reference options as a substring, ignoring case, we will cast the traveller into the Gorge of Eternal Peril (more on this further down) and immediately move onto the next traveller. (For example, the answer `"Lancelot"`, `"sir galahad of camelot  "` and `"  NO, THIS IS ROBIN "` all are successfully matched by the option list `Lancelot|Galahad|Robin`).

Successive travellers will be asked sequential questions from the file. For example, in the `answers.txt` file given above, there will be a total of four travellers, because there are four questions. These questions will, in order, be 

```
"What is your favorite color? "
"What is the capital of Assyria? "
"What is your favorite color? "
"What is the airspeed velocity of an unladen swallow? "
```

In this case, each will be the third question asked to four successive travellers, following the questions `"What is your name? "` and `"What is your quest? "`. Once you've asked all of the trick questions, you program should end normally. For example, if there were seven lines in `answers.txt`, at most seven travelling knights could visit the keeper.

If the travelling knight answers all three questions satisfactorily, print `"Right. Off you go."` and move on to the next traveller, prompting for their name.

When a traveller is cast into the Gorge of Eternal Peril, print out their name, in all capital letters, with the text `": Auuuuuuuugh!"`appended. For example, if Galahad fails to answer the trick question correctly, print out `"GALAHAD: Auuuuuuuugh!"`.

Each message you print to the console should be prefaced by `"KEEPER: "`.

Lastly, if the user answers *any* of your questions with text that ends with a `'?'` character, not counting trailing whitespace, periods, or exclamation points, you should reply: `"KEEPER: Auuuuuuuugh!"` and immediately end the program. Since the keeper is gone, be sure you don't keep answering questions.

### Hints

You can convert a string `s` to upper case by calling `s.upper()`, which returns the result of upper-casing `s`. Similarly, `s.lower()` returns `s` in lower-case.

Although there are many data structures that you can use to organize the data in this problem, it is sufficient to only use lists. We will see more powerful ways of structuring nested data like this later in the course.

You can split a string using `.split()`, which returns a list of strings. You can even pass `split` a separator character on which it will split chunks. For example:

```
"01-10-2019".split('-')  # => ['01', '10', '2019']
```

This program has a lot of interactive input. Use the input mocking trick we saw above to save yourself time in entering this assignment.

### Sample Usage

Your program should be able to emulate the following sample runs. *Make sure to activate your virtual environment before executing these lines of code!*

```
(cs41-env)$ python bridge.py
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? My name is Sir Lancelot of Camelot.
KEEPER: What is your quest? To seek the Holy Grail.
KEEPER: What is your favorite color? Blue.
KEEPER: Right. Off you go.
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? Sir Robin of Camelot.
KEEPER: What is your quest? To seek the Holy Grail.
KEEPER: What is the capital of Assyria? I don't know that!
SIR ROBIN OF CAMELOT: Auuuuuuuugh!
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? Sir Galahad of Camelot.
KEEPER: What is your quest? I seek the grail.
KEEPER: What is your favorite color? Red. No bl--
SIR GALAHAD OF CAMELOT: Auuuuuuuugh!
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? It is Arthur, King of the Britons.
KEEPER: What is your quest? To seek the Holy Grail.
KEEPER: What is the airspeed velocity of an unladen swallow? What do you mean? An African or European swallow?
KEEPER: Auuuuuuuugh!

(cs41-env)$ python bridge.py
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? Patrick
KEEPER: What is your quest? Meet Spongebob
KEEPER: What is your favorite color? PINK!
PATRICK: Auuuuuuuugh!
...

(cs41-env)$ python bridge.py
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? gAlAhAd Of CaMeLoT
KEEPER: What is your quest? What's *your* quest?!?
KEEPER: Auuuuuuuugh!

(cs41-env)$ python bridge.py
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? My name is Sir Lancelot of Camelot.
KEEPER: What is your quest? To seek the Holy Grail.
KEEPER: What is your favorite color? Blue.
KEEPER: Right. Off you go.
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? Sir Robin of Camelot.
KEEPER: What is your quest? To seek the Holy Grail.
KEEPER: What is the capital of Assyria? It was Ashur for a while, at least.
KEEPER: Right. Off you go.
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? Sir Galahad of Camelot.
KEEPER: What is your quest? I seek the grail.
KEEPER: What is your favorite color? Green.
KEEPER: Right. Off you go.
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? It is Arthur, King of the Britons.
KEEPER: What is your quest? To seek the Holy Grail.
KEEPER: What is the airspeed velocity of an unladen swallow? According to Google, it's about 24mph.
KEEPER: Right. Off you go.

(cs41-env)$ python bridge.py
KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.
KEEPER: What is your name? Excuse me?!
KEEPER: Auuuuuuuugh!
```

## Extensions
> Extensions on Assignment 0? If you insist.

This section of an assignment handout usually gives a few of our suggestions if you're looking for ways to go above and beyond the requirements of the assignment. At no point are you ever required to implement an extension - although they sometimes provide interesting challenges or alternative approaches to problem-solving.

In general, when you submit an extension to an assignment, add `-ext` to the end of the filename. In this case, if you want to submit an extension, you should submit both an unmodified `coconuts.py` file that implements the unextended assignment and a `coconuts-ext.py` file that implements your extension. Extension programs should also contain a module-level comment explaining what the extended assignment does differently.

### Binge-Watch Monty Python Videos on Youtube
Including but not limited to:

- [The Dead Parrot](https://www.youtube.com/watch?v=4vuW6tQ0218)
- [The Argument Clinic](https://www.youtube.com/watch?v=XNkjDuSVXiE)

or [the Monty Python channel](https://www.youtube.com/user/MontyPython/videos?sort=p&flow=grid&view=0)

Include in your submission a file called `review.txt` with your thoughts on whichever videos you've watched!

You can tell your friends and family that it's "for class."

### `coconuts`: Multiple questions
Allow the user to assess the coconut-carrying capacity of birds by putting your question-answering logic in a loop. Continue until the user enters an empty line for either the number of ounces of swallow or the number of pounds of coconut.

### `coconuts`: Advanced coconut-carrying logic
Ask the user to differentiate between a European and African swallow. Penalize (or reward) groups of swallows or individual swallows.

### `cheese`: Cycle through responses
Instead of always using the same prompts and responses, cycle through a list of predetermined responses.

### `cheese`: Fuzzy matching
Allow the user to enter any input, and search for each of your cheeses, case-insensitively, in their input. That is, let the user ask: `"Any Norwegian Jarlsberger, per chance?"`.

### `bridge`: Add more questions and responses to the `answers` file
Create a new file named `answer-ext.txt`, and extend it by adding more lines to the file that ask more questions or offer a different collection of acceptable responses.

### `bridge`: Match regular expressions instead of fuzzy text matching
If you are comfortable with regular expressions, update your code to treat potential responses as regular expressions, and say that user input is successful if it satisfies any of the regular expressions.

## Grading

Your grade for this assignment will be assessed on completion. If you successfully submit a Python program that largely follows the specification above, you will receive full credit on this assignment. We will not be very strict on edge cases, although we encourage you to attempt to match the above specification exactly.

We will not be grading your style on this assignment, since we haven't yet talked about what good Python style looks like in detail. However, we will be leaving feedback on your style, so take a pass through your completed assignment to make its style feel good (to you!) if you haven't already done that.

## Style Checks

While not necessary for this assignment, we want to point out a really useful tool for following the mechanics of Python style. The `pycodestyle` command-line tool (previously called `pep8`) takes as arguments a list of Python files and outputs a list of mechanical style violations. This catches small things like inconsistent spacing, line length, whitespace, but not larger things like program design, idiomatic Python, or structural complexity. You can run `pycodestyle` as follows:

```
(cs41-env)$ pycodestyle coconuts.py cheese.py bridge.py
```

Any style violations will be printed to the console. You can automatically apply all of these changes using the `autopep8` tool. Be warned that the `autopep8` tool overwrites your files in-place, and may substantially change them, so you might want to apply changes by hand. However, `autopep8` can be a good time saver.

```
(cs41-env)$ autopep8 coconuts.py cheese.py bridge.py
```

If you just want to see what changes would be made, but not apply them, you can use `autopep8 --diff coconuts.py cheese.py bridge.py` instead.

We installed both `pycodestyle` and `autopep8` into our virtual environment, so they will be available inside of the virtual environment. That is, make sure that you have activated your `cs41-env` virtual environment in order to run these tools.

## Submitting

Submit the python files you've created; no need to submit `answers.txt`. See the [submission instructions](https://github.com/stanfordpython/python-handouts/blob/master/submitting-assignments.md) on the course website for how to do this. The short version is that we are using [Paperless](https://paperless.stanford.edu) and submission works almost the same as in the CS106 series.

If you've added any extra files or extensions above to the assignment, you should include those in your Paperless submission as well.

## Credit
Credit for the assignment idea and much of this writeup go to Sam Redmond (@sredmond).

> With &#129412; by @parthsarin and @coopermj
