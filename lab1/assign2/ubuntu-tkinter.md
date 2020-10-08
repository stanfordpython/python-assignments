# Tkinter Display Issue
Some users have been running into a display issue on Windows installations running Python through Ubuntu bash. The issue happens because the software in the starter code for `requests` uses Python visualization features but, by default, Ubuntu bash is not configured to recognize that it's connected to a display that supports those features.

In this guide, we'll install software that allows Ubuntu bash to communicate with the Windows operating system and use your computer's built-in display.

## 1. Create a Virtual Display that Mirrors to the Actual Display
We first need to create a way to communicate between Ubuntu bash and the default Windows operating system about the display setup. To create this, install [Xming X Server for Windows](https://sourceforge.net/projects/xming/) and, during the installation, set the display value to 0. This tells the server to host its virtual display mirror on "port" 0.

## 2. Tell Ubuntu Bash to Use the Virtual Display
Once that is set up, we need to tell Ubuntu bash to use the virtual display that we just configured. At a command line run:

```
$ export DISPLAY=:0
```

You'll need to do this every time you open up a terminal prompt, because the export settings get re-set when the terminal closes.

## 3. Configure Permissions on the Display
By default, Ubuntu bash will not allow programs to display things. To change that, we need to change the permissions on the display. Run the following lines of code:

```
$ sudo apt install x11-xserver-utils
$ xhost +
```

After the first command, there will be some installation prompts. After the second, you should see a message that says something like `access control disabled, clients can connect from any host`.

## 4. Run `visualizaton.py`
Now, you should be able to execute:

```
$ python3 visualization.py
```

> With &#129412;s by @psarin and @coopermj
