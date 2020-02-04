# Assignment 2: Quest for the &#129412;
**Due Midnight, Friday of Week 7**

## Overview
As you likely recall, in dramatic fashion, the brand new course mascot was stolen during Monday's lecture! The kidnappers have hidden the unicorn at a location on-campus. In this assignment, you will undertake a quest to recover the unicorn.

In this assignment, the first person (or team) to find the unicorn gets **free late night on the staff** and **a perfect score for this assignment**!

* *Expected time: 6 hours*
* *Max time: 8 hours*

Note: It's always a good idea to get started early! We want you to enjoy the beautiful Stanford weather, as a nice break from midterms, and have some fun solving small puzzles.

A few notes before we begin!

1. The unicorn is hidden **in a bush**. You'll likely only get a rough estimation of where the unicorn is, so you'll need to dig around a bit! If you think you're very close and have looked but haven't found the unicorn, you can call Parth.
2. TAKE PICTURES! Take lots of pictures throughout the assignment but, in particular, take pictures once you've found the unicorn / where the unicorn used to be :)
3. You can do this now or at the end, but give us a list of who is on your team by filling out [this form](https://forms.gle/iQrmkX1SSJPSvQDd6).

There are multiple ways to find the unicorn, which are detailed below.

## Paths to the Unicorn
There are several ways to obtain the location of the unicorn, described by the image below:

<p style="align: center; max-width: 100%;">
	<img src="md_img/unicorn_paths.png" style="max-width: 100%" alt="The different paths to the unicorn." />
</p>

Here's a text-based description of the image above, with more information about each piece:

One place to start is the `Pillow` (image) problem. This problem is more like a puzzle hunt than any of the other options, which means that it doesn't have a clear set of instructions to solve the puzzle. You'll have to use clues to figure out how to progress through this problem. The problem involves using the `Pillow` library to manipulate images (you also have to download those images and process them, so `requests` and `numpy` might be useful). *Note: This problem involves traveling around campus. If that poses any difficulties for you, please get in touch with us and we can help. Additionally, if viewing images poses any difficulties for you, let us know and we can help with that as well.* **The assignment spec for this problem is [img.md](img.md)**.

Another option to start out is with the `requests` problem. For this problem, you'll be put in the middle of a maze and you'll have to implement a search algorithm in Python to navigate the maze. The maze is hosted on our website, [https://stanfordpython.com](https://stanfordpython.com). You're only ever given information about the location that you're currently standing at, so you'll have to use `requests` and CS 106B knowledge to explore the entire maze. Periodically, at various points in the maze, you'll obtain information about the location of the unicorn. **The assignment spec for this problem is [requests.md](requests.md)**.

Both `Pillow` and `requests` "feed into" the `numpy` problem, which is the first data science/machine learning style problem of the quarter. To be more precise, once you finish either `Pillow` or `requests`, you should end up with a file called `unicorndata.pickle`. In the `numpy` problem, you'll analyze that data to find the latitude/longitude coordinates of the unicorn. Essentially, we have a bunch of data points with information about the unicorn's distance and we're trying to find a point that minimizes that distance. *Note: This is a mathematically non-trivial problem! It'll take some time to understand how it works. That said, there are detailed instructions on how to implement the assignment that should help you through it and try to explain the mathematics, even if you don't fully understand the math. Of course, we want you to have a productive learning experience, so we're always welcome to help out with this during office hours or on Piazza.* If you're interested in `Pillow` or `requests`, we'd recommend skimming through this assignment spec before you get too far into either of those, since we don't want anybody to get stuck on this portion. **The assignment spec for this problem is [triangulate.md](triangulate.md)**.

An entirely separate path to the unicorn is through the Row of Puzzles. This is designed to be easier, but longer. If you choose this path, you won't be doing as many technically advanced things, but you'll still be using most of the libraries that are used in the other portions of the assignment, namely `requests` and `numpy`, which we've been focusing on in class. In this problem, you'll have to solve some Python puzzle, which will lead you to another one, and to another one, on and on until you get a clue which leads you to the unicorn's location. We won't tell you how many puzzles there are in the Row of Puzzles, but we've designed this to be the slowest path to the unicorn (we expect this will take 6 hours). **The assignment spec for this problem is [row-of-puzzles.md](row-of-puzzles.md)**.

Finally, once you think you know the location of the unicorn, go and find it! The unicorn will have instructions about how to claim your winnings, if you're the first team to reach it. The unicorn is hidden **in a bush outside of a building**. *Note: Again, if this part of the assignment poses difficulties for you, let us know and we can help.*

## Submitting
One person from your team should submit *all of the files you've created or modified* during the course of completing this assignment. First, give us a list of who's in your team and who'll be submitting the assignment on Paperless by filling out [this form](https://forms.gle/iQrmkX1SSJPSvQDd6).

Next, have one person submit the assignment on Paperless. See our [Paperless Submission Instructions](https://github.com/stanfordpython/python-handouts/blob/master/submitting-assignments.md) for more.

## Credit
@psarin wrote `requests`, `triangulate`, and `img`. @coopermj and @antoniof provided invaluable feedback on `requests` and `img`. @psarin and @coopermj wrote `row-of-puzzles`. @theoculhane gave incredible feedback on one of the `row-of-puzzles`.

> With &#129412;s (although hopefully you'll win your own) by @psarin and @coopermj
