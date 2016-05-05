# Assignment 2: Quest for the Holy Grail!

**Due: 4:59:59 PM, Sat May 7th**

## Overview

Congratulations on a great quarter so far!

You have embarked on a quest to find the famous Holy Grail. Along the way, you will have to write various Python scripts to assist you in your journey. We know you're up to the challenge. Your quest will draw on everything you have learned thus far in the course.

We've actually hidden a Holy Grail somewhere on campus. The first person to find it gets late night, on us =D. Godspeed.

*Note: We want you to enjoy the beautiful Stanford weather, as a nice break from midterms, and have some fun solving small puzzles.*

![Holy Grail](http://parktheatreholland.com/wp-content/uploads/2014/10/banner-python.jpg)

## Logistics

Download the [starter files](https://github.com/stanfordpython/python-assignments/tree/master/assign2) from GitHub and use some of the hints below to solve the puzzles and find the Holy Grail!

## Puzzle Guidelines

The staff has created a suite of challenges that will bring you ever closer to the Holy Grail.

### Graduate from Knight School

Before you can leave on your quest, you must first graduate from Knight School. In order to do that, you'll need to assemble your schedule so that you're enrolled in as many courses as possible. After all, the sooner you graduate, the sooner you can start your journey!


In the case of a tie (i.e. two classes that have the same start and end times), choose the class that comes first in the file.

The correct set of classes in chronological order will provide you with a token that will unlock `dna.zip`, so you can continue in your quest.

### Cross the Moat

**Immediately after unzipping `dna.zip`, you should fill out the form linked in `completed-knightschool.txt` so we know how far along you are.**

Now that you have your schedule for next quarter, you're ready to embark on your quest. Unfortunately, there's a challenge in the way, and you'll need to use your Python skills to advance. Solve the puzzle to yield the password to unlock `grail.zip`. More instructions are available in the `README.md` inside `dna.zip`.

### The Final Piece

**Immediately after unzipping `grail.zip`, you should fill out the form linked in `completed-dna.txt` so we know how far along you are.**

Having completed the previous challenges, you're now almost to the holy grail, the grand prize. Read through the `README.md` in `grail.zip` for detailed instructions, and don't hesitate to ask questions on Piazza if you get stuck.

*Note: this final puzzle requires you to seek the holy grail at a physical spot on campus, so you should not wait until Saturday afternoon to start this piece. The holy grail comes with a link to a Google form, which will let us know that you've found the grail.*

## The Hint Machine

We've included in the starter files a `mystery.pyc` file. This file represents a byte-compiled Python file (compiled using CPython 3.4). If you're stuck, you can attempt to glean a useful hint towards the puzzles by codebreaking the symbols exported by this module.

The `mystery` module represented by the `.pyc` file can be imported into the python interpreter or into your own script. The `mystery` module contains a `hint` function that takes some number and type of parameters. Use the hints given by the python compiler, the function itself, and your own introspection skills to figure out what to pass into this mystery function to obtain your next hint.

For example,

```
$ python3
>>> import mystery
>>> mystery.hint()  # You might pass some arguments into `hint`
# some output here
```

## Starter Files

```
assign2/
├── README.md
├── knightschool
│   ├── courses.txt
│   └── knightschool.py
├── dna.zip
├── grail.zip
└── mystery.pyc
```

In addition to this `README`, you've been given a few other tools to help you on your quest:

* `knightschool/`: Starter code for the first puzzle.
* `dna.zip`: Locked starter code for the second puzzle. You'll need to graduate from knight school before you can unlock this puzzle.
* `grail.zip`: Locked starter code for the third puzzle. An elder knight has given you a locked chest containing vital information about the location of the holy grail. Unfortunately, the knight never gave you the key, so you'll need to find a suitable passkey yourself.
* `mystery.pyc`: A hint-giving, coconut-toting byte-compiled Python module that can help out if you're stuck.

## General Advice

As the Zen of Python states, "now is better than never." Get started early on this assignment!

If you get stuck, post general inquiries on Piazza. If you’re blocked on a particular hint given by the compiled python file, please send us a private note on Piazza!

## Extensions

There aren't very many predefined extensions for this project. If you think of one, let us know!

## Submitting

Submit your final code using the `submit` script on AFS, as with Assignment 1.

```
myth$ /usr/class/cs41/tools/submit
```

## Grading

### Functionality

Your functionality grade is determined purely by your progress in the quest. If you complete all of the challenges, you'll receive a guaranteed check-plus. If you complete only the first two challenges, you'll receive a check. If you complete only the first challenge, you'll receive a check-minus.

Remember, we're using the Google forms linked in every piece of the puzzle to determine how far you've made it in the quest, so make sure to submit the form as soon as you unlock a new level! **If you don't submit the form, we have no way of determining your progress, and thus can't give you credit for completion of that part.**

In particular, you need to find the physical holy grail (using the clues in `grail.zip`) on campus to get full marks. The holy grail will be hidden in a bag somewhere. Good luck!

### Style

Your style grade is comprised of three main components - Pythonic practices, program design, and Python mechanics. "Pythonic practices" refers to your use of the Python tools we've talked about in class, and emphasizes Pythonic thinking. "Program design" refers to general programming style - decomposition, commenting, algorithms. "Python mechanics" refers to naming, spacing, parenthesizing, etc. Basically everything covered in PEP 8.

We know that there are many ways to solve each of the challenges, so spend time thinking about the best approach before beginning.

## Credit

Inspiration for this assignment comes from the fantastic 1975 British masterpiece, [Monty Python and the Holy Grail](https://www.youtube.com/v/F41SSqJx2tU). As always, credit to Sherman Leung (@skleung) for the original handout, and to David Slater (@dsslater) for minor edits. David wrote the class selection problem, and Conner Smith (@csmith95) wrote the DNA puzzle.

> With <3 by @sredmond 
