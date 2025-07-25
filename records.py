import json
import os
from datetime import datetime
from typing import List, Dict, Any


class HighScores:
    """
    High score management system for the Tetris game.
    Stores top 10 scores with player initials, score, level, and date.
    """
    
    def __init__(self, filename: str = "high_scores.json"):
        self.filename = filename
        self.scores: List[Dict[str, Any]] = []
        self.max_scores = 8
        self.load_scores()
    
    def load_scores(self) -> None:
        """Load high scores from file or create empty list if file doesn't exist"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.scores = data.get('scores', [])
            else:
                self.scores = []
        except (json.JSONDecodeError, IOError):
            # If file is corrupted or can't be read, start fresh
            self.scores = []
    
    def save_scores(self) -> None:
        """Save high scores to file"""
        try:
            data = {
                'scores': self.scores,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError:
            # Silent fail if can't write (permissions, disk full, etc.)
            pass
    
    def is_high_score(self, score: int) -> bool:
        """Check if a score qualifies for the high score list"""
        if score <= 0:
            return False
        if len(self.scores) < self.max_scores:
            return True
        return score > self.scores[-1]['score']
    
    def add_score(self, initials: str, score: int, level: int) -> int:
        """
        Add a new high score and return its position (1-based).
        Returns 0 if score didn't make the list.
        """
        if not self.is_high_score(score):
            return 0
        
        new_entry = {
            'initials': initials[:3] if initials.strip() else "   ",  # Keep spaces for blank initials
            'score': score,
            'level': level,
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        
        # Find insertion position
        position = 0
        for i, entry in enumerate(self.scores):
            if score > entry['score']:
                position = i
                break
        else:
            position = len(self.scores)
        
        # Insert new score
        self.scores.insert(position, new_entry)
        
        # Keep only top scores
        if len(self.scores) > self.max_scores:
            self.scores = self.scores[:self.max_scores]
        
        self.save_scores()
        return position + 1  # Return 1-based position
    
    def get_scores(self) -> List[Dict[str, Any]]:
        """Get all high scores"""
        return self.scores.copy()
    
    def get_top_score(self) -> int:
        """Get the highest score, or 0 if no scores"""
        return self.scores[0]['score'] if self.scores else 0
    
    def clear_scores(self) -> None:
        """Clear all high scores (for testing or reset)"""
        self.scores = []
        self.save_scores()