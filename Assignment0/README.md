# Assignment 0: Welcome to Python!
> Due: 11:59 PM, Thursday April 8, 2021

## Overview

This introductory assignment aims to give you practice with a few of the Python fundamentals we've covered in class. More importantly, the goal of this warmup assignment is to ensure that your local Python installation is set up correctly and that you are familiar with the CS41 submission process.

- *Expected Time: 2 hours*
- *Max Time: 4 hours*

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

You will create and submit three Python files, named `coconuts.py`, `cheese.py`, and `chatbot.py`, and two text files, named `data.txt` and `sampleruns.txt`.

A reasonable starter `.py` file might look like:

```python
#!/usr/bin/env python3
"""Module-level comment."""

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

### Submission

Please submit a file called `coconuts.py` which contains the code for this segment of the assignment.

## Part 2: The Cheese Shop

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

For anything that is not detailed in the above specification, your program can behave in any way you'd like. For example, you can customize the prompts and messages.

### Hints

You can check that an element is contained in a collection by using the keyword `in`.

### Submission

Please submit a file called `cheese.py` which contains the code for this segment of the assignment.

## Part 3: Creative Chatbot

In the third part of this assignment, you will implement a chatbot program similar to that which was discussed in Lecture 1.2, which uses a `while` loop to repeatedly prompt the user for interactions. This chatbot program will include two rather broad requirements:
1. The program must employ Console I/O. That is, the user must both read from the console (when being prompted for input, or to read output, for example), and write to the console (to provide the chatbot with information, for example) over the course of each run.
2. The program must access data stored in a text file over the course of its run, so that data from previous runs is accessible to users in future runs.

To give you an idea of the scope and complexity of what we expect from this part of the assignment, below are two examples of types of submissions which would fulfill the requirements of this component.

### Example 1: User Authentication

A simple user authentication chatbot might take the role of a gatekeeper. The gatekeeper stops all travellers attempting to pass through the gate, and asks them for their name and passphrase. If the traveller provides a name and passphrase whch are contained in the gatekeeer's Book of Records, the traveller may proceed. If not, the traveller is denied entry.

Upon being asked for a name and passphrase, each traveller has two options: they may (a) provide a valid name and passphrase, or (b) bribe the guard - which allows them to add a new name and passphrase to the Book of Records - for a small fee.

A sample run for such a chatbot might appear as follows:

```
(cs41-env)$ python chatbot.py
Halt! Welcome to the Doors of Destiny. Should you wish to proceed, you must identify yourself within the Book of Records. Is your name present in our book? yes
What is your name, traveller? Michael
What is your passphrase? parthsarin12345
Welcome through, peaceful soul!

(cs41-env)$ python chatbot.py
Halt! Welcome to the Doors of Destiny. Should you wish to proceed, you must identify yourself within the Book of Records. Is your name present in our book? no
Psst! I'm... not supposed to tell you this, but for a small... compensation... I'll be able to add you to the Book of Records without the Warden noticing. Would you like to be added to the Book of Records? yes
Perfect! I've added you - but I don't come cheap! I charge 100 Dogecoin for my services. Can you make the deposit? yes
Deposit successful! You have 5532 Dogecoin remaining in your account.
What is your name, then, traveller? Michael
What is your passphrase? parthsarin12345
Welcome through the Doors of Destiny! And it's been a pleasure doing business with you.

(cs41-env)$ python chatbot.py
Halt! Welcome to the Doors of Destiny. Should you wish to proceed, you must identify yourself within the Book of Records. Is your name present in our book? yes
What is your name, traveller? Michael
What is your passphrase? cs41isacoolclass
The passphrase you presented does not match our records! Guards - arrest this intruder!
```

(Though this chatbot has somewhat more... personality... than most identity systems, this problem is somewhat near and dear to my - Michael's - heart, since I've worked on identity and authentication systems in several capacities for a couple of years now. This type of thinking would be be a great example of what we'd love to see in this part of the assignment - bringing something that you're passionate about, and theming your chatbot of this part around your area of interest).

### Example 2: Simple Schedule

Another example might be a Virtual Assistant chatbot, which allows users to schedule events (in which they would enter a time range, and a name for the event, which would be stored into a text file), and check whether an event was taking place at a given time. A sample run for such a system might appear as follows. (Notes - I've used a MMDDYYYY encoding scheme for dates, and for hours, I've converted hours to floating point numbers, such that 14.5 means 2:30PM).

```
(cs41-env)$ python chatbot.py
Hello there, it's Hal, your friendly scheduling assistant! Would you like to add a new event, or check an existing time slot? add
What is the name of the event? CS41 Lecture
On which day would you like to schedule the event? 03302021
What is the start time? 14.5
What is the end time? 16
Successfully added the event to your day!

(cs41-env)$ python chatbot.py
Hello there, it's Hal, your friendly scheduling assistant! Would you like to add a new event, or check an existing time slot? check
On which day would you like to check for scheduled events? 03302021
What time would you like to check for availability? 15
At that time, you'll be busy with CS41 Lecture.


(cs41-env)$ python chatbot.py
Hello there, it's Hal, your friendly scheduling assistant! Would you like to add a new event, or check an existing time slot? open the pod bay doors
I'm sorry Dave, I'm afraid I can't let you do that.
```

Note that with both of these examples, we've left the scheme you use to store data to the file open-ended. For example, if designing an authentication system as in the first example, you might choose to create a text file with the following data format:

```
dogecoin_in_account:5632

coopermj
parthsarin12345

psarin
pythoniscool!!

antonioferriss
cs41isafunclass
```

If you're designing a scheduling system as in the second example, you may choose to create a text file with the following data format:
```
event_name:CS41 Lecture
date: 03302021
start_time: 14.5
end_time: 16

event_name:Workout
date: 04012021
start_time: 10
end_time: 11
```

The format in which you choose to store your data is up to you, and will likely be (at least in part) informed by the theme around which you'd like to design your chatbot. If you're having trouble working out a data format, though, feel free to reach out, and we're more than happy to help brainstorm with you.

We've deliberately left this problem open-ended, since we're excited to see where you choose to take this prompt.

_We'd ask that, in the spirit of open-endedness, that you please not implement one of the two examples above, but rather that you bring your own take on this assignment to this submission - if you're really struggling for ideas, though, please reach out to us!_

### Submission

Please submit a file called `chatbot.py` which contains the code for this segment of the assignment. Please also submit the following two text files. 
- `sampleruns.txt` should contain - similar to what we've shown in the examples above - input and output from a couple of sample runs, copied and pasted from your Terminal. This will give us an idea of how to interact with your program while grading it. 
- `data.txt` will contain some starter data for your program, so that the user does not need to construct a data file and add data before querying for existing data (e.g. in the authentication example, a user should be able to attempt to login immediately, without first needing to create a file of credentials and populate it with a series of usernames and passwords).

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

This assignment will not be assigned a numeric grade. However, we will be leaving detailed feedback on your functionality and style, so take a pass through your completed assignment to make its style feel good (to you!) if you haven't already done that.

Even though we haven't discussed style too much in class so far, 

## Style Checks

While not necessary for this assignment, we want to point out a really useful tool for following the mechanics of Python style. The `pycodestyle` command-line tool takes as arguments a list of Python files and outputs a list of mechanical style violations. This catches small things like inconsistent spacing, line length, whitespace, but not larger things like program design, idiomatic Python, or structural complexity. 

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

> With &#129412; by @parthsarin and @coopermj
