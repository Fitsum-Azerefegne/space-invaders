🚀 Space Invaders - Python Edition

A classic arcade-style game built with Python's Turtle graphics library.

🎮 How to Play
- Use **Left/Right arrow keys** to move your spaceship
- Press **Spacebar** to shoot lasers
- Destroy all alien invaders before they reach Earth!
- Each alien destroyed gives you 10 points

🕹️ Game Features
- Player spaceship with smooth movement controls
- 5x10 grid of animated alien invaders
- Laser bullet system (fires up to 5 bullets at once)
- Collision detection between bullets and aliens
- Score tracking and display
- Win/lose conditions

🏗️ Technical Implementation
   Core Components:

**Spaceship Class** (`spaceship.py`)
- Handles player movement with keyboard controls
- Manages screen boundary detection
- Turtle-shaped player avatar

**Bullets System** (`bullets.py`)
- Manages bullet creation and movement
- Tracks active bullets (max 5 on screen)
- Handles bullet-alien collision detection

**Invaders System** (`invaders.py`)
- Creates and manages the alien formation
- Handles group movement patterns
- Implements alien animation (shape switching)

🛠️ Running the Game
1. Ensure you have Python 3 installed
2. Clone/download the repository
3. Run from terminal:
```bash
python main.py
```

💡 Requirements
- Python 3.x
- Turtle graphics module (included in standard library)

The game uses object-oriented design principles to keep the code organized and maintainable. All graphics are rendered using Python's built-in Turtle module.



