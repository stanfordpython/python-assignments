#!/usr/bin/env python3 -tt
"""
File: knightschool.py
---------------------
Assignment 2: Quest for the Holy Grail
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.

It's Winter quarter of your Senior year, and you have a few more Ws then you'd like.
In order for you to 'Camp Stanford' next quarter, you need to take as many classes as
possible. Lucky for you all classes meet MWF, so you dont have to worry about the
days of the week, just the times of the day. You need to make a schedule that has
no overlapping classes, however you don't need to take into account the time of
getting from one class to another. One last thing - you are fine with classes that
start at 9, but any course that runs later than 6:30 is off the table.

The final key for the next puzzle will be the chronological concatenation of letters
from your final course list.

The list of possible classes will be listed like this:

    course_name start_time end_time letter

For example,

    CS41 13.5 15 a

You'll notice that we use decimals for minutes and military time to avoid confusion.

One way to solve this problem involes a naive brute force approach. Look at all possible
orderings of subsets of classes, and keep the longest one that is valid. However, that approach may
be too slow. Instead, there are ways to filter out classes that you would never take. When done
properly, this will leave few enough classes that a brute force approach will work in reasonable
time.

Notes:

*   Finish the implementation of a class representing a Course. What attributes should
    instances of this class have?

*   You can define a __str__ or __repr__ method for Courses so that they are more
    readable when printed to the console.

*   If two classes occur at the same time, choose the class that comes first in the data file.

*   Would you ever choose CourseY instead of CourseX?
        CourseX 13.5 15 X
        CourseY 13.5 16 Y
"""
import itertools

class Course:
    def __init__(self, *what_other_attributes_go_here):
        """
        What attributes should the class have?
        """
        pass

    def __str__(self):
        return "Course({})".format(self)

def brute_schedule(courses):
    """Determine a final course list, subject to time constraints.

    There are a few clever ways to solve this problem, but this function will
    just implement a brute force approach, and return the final puzzle answer.
    """
    return ''

def fast_schedule(courses):
    """Filters courses subject to time and overlap constraints.

    For every start time, keep the course with the shortest duration that
    appears first in the list of courses, and throw out any courses that
    start earlier than 9 AM or end later than 6:30 PM

    For example, with these three courses:

        CourseA 9 12 A
        CourseB 9 11.5 B
        CourseC 9.5 12 C

    CourseB is strictly better than CourseA, so we remove CourseA from
    consideration, leaving:

        CourseA 9 12 A
        CourseB 9 11.5 B
        CourseC 9.5 12 C

    You should return the final puzzle answer.
    """
    # Filter out strictly dominated courses

    # With the smallest set of courses, return the final key
    return brute_schedule(courses)


if __name__ == '__main__':
    DATA_FILE = 'courses.txt'

    with open(DATA_FILE, 'r') as f:
        course_infos = [line.strip() for line in f]

    courses = [Course(*info.split()) for info in course_infos]

    print(fast_schedule(courses))
