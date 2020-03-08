# Assignment 3: Final Project!

## The Proposal

*Due: Wednesday, Week 8 (February 26th) at 11:59:59 PM*

<p align="center">
	<img src="proposal.png" style="max-width: 100%" alt="A person dressed in a unicorn head, proposing to another person wearing a unicorn onesie." />
</p>

As discussed in class, the purpose of the project proposal is for the course staff to ensure that the project is well-scoped and incorporates Python in some meaningful way. We can also suggest useful packages for your project. The more detailed your proposal, the more we can assist you by pointing you away from common pitfalls and towards feasible solutions.

Submit a project proposal using [this form](https://forms.gle/nYR7wvhEa6K7m8A79). Or, if you prefer to edit more freely, you can use [`template.md`](template.md) as a starting template for your proposal. See [`sampleproposal.md`](sampleproposal.md) for an example of what we're looking for. Additionally, we've added some ideas to [`ideas.md`](ideas.md) if you're stuck.

In order to submit the proposal, fill out our [Google Form](https://forms.gle/nYR7wvhEa6K7m8A79) with the appropriate content. When we review your proposals, we'll look at the most recently added proposal.

*Note: you can use late days on the project proposal, but hopefully you will complete the proposal on time so that we can get feedback to you sooner.*

## The Project

*Due Dates:*

* *Presentation: Monday, Week 10 (March 9th) at 3pm*
* *Code & Writeup: Wednesday, Week 10 (March 11th) at 11:59:59pm*

Implement the project you have proposed, incorporating our feedback. You are free to begin working on the project before you hear from us.

### Development Strategy and Hints

Have a plan. We're making you submit a project proposal so that you think about potential challenges and your plan to overcome them.

Start small and iterate quickly. Python, unlike many other languages, allows you to rapidly iterate. Consider developing your code in small steps using the interactive interpreter.

Build incrementally and test frequently! This project will likely be the largest Python project you have written so far, so make sure each task works before moving on!

Ask questions aggressively on Piazza. Without the structure of a usual assignment, it can be easy to get stuck for a long time on seemingly trivial tasks. I promise that even the most trivial-seeming tasks can be the most difficult! Hopefully, the course staff will be able to help you get unblocked! We may not know the details of every library and dataset you use, but we can certainly try to help.

### Deliverables

In addition to submitting your code (and everything that goes with it), you must include a `README.md` file as a meaningful writeup of your final project.

This writeup should contain a technical overview of the project and the code therein. In effect, you're writing documentation for your project - if the first thing someone reads about your project is the README, what information does she need to know? We're asking you to also include a technical section in your README to describe the code design, the purpose of various modules, and any requirements (e.g. must run a certain version of Python, or must have a particular operating system, or must have a Postgres database running, or must have a Google account, or anything else).

In addition, we're asking you to write short installation/execution instructions. After we download your code, what steps do we have to perform to get it up and running? For many projects, the answer will just be "run the main python script named `something.py`," but several others will have more complex configuration. If we can't set up your project, we have no way to confirm that your project works, so we hope that your installation instructions are clear, correct, replicable, and concise.

Add a section to your README that flags what portions of the final project you are comfortable with the CS 41 staff publishing on the website. Think of this as a replacement for your in-person presentation. We'd like you to, at least, provide a screenshot to publish. At the same time, we understand if you decide that you don't want us to publish any of the project.

Other general sections of a README usually include, but are not limited to: known bugs, contact information for the maintainer (that's you!), and credits/acknowledgements.

There is no upper or lower limit to the length of the README. We've had successful README's in the past that are as short as a few hundred words, or some much longer, with the longest being around 2000 words. Regardless, the majority of the writeup should focus on the technical overview. You're free to write fewer or more words as you see fit, but remember that we are reading your README to understand what your project does.

In addition, please record a video of your final project in action and include it in the final submission. We'll watch this video to get a sense for what your project does. It can be a fun way to immortalize the work you've done and show us a working demo! You should narrate what we're seeing in the video, describing the features and technical overview that would otherwise be in the README.

Moreover, we want this video to be a conversational, informal way to show off what you've built! Don't worry if the production quality isn't good, or if your roommate walks in on you in the middle, or if you get some weird message notification.

Mechanically, you can [record your screen on a Mac with QuickTime Player](https://support.apple.com/en-us/HT201066#record), or you can just record a video on your phone.

### Starter Code

For this assignment, we are not explicitly providing any code to you.

You are free to use any builtin modules, publicly available code, or any code you find online, as long as you cite it appropriately. Google and StackOverflow are your friends! The chances are high that someone has built a library to help with your project, so make sure to ask us or search before reinventing the wheel!

You may *not* use proprietary code, code which requires a paid license, anything which promotes illegal activity, anything which violates Stanford policies, etc.

## Grading

The project *proposal* grade will be assessed purely on completion. Did you do it? Great! If not - less great. 

Your final project grade will be assessed on both functionality and style.

Functionality will be determined holistically using a combination of difficulty of project and success of execution. Unfortunately, that's as detailed as we can get given the breadth of possible topics. In effect, if you put in your fair share of effort, we'll be reasonable. ☺️

Stylistically, as always, you'll be assessed on three main categories:

* **Pythonic practices:** Proper use of the Python tools and ways of thinking introduced in this class - using list comprehensions where appropriate, intelligent utilizing iterables/generators where appropriate, etc. Show us that you've learned how to think like a Python programmer!
* **Program design:** General programming style - decomposition, commenting, logic, algorithm design, etc.
* **Python mechanics:** Basically everything covered in PEP8 - naming, spacing, parenthesizing, etc.

We hold the final project to a higher standard of style than the assignments, since it's naturally more freeform. Make sure that your code is something that you are proud showing off!

## Submitting

Upload all of the files you want to submit, including a `README` and a short demo video, to [Paperless](https://paperless.stanford.edu).

**WARNING: If you use any third-party libraries, ensure that you have generated a `requirements.txt` file listing your project's dependencies before submitting. You can do this by putting the output of `$ pip freeze` into a file. When exercising your code, we guarantee that we will run `$ pip install -r requirements.txt` to install this list of dependencies.**

If your project is sufficiently convoluted, make sure to add the corresponding clarifying information in your README file.

We highly recommend that you check your submission folder on Paperless after submitting to ensure that all necessary files were copied over successfully.

## Credit
This handout is based on a similar handout written by former CS 41 Course Staff.

> With &#129412;s by @psarin and @coopermj
