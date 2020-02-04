# Path (b): Image Manipulation
This path is more like a puzzle hunt than the others. The clues are going to be a little more vague.

First you need to download 150 images from our website. The images are hosted at the urls [https://stanfordpython.com/img/0.png](https://stanfordpython.com/img/0.png) through [https://stanfordpython.com/img/149.png](https://stanfordpython.com/img/0.png). For example, [https://stanfordpython.com/img/29.png](https://stanfordpython.com/img/29.png) hosts the thirtieth image:

<p style="align: center; max-width: 100%;">
	<img src="https://stanfordpython.com/img/29.png" style="max-width: 100%" alt="The thirtieth image in the image manipulation puzzle." />
</p>

*Hint*: if you're trying to manually download each of the images, rethink your strategy.

The data you just downloaded contain almost all of the information needed to solve this problem. Each of the images, individually, will not help you, but the sum of their information will. I'll just outline **some** useful tips.

* If you want to do **some** image manipulation, `Pillow` is a useful library. Here's the documentation: [https://pillow.readthedocs.io/](https://pillow.readthedocs.io/).
  * Make sure you have `Pillow`, and not `PIL` installed. You install `Pillow` by running `pip install Pillow` at a command line. But, you import it in a script with `import PIL`. (*Note for the curious*: This is because `Pillow` is the fork of `PIL` that is still maintained, while `PIL` is no longer being maintaned).
  * Your development environment should be set up like this automatically if you followed our instructions at the beginning of the quarter.
* **Some**times it's useful to interface between `Pillow` and `numpy` because images are really just arrays of pixels where each pixel has R, G, and B values. That makes them an `m x n x 3` array for an image of dimension `m x n`.
  * `np.asarray(im)` converts an image to a numpy array.
  * `Image.fromarray(a)` converts a numpy array to an image.
  * Beware! `Pillow` images can only come from `numpy` arrays that have data type `uint8`. You can convert any `numpy` array to have that data type with `a.astype(np.uint8)`.
* There are a bunch of ways to convert characters to integers. One of the easiest ways is built into Python: `ord(ch)` returns an integer representing the Unicode code point of that character and `chr(i)` is the inverse. `chr(i)` returns the string representing a character whose Unicode code point is the integer `i`.

## Submitting

Put all of the code you used to solve this assignment into one file called `img.py`. It doesn't really have to be clean, since we expect you'll be doing most of your work in the interactive interpreter, but the code should be runnable. If you need to write different functions, each of which solves a piece of the assignment, please do that.

*Note*: Your code will still be graded on Pythonic style practices, but we'll be more lenient on the parts of Pythonic style that don't apply to code that you're writing in the interactive interpreter.
