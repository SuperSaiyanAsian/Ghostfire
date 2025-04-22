# Ghostfire

**Ghostfire** is a fun, open‑source arcade game built with [Pygame](https://www.pygame.org/).  
In this game, you control a stationary gun located at the bottom of the screen. Your goal is to shoot red ghosts while avoiding blue ghosts.  
The game features cool background music, sound effects for firing, and certain sounds upon victory or defeat.

## Features

- **Interactive Gameplay:**  
  Control a gun that automatically aims toward your mouse pointer, and click to fire bullets.
- **Audio Effects:**  
  Enjoy continuous background music with sound effects whenever you fire the gun. A different sound will be played depending on whether you win or lose.

- **Custom Graphics:**  
  The ghosts are drawn programmatically using Pygame drawing functions—no external images used.

- **State-Based Music:**  
  The game will stop background music and switch to dedicated victory or defeat tracks based on the outcome.

## Installation

### Requirements

- **Python 3.x**
- **Pygame (version 2.x is recommended)**
- Additional standard libraries: `sys`, `random`, `math` (which are included with Python)

### Steps (Non-Technical Method)

1. **Clone the Repository**

- Click on the green code button towards the top of the page
- Click on Download ZIP

2. **Extract the Downloaded ZIP File**

3. **Run the Game**

- Run the Ghostfire.exe executable

### Steps (Technical Method)

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Ghostfire.git
   cd Ghostfire
   ```

2. **Install Dependencies**

   ```bash
   pip install pygame
   ```

3. **Run the Game**

   ```bash
   py -u .\Ghostfire.py
   ```
