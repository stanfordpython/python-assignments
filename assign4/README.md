# Assignment 4: Final Project!

## The Proposal

*Due: Friday, May 20th at 11:59:59 PM*

![The Proposal](https://raw.githubusercontent.com/stanfordpython/python-assignments/master/assign4/proposal.png)

As described in class, the purpose of the project proposal is for the course staff to ensure that the project is well-scoped and incorporates Python in some meaningful way. We can also suggest useful packages for your project. The better your proposal, the more we can assist you by pointing you away from common pitfalls and towards good solutions.

You should use [`template.md`](https://github.com/stanfordpython/python-assignments/blob/master/assign4/template.md) as a starting template for your proposal. You can access the raw markdown [here](https://raw.githubusercontent.com/stanfordpython/python-assignments/master/assign4/template.md) or just copy-paste into a Google Doc. See [`sampleproposal.md`](https://github.com/stanfordpython/python-assignments/blob/master/assign4/sampleproposal.md) for an example of what we’re looking for. Additionally, we've added some ideas to [`ideas.md`](https://github.com/stanfordpython/python-assignments/blob/master/assign4/ideas.md) if you're stuck.

In order to submit the proposal, drop your file into our [Google Drive Folder](https://drive.google.com/open?id=0B-eHIhYpHrGDdHJzclFoem1rR1E). When we review your proposals, we'll look at the most recently added proposal.

*Note: you can use late days on the project proposal, but hopefully you will complete the proposal on time so that we can get feedback to you sooner.*

## The Project

*Due: Sunday, May 29th at 11:59:59 PM*

Implement the project you have proposed, incorporating feedback that we will return to you by Monday, May 23rd at the latest. You are free to begin working on the project before you hear from us.

*Note: you can only use up to one late day on the final project!*

### Development Strategy and Hints

Have a plan. We're making you submit a project proposal so that you think about potential challenges and your plan to overcome them.

Start small and iterate quickly. Python, unlike many other languages, allows you to rapidly iterate. Consider developing your code in small steps using the interactive interpreter.

Build incrementally and test frequently! This project will likely be the largest Python project you have written, so make sure each task works before moving on!

### Deliverables

In addition to your code, you must include a `README.md` file as a meaningful writeup of your final project.

This writeup should contain a technical overview of the project and the code therein. In effect, you're writing documentation for your project - if the first thing someone reads about your project is the README, what information does she need to know? We're asking you to also include a technical section in your README to describe the code design, the purpose of various modules, and any requirements (e.g. must run a certain version of Python, or must have a particular operating system, or must have a Postgres database running, or must have a Google account, or anything else).

In addition, we're asking you to write installation/execution instructions. After we download your code, what steps do we have to perform to get it up and running? For many of you, the answer will just be "run the main python script," but several others will have more complex configuration. If we can't set up your project, we have no way to confirm that your project works correctly, so we hope that your installation instructions are clear, correct, replicable, and concise.

Other general sections of a README usually include, but are not limited to: known bugs, contact information for the maintainer (that's you!), and credits/acknowledgements.

In total, the README should be about 700-1500 words, with a majority of that going to the technical overview. Of course, these words counts are estimates, and you're free to write fewer or more as you see fit.

### Starter Code

For this assignment, we are not explicitly providing any code to you. However, we have been working on an early alpha release of a `stanford` package that makes CS106A/B/X-style functionality (graphics, sound) available in Python 3. The software hasn't been tested much, and is surely buggy, but if you'd like to work with our development libraries, let us know.

You are free to use any builtin modules, publicly available code, or any code you find online, as long as you cite it appropriately. Use Google and StackOverflow a lot! Chances are that someone has built a library to help with your project.

You may *not* use proprietary code, code which requires a paid license, anything which promotes illegal activity, etc.

## Grading

The project *proposal* grade will be assessed purely on completion. Did you do it? Great! If not - less great. 

Your final project grade will be assessed on both functionality and style.

Functionality will be determined holistically using a combination of difficulty of project and success of execution. Unfortunately, that's as detailed as we can get given the breadth of possible topics. In effect, if you put in your fair share of effort, we'll be reasonable. =)

Stylistically, as always, you'll be assessed on three main categories:

* **Pythonic practices:** Proper use of the Python tools and ways of thinking introduced in this class - using list comprehensions where appropriate, intelligent utilizing iterables/generators where appropriate, etc. Show us that you've learned how to think like a Python programmer!
* **Program design:** General programming style - decomposition, commenting, logic, algorithm design, etc.
* **Python mechanics:** Basically everything covered in PEP8 - naming, spacing, parenthesizing, etc.

We hold the final project to a higher standard of style than the assignments, since it's naturally more freeform. Make sure that your code is something that you are proud showing off!

## Submitting

When you have finished your final project, you can submit all your files using the `submit` script as usual:

```
myth$ /usr/class/cs41/tools/submit
```

**WARNING: If you use any third-party libraries, ensure that you have generated a `requirements.txt` file listing your project's dependencies before submitting. You can do this by putting the output of `$ pip freeze` into a file. When exercising your code, we guarantee that we will run `$ pip install -r requirements.txt` to install this list of dependencies.**

If your project is sufficiently convoluted, make sure to add the corresponding clarifying information in your README file.

We highly recommend that you check your submission folder on AFS after submitting to ensure that all necessary files were copied over successfully.

> With <3 by @sredmond 