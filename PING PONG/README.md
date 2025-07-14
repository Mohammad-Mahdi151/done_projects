# Pygame Ping Pong Game

A classic Ping Pong game developed using Pygame, featuring both single-player (vs. AI) and two-player modes.

## Table of Contents

- [Features](#features)
- [Game Modes](#game-modes)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Controls](#controls)
- [Game Rules](#game-rules)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Future Improvements](#future-improvements)

## Features

- **Two Game Modes:** Play against an AI opponent or challenge a friend in two-player mode.
- **Dynamic Ball and Paddle Movement:** Smooth and responsive game physics.
- **Score Tracking:** Keep track of scores for both players/AI.
- **Win Condition:** First player to reach 10 points wins the round.
- **Restart Option:** Easily restart a new game after a round ends.
- **Customizable Speeds:** Paddle and ball speeds can be adjusted (via `constants.py`).
- **Visual Feedback:** Clear visual elements and color scheme.

## Game Modes

Upon starting the game, you will be prompted to choose a game mode:

1.  **Player vs. Opponent (AI):** Play against a computer-controlled opponent.
2.  **Player vs. Another Player:** Play against a second human player on the same keyboard.

## Installation

To run this game, you need Python and Pygame installed.

1.  **Install Python:** If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
2.  **Install Pygame:** Open your terminal or command prompt and run:
    ```bash
    pip install pygame
    ```

## How to Run

1.  **Clone the repository** (if applicable) or ensure all game files are in one directory.
2.  **Navigate to the game directory** in your terminal or command prompt.
3.  **Run the main game file:**
    ```bash
    python "PING PONG.PY"
    ```
4.  Follow the on-screen prompts to select your desired game mode.

## Controls

### Player 1 (Right Paddle)

-   **Move Up:** `Up Arrow` key
-   **Move Down:** `Down Arrow` key

### Player 2 (Left Paddle - in Two-Player Mode)

-   **Move Up:** `W` key
-   **Move Down:** `S` key

### General

-   **Quit Game:** Press `Q` when prompted, or close the game window.

## Game Rules

-   The first player to score 10 points wins the round.
-   A point is scored when the opponent fails to return the ball.
-   The ball's speed increases slightly after each paddle collision.

## Technologies Used

-   **Python 3.x**
-   **Pygame:** A set of Python modules designed for writing video games.

## File Structure

