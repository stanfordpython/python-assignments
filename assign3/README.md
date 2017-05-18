# Assignment 3: Stylize

## Congratulations!

Congratulations on completing Week 6! Midterm season is almost over, and we've basically finished discussing the syntax of the Python language. At this point, you know most of the important stuff about the language itself. Therefore, we'll spend most of the rest of the time in class going over useful builtin- or third-party modules that are omnipresent in the Python ecosystem. However, as far as the language itself goes, you have all become skilled in the art of the Python language.

## Overview

One of the key learning goals of this class is that you learn to recognize and write "good" Python code. To that end, this assignment is all about **Python style**. The starter code contains a complete, working implementation of the below assignment specification. Your task is to rewrite the given solution without changing the functionality.

## Recipe Book Specification

The primary functionality of the Recipe Book is searching for and displaying food recipes based on their ingredients. If you run

```
$ python3 recipes.py
...
>>> 
```
you'll be taken to an interactive command prompt where you will be able to execute various commands to query recipe books. In particular, you'll choose between querying AllRecipes dynamically, or loading a static recipe book from a file and querying that book.

At a high level, you can search for recipes that are related to a given collection of keywords, include a collection of ingredients (favorite foods), and exclude a collection of ingredients (allergens). After searching, the collection of matching recipes will be saved in memory in a recipe book. Then, you can query this collection of matching recipes, asking to order them by preparation time, by number of ingredients, or by number of instructions. A search query takes the form

```
search
keyword1 keyword2 +ingredientToInclude1 +ingredientToInclude2 -ingredientToExclude1 -ingredientToExclude2
```

For example, to search for recipes related to dinner containing chicken, but not containing nuts, you would enter

```
search
```
and then on the next line, enter
```
dinner +chicken -nuts
```

I am personally partial to

```
chocolate +chocolate -kale
```

### Orienting Yourself

Part of the challenge of this assignment is becoming familiar with a poorly architected project. Unfortunately, that happens quite a bit in the wild, so we leave it mostly up to you to explore and engage with this code. We will provide the following overview:

```
└── recipebook
    ├── __init__.py
    ├── console.py
    ├── duration.py
    ├── fetcher.py
    ├── ingredients.py
    ├── recipe.py
    ├── recipes.json
    ├── recipes.py
    └── requirements.txt
```

`console.py` loads a static recipe book, the one contained in `recipes.json`. It doesn't seem to actually do much console interaction. Maybe it could be renamed? Furthermore, `recipes.json` isn't actually in JSON format. Could we fix that?

`duration.py` is a small utility class to convert ISO 8601 durations, for preparation and cooking times, as returned by our web scraper, into a number of minutes.

`fetcher.py` uses the BeautifulSoup4 library to scrape recipe information from AllRecipes.com, and returns `Recipe` objects as defined by `recipe.py`

`ingredients.py` defined an `Ingredient` and `IngredientList` class. How useful are these classes? Could we simplify them? Make them act like other data structures?

`recipe.py` defines the `Recipe` class and the `RecipeBook` class. They currently don't have any interested methods or functions.

`recipes.json` is the JSON file containing a static dump of recipes.

`recipes.py` is the main script that, when executed, will interact with the user.

`requirements.txt` lists the third-party packages required to run this project.

### Installing Required Packages

The Recipe Book, as written, relies on some third-party packages. You should install these into your `cs41` virtual environment, by running

```
$ workon cs41
(cs41) $ pip install -r requirements.txt
```

If you are feeling up to the challenge, you can also create a dedicated virtual environment for this project. In the real world, you would likely have a new virtual environment for each project.

```
$ mkvirtualenv --python=`which python3` recipebook
# terminal output ...
(recipebook) $ pip install -r requirements.txt
```

### Modifying Behavior

You *are* allowed to change the behavior of the Recipe Book if the change will improve the functionality in a reasonable way. This includes, but is not limited to, adding more descriptive error messages, capturing only the errors you'd like to catch, and releasing system resources even in the event of an Exception. In effect, you can modify the behavior such that a user's experience is the same or better than before.

In general, you are free to change the printed user text, as long as the message still conveys the same or better information.

## Alternative Project

As an alternative to the recipe book, you can also tackle a similar project that reinforces similar skills. In particular, you will find poorly written, but functional, Python code in the wild, and rewrite the codebase to adhere to Python style principles, and submit to us both the before- and after- snapshots of the Python repository.

Where can you find Python codebases? There are Python projects that exist for other Stanford courses, [trending open-source projects on GitHub](https://github.com/trending/python), tools you may use in research, or pre-existing side-projects.

There are a few caveats:

- You must obtain the codebase owner's explicit written permission to copy, modify, and distribute the source code before beginning to make changes.
- The code you submit (or data you use) cannot violate any privacy or intellectual property laws.
- We (the course staff) must have the legal right to read and edit the Python codebase.
- You must get a verbal or written affirmation from a course staff member about the scope and pre-existing style problems of the code. Usually, this consists of showing one of us a small snippet of code from the codebase.

This should be an unusual alternate option that only a few students undertake. If you do not currently have a Python codebase in mind while reading this, you should complete the standard assignment.

## Extensions

We propose exactly one extension – Code Golf!

The crux of this assignment lies is recognizing that, by understanding Python mechanics and builtin utilities, you can write code that accomplishes a particular goal. For this assignment as a whole, that particular goal is readable, stylistic Python code. However, it can also be fun to target a different goal with your Python ninja skills.

The challenge of code golf is to rewrite the program using as few characters as possible in the source code. How short can you make the Recipe Book? For this challenge, you can toss style out the window - *in the context of this extension*, we only care about the number of characters you use.

You must maintain all the functionality of the un-golfed assignment.

If you beat our reference golfed solution (i.e. your golfed submission has fewer characters of source code), you automatically get a &check;+/&check;+ on this assignment, since outperforming the course staff demonstrates masterful control of using Python's utilities to a particular end.

If you decide to submit this extension, all of your golfed files must live in a folder named golf/ at the root of the submission direction, whose contents mimic the starter code's files. That is, you should have a `golf/` folder that contains `recipes.py` along with any other necessary python modules and static data files.

## Submitting

Submit your final code using the `submit` script on AFS, as with previous assignments.

```
myth$ /usr/class/cs41/tools/submit
```

## Grading

### Functionality

Your functionality grade is determined purely by adherence to the above specification. The submitted code must behave as well or better than the starter code, and you will receive a &check;+ for functionality.

### Style

Your style grade is comprised of three main components - Pythonic practices, program design, and Python mechanics. 

* **Pythonic practices:** Proper use of the Python tools and ways of thinking introduced in this class - using list comprehensions where appropriate, intelligent utilizing iterables/generators where appropriate, using magic methods, etc.
* **Program design:** General programming style - decomposition, commenting, logic, algorithm design, etc.
* **Python mechanics:** Basically everything covered in PEP8 - naming, spacing, parenthesizing, etc.

## Credit

Shoutout to FictiveKin's [OpenRecipes project](https://github.com/fictivekin/openrecipes), from which we've shamelessly copied recipe information.

> With <3 by @sredmond
