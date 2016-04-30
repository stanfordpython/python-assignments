import itertools
import time

"""
It's Winter quarter of your Senior year and you have a few more Ws then you'd like.
In order for you to 'Camp Stanford' next quarter, you need to take as many classes as 
possible. Lucky for you all classes meet MWF, so you dont have to worry about the 
days of the week, just the times of the day. You need to make a schedule that has 
no overlapping classes, however you dont need to take into account the time of 
getting from one class to another. One last thing, you are fine with classes that 
start at 9, but anything that is later than 6:30 is off the table
The list of possible classes will be listed like this:


Name start_time end_time piece

an example:
CS41 13.5 15 a

you'll notice that we use decimals for minutes and military time to avoid confusion

You probably can't do this problem with a naive brute force approach that will search all 
possibilities, but there are ways to filter out classes that you would never take. If done 
properly this may leave few enough classes that brute force will work.

Hints: 

*   Consider creating a class for a course and reading in the file and creating a list
    of course objects.

*   Write the brute force method first (going through every possible permutations of classes),
    then try making it more efficent.

*   Would you ever choose CS110 instead of CS41?
    CS41 13.5 15 a
    CS110 13.5 16 b
"""

DATA_LOCATION = ""

class Class:
    def __init__(WHAT_ARE_YOU_GOING_TO_PASS_TO_THE_CONSTRUCTOR):
        """
        What fields should the class have?
        """

def brute_schedule(classes):
    """
    Unfortunately this problem is not solvable by a greedy algorithm so we have to 
    either do recursion or something a bit more aggressive. The easiest way to find 
    the best schedule is to try to fit as many classes as possible in every 
    conceivable order and then keep the best one.
    """

def fast_schedule(classes):
    """
    Takes the classes and keeps only one class per start time with the shortest duration
    
    For example, with these three classes: 
    ClassA 9 12
    ClassB 9 11.5
    ClassC 9.5 12

    This will cut out ClassA becuase you would always prefer ClassB, This leaves:
    ClassB 9 11.5
    ClassC 9.5 12

    This *significantly* cuts down the number of permutations

    It also applies the 9am to 6:30pm time constraint
    """
    brute_schedule(classes)


if __name__ == '__main__':
    with open(DATA_LOCATION, 'r') as f:
        lines = f.readlines()

    class_strings = [line[:-1] for line in lines]
    classes = [Class(*class_str.split()) for class_str in class_strings]


    fast_schedule(classes)

