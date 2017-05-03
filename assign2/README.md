# Assignment 2: Quest for the Holy Grail!

**Due: 11:59:59 PM, Thu May 11th**

## Overview

Congratulations on a great quarter so far!

You have embarked on a quest to find the famous Holy Grail. Along the way, you will have to write various Python scripts to assist you in your journey. We know you're up to the challenge. Your quest will draw on everything you have learned thus far in the course.

We've actually hidden a Holy Grail somewhere on campus. The first person to find it gets late night, on us =D. Godspeed.

*Note: We want you to enjoy the beautiful Stanford weather, as a nice break from midterms, and have some fun solving small puzzles.*

![Holy Grail](http://i.imgur.com/mbHoLDl.png)

## Logistics

Download the [starter files](https://github.com/stanfordpython/python-assignments/tree/master/assign2) from GitHub and use some of the hints below to solve the puzzles and find the Holy Grail!

## Puzzle Guidelines

The course staff has created a suite of challenges that will bring you ever closer to the Holy Grail.

### Knight Training

Your quest will begin with a set of trials to test your readiness. Your skills as a dragon trainer and a swordsperson will be critical in this stage of your journey. You will complete this part of the quest by writing code in the `knight.py` file and then running `python3 quest.py` to test your knight against our challenges. Don't worry - you may attempt the quest as many times as you would like. The quest will provide helpful advice along the way on what you need to do next. If you would like to speed up the advice use the flag `-f`. If you are finished with listening to the elders who run the quest, use the flag `-q`. That is, you can run `python3 quest.py -f` or `python3 quest.py -q`.

#### How to Train Your Dragon

When training your dragon to fly, we expect that you return *changes* in their flight pattern. In the example below, in order to get to x, y, z position (2, 4, 0), our dragon must turn 25.565 degrees clockwise and travel 4.472 forward. Note that when later flying to (4, 8, 0), the dragon's direction is not adjusted (a *change* of 0 degrees in orientation) since it is already oriented in the correct direction and only needs to move 4.472 units. This example omits the z-direction because of the limitation of MS-Paint.

A few notes:

* We define a clockwise rotation as positive. It is possible therefore to have negative angle adjustments, if your dragon is rotating counter-clockwise.
* We define an upward angle of ascent from ground level as positive. If your dragon needs to lower the angle of ascent, you can supply a negative change in angle of ascent.
* We will never have your dragon fly backwards. That is, the distance your dragon travels will always be positive.

A few hints:
* The `math` module has many useful trigonometric functions, including `math.atan2`, `math.acos`, `math.sqrt`, and `math.degrees`.
* Drawing a diagram can help determine which trig functions to use.

![Dragon](http://web.stanford.edu/~dsslater/dragon.png)

#### A Fighting Chance

When fighting against our champion, your "moves" should be returned as a list of integers, where each number refers to your choice of move in a given round. The numbers refer to the different types of moves: do nothing (0), parry (1), attack (2), aggressive attack (3).

As an example, consider a competition of three rounds where our champion's strategy is: attack during round 0, aggressive attack during round 1, and then do nothing during round 2. This strategy would be represented as the list `[2, 3, 0]`. If your knight were to respond with parry, parry, followed by aggressive attack, your strategy would be represented as `[1, 1, 3]`. In this case, you would win the engagement! In the actual quest, your strength is not equal to the champion's strength, and the champion's strategy is not public information.

Once you have trained your dragon and have defeated our champion in a duel, you will be given a riddle to solve out in the real world. You can unlock the next part of the quest by entering the correct answer to the riddle.

### Potion Making

Now that your knight's physical prowess has been proven, we will challenge your knight's mind. Your job is to identify how many potions can be concocted, given a collection of recipes, a pantry of ingredients, and market where you can trade. 

Notes:

* The task is to determine how many recipes could hypothetically be completed. The fact that Potion A *could* be concocted does not affect whether Potion B *could* be concocted. In other words, if you could produce Potion A by itself, Potion B by iteself and Potion C by itself then you would return 3.

Once you have completed the potion making portion, you will receive a secret code, allowing you to unlock the final part of the quest.

### The Final Piece

Having completed the previous challenges, you're now almost to the holy grail, the grand prize. Read through the `README.md` in the unzipped `grail.zip` for detailed instructions, and don't hesitate to ask questions on Piazza if you get stuck.

*Note: this final puzzle requires you to seek the holy grail at a physical spot on campus, so you should not wait until the final day to start this piece. The holy grail comes with a link to a Google form, which will let us know that you've found the grail and to submit a picture of you with it.*


## Starter Files

```
assign2/
├── README.md
├── knight.py
├── quest.py
└── grail.zip
```

In addition to this `README`, you've been given a few other tools to help you on your quest:

* `knight.py`: Starter code for the first two parts of the quest.
* `quest.py`: The script that will put your knight through tests while giving you hints and riddles along the way.
* `grail.zip`: Locked starter code for the third puzzle. An elder knight has given you a locked chest containing vital information about the location of the holy grail. Unfortunately, the knight never gave you the key, so you'll need to find a suitable passkey yourself.

## General Advice

As the Zen of Python states: "Now is better than never." Get started early on this assignment!

If you get stuck, post general inquiries on Piazza. If you’re blocked on a particular hint, please send us a private note on Piazza!

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

You need to find the physical holy grail (using the clues in `grail.zip`) on campus to get full marks. The holy grail will be hidden in a bag somewhere. Good luck!

### Style

Your style grade is comprised of three main components - Pythonic practices, program design, and Python mechanics. "Pythonic practices" refers to your use of the Python tools we've talked about in class, and emphasizes Pythonic thinking. "Program design" refers to general programming style - decomposition, commenting, algorithms. "Python mechanics" refers to naming, spacing, parenthesizing, etc. Basically everything covered in PEP 8.

We know that there are many ways to solve each of the challenges, so spend time thinking about the best approach before beginning.

## Credit

Inspiration for this assignment comes from the fantastic 1975 British masterpiece, [Monty Python and the Holy Grail](https://www.youtube.com/watch?v=F41SSqJx2tU). As always, credit to Sherman Leung (@skleung) for the original handout and idea, and to David Slater (@dsslater) and Gracie Young (@grace-young) for edits and puzzle details. David wrote the dragon-training and knight-fighting, and Gracie wrote the potion-making.

> With <3 by @sredmond, @dsslater, and @grace-young
