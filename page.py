import curses
import random
import time
import string
import repeat_event as rpe


class Static:
  """
    This is a class that can be used to build static pages such as
    welcomme and controls pages.
    """
  
  def __init__(self,
               width=60,
               height=20,
               screen=None,
               change_speed=0.01,
               reveal_time=0.05):
    self.__stdscr = screen if screen else curses.initscr()
    self.__delete = False if screen else True
    max_y, max_x = self.__stdscr.getmaxyx()
    self.__width, self.__height = min(width, max_x), min(height, max_y)
    self.__text, self.__animated_text, self.__overlapping_text = [], [], []
    self.__border_char = ["*", "*"]
    self.__border_present = False
    self.__refresh_time, self.__reveal_time = change_speed, reveal_time
    self.__repeating_function = None
    curses.curs_set(0)
    curses.noecho()
    self.__stdscr.nodelay(True)
    self.__stdscr.clear()
    self.__stdscr.refresh()

  def __del__(self):
    self.__stdscr.clear()
    self.__stdscr.refresh()
    if self.__delete:
      curses.endwin()

  def __animate_string(self, y, x, message):
    chars = string.ascii_letters + string.digits + string.punctuation
    curses.curs_set(0)
    str_len = len(message)
    reveal_string = "%" * str_len
    reveal_counter = self.__reveal_time
    reveal_index = -1

    while reveal_index < str_len:
      time.sleep(self.__refresh_time)
      self.__stdscr.addstr(y, x, " " * str_len)
      rand_str = [
        random.choice(chars) if c == "%" else c for c in reveal_string
      ]
      rand_str = "".join(rand_str)

      if reveal_counter <= 0:
        tmp_reveal_list = list(reveal_string)
        tmp_reveal_list[reveal_index] = message[reveal_index]
        reveal_string = "".join(tmp_reveal_list)
        reveal_index += 1
        reveal_counter = self.__reveal_time
      else:
        reveal_counter -= self.__refresh_time

      self.__stdscr.addstr(y, x, rand_str)
      self.__stdscr.refresh()

  def __setitem__(self, coords, value):
    if isinstance(value, list) and len(value) == 2:
      if value[1]:
        self.__animated_text.append([coords[1], coords[0], value[0]])
      else:
        self.__text.append([coords[1], coords[0], value[0]])

  def centred_text_atY(self, y, value, animated=False):
    x = (self.__width - len(value)) // 2
    if animated:
      self.__animated_text.append([y, x, value])
    else:
      self.__text.append([y, x, value])

  def add_overlapping_text(self, x, y, value, centered=True):
    if centered:
      x = (self.__width - len(value)) // 2

    def display_message():
      self.__stdscr.move(y, len(self.__border_char[0]))
      self.__stdscr.clrtoeol()
      if self.__border_present:
        self.__stdscr.addstr(y, self.__width - len(self.__border_char[1]),
                             self.__border_char[1])
      self.__stdscr.addstr(y, x, value)
      self.__stdscr.refresh()

    self.__overlapping_text.append(display_message)

  def set_border(self, symbols):
    if isinstance(symbols, list) and len(symbols) == 2:
      self.__border_char = symbols
    elif isinstance(symbols, list) and len(symbols) == 1:
      self.__border_char = symbols * 2
    elif isinstance(symbols, str):
      self.__border_char = [symbols] * 2

  def draw_border(self):
    self.__border_present = True
    for x in range(1, self.__height - 1):
      self.__stdscr.addstr(x, 0, self.__border_char[1])
      self.__stdscr.addstr(x, self.__width - len(self.__border_char[1]),
                           self.__border_char[1])
    for y in range(self.__width):
      self.__stdscr.addstr(0, y, self.__border_char[0])
      self.__stdscr.addstr(self.__height - 1, y, self.__border_char[0])
      self.__stdscr.refresh()

  def draw(self):
    for _, text in enumerate(self.__animated_text):
      self.__animate_string(*text)
    for _, text in enumerate(self.__text):
      self.__stdscr.addstr(*text)
    if self.__overlapping_text:
      self.__repeating_function = rpe.RepeatingFunction(
        self.__overlapping_text)
      self.__repeating_function.start()

  def getch(self, which_keys=[]):
    while True:
      key_pressed = self.__stdscr.getch()
      if key_pressed in which_keys or (not which_keys and key_pressed != -1):
        if self.__repeating_function:
          self.__repeating_function.stop()
        return key_pressed

  def clear(self, keep_border=True):
    self.__stdscr.clear()
    self.__stdscr.refresh()
    self.__text, self.__animated_text, self.__overlapping_text = [], [], []
    if keep_border:
      self.draw_border()

  def display_records(self, scores, title="HIGH SCORES", show_options=True):
    """Display high scores in a formatted table"""
    self.clear()
    self.draw_border()
    
    # Display title
    self.centred_text_atY(2, title, True)
    
    if not scores:
      self.centred_text_atY(8, "No records yet!")
      self.centred_text_atY(9, "Be the first to set a high score!")
    else:
      # Table headers
      self.centred_text_atY(4, "RANK  INITIALS  SCORE    LEVEL  DATE")
      self.centred_text_atY(5, "=" * 40)
      
      # Display each score
      for i, record in enumerate(scores[:8]):  # Show top 8
        rank = str(i + 1).rjust(2)
        initials = record['initials'].ljust(8)
        score = str(record['score']).rjust(8)
        level = str(record['level']).rjust(5)
        date = record['date']
        
        line = f" {rank}.   {initials} {score}    {level}   {date}"
        self.centred_text_atY(7 + i, line)
    
    # Instructions
    if show_options:
      self.add_overlapping_text(0, 17, "Press p to play")
      self.add_overlapping_text(0, 17, "Press c for controls")
      self.add_overlapping_text(0, 17, "Press q to quit")
    else:
      self.add_overlapping_text(0, 17, "Press any key to continue")
    self.draw()

  def get_player_initials(self, prompt="Enter your initials (3 chars):"):
    """Get player initials for high score entry"""
    self.clear()
    self.draw_border()
    
    self.centred_text_atY(6, "NEW HIGH SCORE!")
    self.centred_text_atY(8, prompt)
    self.centred_text_atY(10, "Type up to 3 letters and press ENTER")
    self.centred_text_atY(11, "Press ENTER alone for blank initials")
    
    # Show input area
    max_y, max_x = self.__stdscr.getmaxyx()
    input_y = max_y // 2 + 1
    input_x = (max_x - 10) // 2
    
    self.centred_text_atY(input_y - 1, "Initials: [___]")
    
    # Draw all the text first
    self.draw()
    
    # Enable cursor and echo for input
    curses.curs_set(1)
    curses.noecho()
    self.__stdscr.nodelay(False)
    
    # Position cursor for input (inside the brackets)
    bracket_x = (max_x - 3) // 2
    self.__stdscr.move(input_y - 1, bracket_x)
    self.__stdscr.refresh()
    
    # Get input (up to 3 characters)
    initials = ""
    while len(initials) < 3:
      try:
        ch = self.__stdscr.getch()
        if ch == 27:  # ESC key
          initials = "AAA"  # Default initials
          break
        elif ch == ord('\n') or ch == ord('\r'):
          # Allow ENTER with any length (including 0 for blank)
          break
        elif ch == curses.KEY_BACKSPACE or ch == 127 or ch == 8:
          if len(initials) > 0:
            initials = initials[:-1]
            # Clear the character and move cursor back
            self.__stdscr.move(input_y - 1, bracket_x + len(initials))
            self.__stdscr.addstr("_")
            self.__stdscr.move(input_y - 1, bracket_x + len(initials))
        elif 32 <= ch <= 126:  # Printable characters
          if len(initials) < 3:
            char = chr(ch).upper()
            # Only allow letters
            if char.isalpha():
              initials += char
              self.__stdscr.addstr(char)
        
        self.__stdscr.refresh()
      except KeyboardInterrupt:
        # Handle Ctrl+C - restore settings and re-raise
        curses.curs_set(0)
        curses.noecho()
        self.__stdscr.nodelay(True)
        raise
      except:
        break
    
    # Restore cursor settings
    curses.curs_set(0)
    curses.noecho()
    self.__stdscr.nodelay(True)
    
    # Handle blank initials or pad to 3 characters
    if len(initials) == 0:
      initials = "   "  # Three spaces for blank
    elif len(initials) < 3:
      initials = initials.ljust(3, ' ')  # Pad with spaces
    
    return initials[:3].upper()
