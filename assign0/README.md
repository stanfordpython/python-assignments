# Assignment 0: Welcome to Python!
> Due: 11:59 PM, Friday, April 9, 2021

## Overview

This introductory assignment aims to give you practice with a few of the Python fundamentals we've covered in class. More importantly, the goal of this warmup assignment is to ensure that your local Python installation is set up correctly and that you are familiar with the CS41 submission process.

Note: As this is Assignment 0, please get started early! We want to make sure that there's time to resolve any installation or submission problems.

## Outline

- In Part 1, you will create a file called `coconuts.py` in which you write code to calculate the coconut-carrying capacity of swallows.
- In Part 2, you will create a file called `cheese.py` in which you write code to play the part of a cheese shop owner as they discuss inventory with a client.
- In Part 3, you will design and implement your own chatbot program from a broad specification - we're excited to see what types of chatbots you choose to build!

(If coconuts and cheese shops sound rather random, there is some method to this madness - the first two parts of this assignment are themed, as you will soon see, around Monty Python sketches which inspired the name of the Python Programming Language).

## Installing Python

Follow our instructions for installing Python 3.9.2 and setting up a virtual environment. _It is important that you have Python 3.9.2 installed on your system, as some of the features we will be discussing later in the quarter are unique to this most recent version of Python._

- For macOS users, follow [these instructions](https://github.com/stanfordpython/python-handouts/blob/master/installing-python-macos.md)
- For Linux users, follow [these instructions](https://github.com/stanfordpython/python-handouts/blob/master/installing-python-linux.md)
- For Windows users, follow [these instructions](https://github.com/stanfordpython/python-handouts/blob/master/installing-python-windows.md)

**IMPORTANT: Every time you open a new terminal session, you will need to activate your virtual environment again.**

## Starter Files

There are no starter files for this assignment. 

You will create and submit three Python files, named `coconuts.py`, `cheese.py`, and `chatbot.py`, and some text files which store data for your chatbot.

A reasonable starter file might look like:

```python
#!/usr/bin/env python3
"""
File: <filename>.py
-------------------

What does this file do?
"""

# Write additional code and functions here.

def main():
    # Write the main execution of your program here.
    
if __name__ == '__main__':
    main()
```

## Part 1: Coconut-Carrying Capacities

Before anything else, watch [this three-minute video](https://www.youtube.com/watch?v=zqtS9xyl0f4) on Youtube. The transcript can be found [here](http://www.montypython.net/scripts/HG-cocoscene.php).

We're going to help the guards out and compute whether a collection of swallows can carry a collection of coconuts between them. We know that "a five ounce bird could not carry a one pound coconut," so we will assume that a 5.5 ounce bird can carry a one pound coconut. More specifically, we will assume that every 5.5 ounces of bird can carry one pound of coconut.

Create a file named `coconuts.py` in which we will write our program. In this portion of the assignment, we will ask the user for two numbers: the total ounces of birds that are carrying coconuts, and the total weight in pounds of the coconuts.

Prompt the user for the number of ounces of bird by asking: `"How many ounces of birds are carrying the coconuts? "`. Prompt the user for the number of pounds of coconut by asking: `"How many pounds of coconuts are there? "`. Remember to convert these values to numeric types!

If the total number of ounces of birds divided by the number of pounds of coconuts is at least 5.5 (including the value 5.5), then print `"Yes! Carrying the coconuts is possible."`. Otherwise, print `"No. Carrying the coconuts is impossible."`

You can assume that the user input is formatted correctly.

### Sample Runs

Your program should be able to emulate the following sample runs. *Make sure to activate your virtual environment before executing these lines of code!* User input is ***bolded and italicized***:

<pre><code>(cs41-env)$ python coconuts.py
How many ounces of birds are carrying the coconuts? <b><i>5</i></b>
How many pounds of coconuts are there? <b><i>1</i></b>
No. Carrying the coconuts is impossible.

(cs41-env)$ python coconuts.py
How many ounces of birds are carrying the coconuts? <b><i>6.2</i></b>
How many pounds of coconuts are there? <b><i>1.1</i></b>
Yes! Carrying the coconuts is possible.

(cs41-env)$ python coconuts.py
How many ounces of birds are carrying the coconuts? <b><i>17</i></b>
How many pounds of coconuts are there? <b><i>3</i></b>
Yes! Carrying the coconuts is possible.

(cs41-env)$ python coconuts.py
How many ounces of birds are carrying the coconuts? <b><i>12.5</i></b>
How many pounds of coconuts are there? <b><i>2.5</i></b>
No. Carrying the coconuts is impossible.
</code></pre>

Submit the `coconuts.py` file, which should be the code for this segment of the assignment.

## Part 2: The Cheese Shop

Before anything else, watch [this five-minute video](https://www.youtube.com/watch?v=Hz1JWzyvv8A) (cw: gun violence) on Facebook. The transcript can be found [here](http://www.montypython.net/scripts/cheese.php).

In this part of the assignment, you will play the part of the Michael Palin, the owner of the National Cheese Emporium.

Unlike the owner in the sketch, you *do* have some cheeses, and you will repeatedly ask the user what cheese they would like, and then you will respond whether or not you have that cheese.

Make a list of `cheeses` containing `"Muenster"`, `"Cheddar"`, and `"Red Leicester"`; these are the cheeses you have in your shop.

Begin by printing the string `"Good morning. Welcome to the National Cheese Emporium!"` to the console.

Next, in a loop, we will repeatedly ask the user which cheese they would like to buy. If the user enters the exact name of a cheese that you have, affirm that you have the cheese they asked for in the format `"We have {}, yessir."`. If the user does not enter the exact name of a cheese that you have, say that you don't have that cheese in the form `"I'm afraid we don't have any {}."` and then reprompt the user to ask for another cheese.

The user is also allowed to enter special questions. If the user enters either of the strings `"You... do have some cheese, don't you?"` or `"Have you in fact got any cheese here at all?"`, you must reply by listing the number of cheeses that you have in the format `"We have {} cheese(s)!"`, along with the name of each type of cheese you have, one on each line.

### Sample Usage

Your program should be able to emulate the following sample runs. *Make sure to activate your virtual environment before executing these lines of code!*

<pre><code>(cs41-env)$ python cheese.py
Good morning. Welcome to the National Cheese Emporium!
What would you like? <b><i>Red Windsor</i></b>
I'm afraid we don't have any Red Windsor.
What would you like? <b><i>Lancashire</i></b>
I'm afraid we don't have any Lancashire.
What would you like? <b><i>cheddar</i></b>
I'm afraid we don't have any cheddar.
What would you like? <b><i>Cheddar</i></b>
We have Cheddar, yessir.

(cs41-env)$ python cheese.py
Good morning. Welcome to the National Cheese Emporium!
What would you like? <b><i>Red Windsor</i></b>
I'm afraid we don't have any Red Windsor.
What would you like? <b><i>cHeDdAr</i></b>
I'm afraid we don't have any cHeDdAr.
What would you like? <b><i>Have you in fact got any cheese here at all?</i></b>
We have 3 cheese(s)!
Muenster
Cheddar
Red Leicester
What would you like? <b><i>exit</i></b>
I'm afraid we don't have any exit.
What would you like? <b><i>LET ME OUT</i></b>
I'm afraid we don't have any LET ME OUT.
What would you like? <b><i>Cheddar</i></b>
We have Cheddar, yessir.
</code></pre>

For anything that is not detailed in the above specification, your program can behave in any way you'd like. For example, you can customize the prompts and messages.

### Hints

You can check that an element is contained in a collection by using the keyword `in`.

### Submission

Please submit a file called `cheese.py` which contains the code for this segment of the assignment.

## Part 3: Chatbot

In the third part of this assignment, you will implement a chatbot program which has a conversation with the user. There are just two requirements for this program:

1. *Ask the user for input and print out responses*. The program should read input from the console and, based on the input, print out some response. You don't have to respond immediately after every input; the program could keep asking questions, just as long as it responds eventually.
2. *Access stored data*. The program should access data stored in a text file over the course of its run, so that data from previous runs is accessible to users in future runs.

Beyond this, make it your own! Here are two examples that your course staff made previously:

### Example 1: The Doors of Destiny

This program is a simple user authentication chatbot who acts like a gatekeeper before the "Doors of Destiny". The gatekeeper stops all travellers attempting to pass through the gate, and asks them for their name and passphrase. If the traveller provides a name and passphrase whch are contained in the gatekeeer's Book of Records, the traveller may proceed. If not, the traveller is denied entry.

Upon being asked for a name and passphrase, each traveller has two options: they may (a) provide a valid name and passphrase, or (b) bribe the guard - which allows them to add a new name and passphrase to the Book of Records - for a small fee.

Here's what the chatbot looks like (user input is ***bolded and italicized***):

<pre><code>(cs41-env)$ python chatbot.py
Halt! Welcome to the Doors of Destiny. 
Should you wish to proceed, you must identify yourself within the Book of Records. 

Is your name present in our book? <b><i>yes</i></b>
What is your name, traveller? <b><i>Michael</i></b>
What is your passphrase? <b><i>parthsarin12345</i></b>
Welcome through, peaceful soul!

Halt! Welcome to the Doors of Destiny. 
Should you wish to proceed, you must identify yourself within the Book of Records. 

Is your name present in our book? no
Psst! I'm... not supposed to tell you this, but for a small... compensation... I might be able to add you to the Book of Records without the Warden noticing. 

Would you like to be added to the Book of Records? <b><i>yes</i></b>
Perfect! I've added you - but I don't come cheap! I charge 100 coins for my services. 
Can you make the deposit? <b><i>yes</i></b>
Deposit successful! (You have 5532 coins remaining in your account).

What is your name, then, traveller? <b><i>Michael</i></b>
What is your passphrase? <b><i>parthsarin12345</i></b>
Welcome through the Doors of Destiny! And it's been a pleasure doing business with you.

Halt! Welcome to the Doors of Destiny. 
Should you wish to proceed, you must identify yourself within the Book of Records. 

Is your name present in our book? <b><i>yes</i></b>
What is your name, traveller? <b><i>Michael</i></b>
What is your passphrase? <b><i>cs41isacoolclass</i></b>
The passphrase you presented does not match our records! Guards - arrest this intruder!
</code></pre>

### Example 2: Simple Schedule

This program is more like a virtual assistant (think Siri, Alexa, etc.), which allows users to schedule events and see their calendar. Here's a sample run for this program (note that this uses `MMDDYYYY` as an encoding scheme for dates, and that hours are represented as floating point numbers, so 14.5 means 2:30PM); once again, user input is ***bolded and italicized***:

<pre><code>(cs41-env)$ python chatbot.py
Hello there, it's Hal, your friendly scheduling assistant! 

Would you like to add a new event, or check an existing time slot? <b><i>add</i></b>
What is the name of the event? <b><i>CS41 Lecture</i></b>
On which day would you like to schedule the event? <b><i>03302021</i></b>
What is the start time? <b><i>14.5</i></b>
What is the end time? <b><i>16</i></b>

Successfully added the event to your day!

Would you like to add a new event, or check an existing time slot? <b><i>check</i></b>
On which day would you like to check for scheduled events? <b><i>03302021</i></b>
What time would you like to check for availability? <b><i>15</i></b>
At that time, you'll be busy with CS41 Lecture.

Would you like to add a new event, or check an existing time slot? <b><i>open the pod bay doors</i></b>
I'm sorry Dave, I'm afraid I can't let you do that.
</code></pre>

These chatbots are adorable and geeky! Feel free to bring your personality and passions to this part of the assignment. 😊

### File I/O and Data Formatting
Note that with both of these examples, we've left the scheme you use to store data to the file open-ended. For example, the authentication system might have two files - `coins.txt` to keep track of the coin balance, and `data.txt` to track names and passphrases - that look like this:

```
5632
```

```
Michael:parthsarin12345
Parth:pythoniscool!!
Antonio:cs41isafunclass
```

The scheduling system in the second example might have a single data file that looks like this:

```
event_name: CS41 Lecture
date: 03302021
start_time: 14.5
end_time: 16

event_name: Workout
date: 04012021
start_time: 10
end_time: 11
```

The format for your data is up to you, and will likely be informed by the theme around which you'd like to design your chatbot. If you're having trouble working out a data format, though, feel free to reach out, and we're more than happy to help brainstorm with you.

### Submission

Please submit a file called `chatbot.py` which contains the code for this segment of the assignment. Please also submit the following text files.

- `sampleruns.txt` should contain input and output from a couple of sample runs, copied and pasted from your Terminal (similar to what we've included above). This way we know how to interact with your program
- Any data files for your program (there should be at least one). Include some nontrivial data in the file so we don't have to add data before we use the program (e.g. in the authentication example, we should be able to attempt to login immediately, without first needing to create a file of credentials and populate it with a series of usernames and passwords).

## Extensions
> Extensions on Assignment 0? If you insist.

This section of an assignment handout usually gives a few of our suggestions if you're looking for ways to go above and beyond the requirements of the assignment. At no point are you ever required to implement an extension - although they sometimes provide interesting challenges or alternative approaches to problem-solving.

When you submit an extension to an assignment, you should submit *both* an unmodified `coconuts.py` file that implements the unextended assignment and a `coconuts-ext.py` file that implements your extension. Extension programs should also contain a module-level comment explaining what the extended assignment does differently.

### Binge-Watch Monty Python Videos on Youtube
Including but not limited to:

- [The Dead Parrot](https://www.youtube.com/watch?v=4vuW6tQ0218)
- [The Argument Clinic](https://www.youtube.com/watch?v=XNkjDuSVXiE)

or [the Monty Python channel](https://www.youtube.com/user/MontyPython/videos?sort=p&flow=grid&view=0)

Include in your submission a file called `review.txt` with your thoughts on whichever videos you've watched!

You can tell your friends and family, "it's for class."

### `coconuts`: Multiple questions
Allow the user to assess the coconut-carrying capacity of birds by putting your question-answering logic in a loop. Continue until the user enters an empty line for either the number of ounces of swallow or the number of pounds of coconut.

### `coconuts`: Advanced coconut-carrying logic
Ask the user to differentiate between a European and African swallow. Penalize (or reward) groups of swallows or individual swallows.

### `cheese`: Assignment Expressions
If you're feeling especially fancy, [you can use assignment expressions](https://www.python.org/dev/peps/pep-0572/) (a nifty new feature in Python 3.8) to assign a value to a variable in a loop condition.

### `cheese`: Cycle through responses
Instead of always using the same prompts and responses, cycle through a list of predetermined responses.

### `cheese`: Fuzzy matching
Allow the user to enter any input, and search for each of your cheeses, case-insensitively, in their input. That is, let the user ask: `"Any Norwegian Jarlsberger, per chance?"`.

### `chatbot`: Go Nuts!
As you are likely well aware, building effective chatbots which can fluently converse with - and understand - humans is an open area of research in computer science. Though we've designed this assignment so that you implement a simple chatbot within a well-scoped set of requirements, there truly is no ceiling to where you can take this. As two starter ideas, though, we'd recommend adding new features to your chatbot within the theme you've defined, and seeing whether you can make your chatbot robust to imperfect input (in the calendar chatbot, for example, whether the user types `add` or `add event`, the outcome should be the same - how robust can you make your chatbot to such variability in user input?).

## Grading

This assignment will just be submitted for feedback, not a grade!

## Style Checks

While not necessary for this assignment, we want to point out a useful tool for following the mechanics of Python style. The `pycodestyle` command-line tool takes as arguments a list of Python files and outputs a list of mechanical style violations. This catches small things like inconsistent spacing, line length, whitespace, but not larger things like program design, idiomatic Python, or structural complexity. *Nobody writes error-free code! `pycodestyle` is there to help your code comply with the (somewhat arbitrary) rules that the Python community has decided on.*

You can run `pycodestyle` as follows:

```
(cs41-env)$ pycodestyle coconuts.py cheese.py chatbot.py
```

Any style violations will be printed to the console. You can automatically apply all of these changes using the `autopep8` tool. Be warned that the `autopep8` tool overwrites your files in-place, and may substantially change them, so you might want to apply changes by hand. However, `autopep8` can be a good time saver.

```
(cs41-env)$ autopep8 coconuts.py cheese.py chatbot.py
```

If you just want to see what changes would be made, but not apply them, you can use `autopep8 --diff coconuts.py cheese.py chatbot.py` instead.

During setup, we installed both `pycodestyle` and `autopep8` into our virtual environment, so they will be available inside of the virtual environment. That is, make sure that you have activated your `cs41-env` virtual environment in order to run these tools.

## Submitting

Submit the python files you've created to [Paperless](https://paperless.stanford.edu).

If you've added any extra files or extensions above to the assignment, you should include those in your Paperless submission as well.

## Credit
Credit for the assignment idea and much of this writeup go to Sam Redmond (@sredmond).

> With love, 🦄s, and 🐘s by @psarin and @coopermj
