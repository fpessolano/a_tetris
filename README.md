# A_TETRIS 

**About:** An ASCII-based Tetris game  
**Author:** F. Pessolano  
**Version:** v.0.6.4  

## Description
This is a Python project initially started to teach Python programming in a fun and engaging way. The game recreates the classic Tetris experience using only ASCII art and the Python `curses` module for terminal-based gameplay.

## Features
- Classic Tetris gameplay with all standard pieces (tetrominoes)
- Progressive difficulty with 8 levels
- Score tracking with bonus points for multiple line clears
- **High score system** with top 8 records and initials entry
- Sound effects and background music
- Next piece preview
- Pause functionality
- **Interactive menu system** with records, controls, and quit options
- Customizable piece frequency weights per level

## Dependencies
Install the required dependencies using:
```bash
pip install -r requirements.txt
```

Required packages:
- `pygame` (for sound effects)
- `windows-curses` (for Windows compatibility)

## Usage
Run the game from the terminal:
```bash
python main.py
```

### Controls
**In-Game:**
- **Left/Right arrows:** Move piece horizontally
- **Down arrow:** Speed up piece drop  
- **Up arrow:** Rotate piece
- **Space:** Pause/unpause game
- **ESC/E:** Quit current game (goes to game over screen)

**Menu Navigation:**
- **P:** Play/Start new game
- **C:** Show controls
- **R:** View high score records
- **Q:** Quit program

## Game Mechanics
- **Scoring:** Points awarded for line clears (single: 40, double: 100, triple: 300, tetris: 1300)
- **Levels:** Automatic progression based on score thresholds
- **Speed:** Game speed increases with each level
- **Pieces:** Weighted random distribution of pieces varies by level
- **High Scores:** Top 8 scores saved with player initials, level, and date
- **Records:** Only scores above 0 qualify for high score table

## Recent Improvements (v.0.6.4)
- ✅ **Added high score system** with top 8 records and player initials
- ✅ **Enhanced menu navigation** with consistent options across all screens
- ✅ **Improved user interface** with records page and better controls display
- ✅ Fixed level-up bug where next piece preview didn't update correctly
- ✅ Improved code organization with constants moved to dedicated file
- ✅ Enhanced error handling for better stability
- ✅ Performance optimizations in random piece generation
- ✅ Removed unsafe `__del__` methods for better memory management
- ✅ Clean codebase with unused imports removed
- ✅ **Quit option available** from any screen without playing

## Technical Details
- **Language:** Python 3.x
- **UI Library:** Built-in `curses` module
- **Audio:** `pygame` for sound effects
- **Architecture:** Object-oriented design with separate modules for game logic, graphics, shapes, and sound

## File Structure
- `main.py` - Entry point and game loop
- `tetris.py` - Core game logic and mechanics  
- `graphics.py` - Terminal display and rendering
- `shapes.py` - Tetris piece definitions and rotations
- `sounds.py` - Audio management
- `constants.py` - Game configuration and constants
- `randict.py` - Weighted random piece selection
- `page.py` - Menu and UI pages
- `records.py` - High score management system
- `high_scores.json` - Persistent storage for high scores (auto-generated)

## Known Issues
- None currently reported

## Contributing
This project serves as an educational example of Python game development. Feel free to fork and enhance!
