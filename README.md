# Rock Paper Scissors Game

A command-line implementation of the classic Rock Paper Scissors game developed using Python.

## Features

* Player vs Computer gameplay
* Randomized computer moves
* Score tracking system
* Persistent score storage
* Leaderboard viewing
* Input validation
* Custom welcome and exit messages using Python decorators

## Technologies Used

* Python
* Object-Oriented Programming
* File Handling
* Exception Handling
* Random Module
* Decorators

## Project Structure

```text
Rock-Paper-Scissors/
│
├── main.py
├── Player_prof.py
└── score.txt
```

## Overview

This application allows players to compete against a computer opponent in a game of Rock Paper Scissors through a command-line interface.

Player scores are stored locally and can be reviewed through a built-in leaderboard system. The project demonstrates object-oriented programming principles through a dedicated player class, file-based score persistence, and the use of decorators to enhance program functionality.

## Key Implementation Details

* Utilized a custom `@greet` decorator to manage welcome and exit messages.
* Implemented a `Player` class for player information and score management.
* Stored player scores in a text file to maintain records across sessions.
* Used Python's `random` module to generate computer moves.

## Getting Started

Run the application using:

```bash
python main.py
```

## Gameplay

* Enter your name to start a new game.
* Choose:

  * R for Rock
  * P for Paper
  * S for Scissors
* Continue playing rounds until you choose to exit.
* View previously recorded scores through the leaderboard menu.
