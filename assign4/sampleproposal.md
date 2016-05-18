# CS41 Sample Project Proposal: Mastermind

> Sam Redmond (sredmond) and Guido van Rossum (bdfl)

## Overview

We want to build a Python-based interface for the game [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)).

## Implementation Strategy

The overarching implementation will involve object-oriented design to compartmentalize the API methods to update and display the state of the board for each turn in Mastermind. The board class will be effectively integrated into a text based interface that users can interact with in a game loop that asks for user input at each turn.

## Tasks

1. Setting up the board’s data model
2. Printing the board
3. Building out the textual interface to interact with the game
4. Randomly create a starting board
5. Logic to define game rules and winning
6. (Stretch) Building functionality for two players (Player A sets the code. Player B solves it) 
7. (Stretch) Implementing a basic graphics UI to display the board instead of printing it, maybe using PyQT
8. (Stretch) Implementing an "evil" mastermind (like "Evil Hangman") that actually changes the final answer of the puzzle to prolong the game based on the moves made so far.

Estimated Timeline
Sam
Sherman
Task 1 (2 hours)
Task 2 (1 hour)
Task 3 (1 hour)
Task 4 (1 hour)
Task 6 (3 hours)
Task 5 (1 hour)


Task 7 (3 hours)
Testing
Run tests on the board.py to throughly explore and assess the API methods exposed by the Board class: 
empty initialization
verifying that the state updates correctly given an user’s color choice
testing edge cases where a single color, multiple colors, or no colors are found in the board’s state
Testing mastermind.py to verify that the game loop is able to check for malformed input, handle the starting and ending of the game.

Demo
We would demo a sample runthrough of the game by setting the code ahead of time and calling on classmates to pick colors 
