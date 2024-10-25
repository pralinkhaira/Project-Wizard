# Tetris Game

A classic Tetris game implemented using HTML, CSS, and JavaScript.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Code Structure](#code-structure)
- [Credits](#credits)

## Demo

Check out the live demo <a href="https://codepen.io/TheAkshantSaini/full/PovXajP" target="blank">codepen.io</a>
![image](https://github.com/TheAkshantSaini/Blocks-game/assets/92256182/78481e71-c031-4a20-9f91-9b9797d7ef5f)


## Features

- Classic Tetris gameplay
- Score tracking
- Keyboard controls
- Game over detection
- Responsive design with dark mode

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TheAkshantSaini/Blocks-game.git
2. Navigate to the project directory:
   cd tetris-game

## Usage

Open the index.html file in your web browser.

## Gameplay

- Click the "Play" button to start the game.
- Use the arrow keys to control the falling pieces:
- Left arrow: Move piece left
- Right arrow: Move piece right
- Down arrow: Move piece down faster
- Up arrow: Rotate piece

## Code Structure

- index.html: The main HTML file that sets up the game layout.
- style.css: The CSS file for styling the game.
- index.js: The JavaScript file containing the game logic.
### HTML Structure
- The main container is divided into two parts: the game board (<canvas id="board">) and the sidebar.
- The sidebar contains the game title, score display, and play button.
### CSS Structure
- Dark mode styling is applied to the body and sidebar.
- The game container is centered with a grid layout.
- The game board and sidebar are styled for visibility and readability.
### JavaScript Structure
- Constants for game dimensions, block size, color mapping, and brick layouts.
- Board class for managing the game board, drawing cells, handling rows, and score.
- Brick class for managing individual bricks, their movements, rotations, and collisions.
- Event listeners for starting the game and handling keyboard controls.

## Credits

- Developed by Akshant Saini
- Inspired by the classic Tetris game.
