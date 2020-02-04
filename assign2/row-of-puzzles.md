# Path (c): Row of Puzzles!

This path consists of an unknown row of clues which lead you to the unicorn. To keep things exciting, we aren't going to tell you how many steps there are along the Row of Clues - this path is of unknown length!

To traverse between clues, you will navigate using a series of JSON files hosted on the course website. To start your quest, navigate to `https://www.stanfordpython.com/row-of-puzzles/start.json`. You should be greeted with a JSON file of the following form:

```
{"next": "at7HKK0hP2isUxHYrCezHKoqKV6S9b.json"}
```
The next JSON in your path will then be located at `https://stanfordpython.com/row-of-puzzles/at7HKK0hP2isUxHYrCezHKoqKV6S9b.json`. Eventually, as you progress in this manner, you will be directed to an HTML file which will contain the first puzzle in the row of puzzles for you to solve.

(Hint - you can try to traverse these links manually, but the puzzles are separated by a lot of JSON files! There is a prime opportunity for you to use the `requests` library to write some code to navigate between puzzles.)

As you solve each puzzle, you will be given the link to a JSON file. This file is the starting JSON file on the path to the subsequent clue. You can traverse to each subsequent clue using the method we outlined above.

For example, the path from `start.json` to the first puzzle clue may look like this:

```
start.json --> 1.json --> 2.json --> puzzle1_clue.html
```

Then, once you solve the first puzzle, the solution will be a JSON filename. Assume for the moment that the solution is `yay.json` (even though that is not the solution to the first puzzle). Then, the path of files to the second puzzle starts at `https://www.stanfordpython.com/row-of-puzzles/yay.json` and may look like this:

```
yay.json --> 3.json --> 4.json --> puzzle2_clue.html
```

And the process would repeat.

On with the quest! Remember to commence at `https://www.stanfordpython.com/row-of-puzzles/start.json`. We wish you the best in your quest! 🦄
