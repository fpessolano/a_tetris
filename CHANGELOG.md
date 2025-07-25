# Changelog
All notable changes to this project will be documented in this file.

## [0.7.0] - 2025-07-25
#### Added
- **High Score System**: Comprehensive top 8 high score tracking with player initials, level, and date
- **Records Management**: Persistent JSON-based score storage with automatic sorting
- **Interactive Menu System**: Consistent navigation options (P/C/R/Q) across all screens
- **Records Page**: Dedicated high score display with formatted table
- **Initials Input**: User-friendly interface for entering player initials after achieving high scores
- **Quit Option**: Available from any screen without requiring gameplay
- **Enhanced Controls Display**: Clear separation of in-game and menu navigation controls

#### Fixed
- **Zero Score Prevention**: Scores of 0 or below are no longer recorded in high score table
- **Menu Navigation**: Removed problematic Ctrl+C handling that caused restart issues
- **User Experience**: Improved clarity of initials input with better instructions

#### Changed
- **Game Flow**: Enhanced navigation between game, records, controls, and quit options
- **Documentation**: Updated README.md with comprehensive feature list and controls
- **File Structure**: Added records.py module for high score management
- **UI Consistency**: Standardized option prompts across all screens

## [0.6.4]
#### Fixed 
 - removed some typos

## [0.6.3]
#### Fixed 
 - n/a

#### Changed 
 - unified requirement.txt
 - bug fixed al level up with next shgape being wrong

#### Added
 - Game sounds


## [0.5.2]
#### Fixed 
 - Added curses.refresh in some missing code parts after a curses.clear command

#### Changed 
 - Most test code has been deleted

#### Added
 - More levels
 - More shapes
 - Proper end screen with play again
 - Some code commenting has been added


## [0.4.2]
#### Fixed 
 - Randonmess has been fixed to avoid locking into always the same shape

#### Added
 - Proper title screen
 - Instruction screen


## [0.3.1]
#### Fixed 
 - Bug prevennting shape list and frequencies from beng updated
 - Error in not checking is we are at the last level

#### Changed 
 - Better randomness of shapes
 - Better control of item sequences and frequency

#### Added
 - The cleared lines counter
   