import curses
import graphics
import shapes as sp
import time
import constants as c


class Tetris:
  # frame_pause needs to accelerate towards the end of the level
  # add splash screen for new level
  # change color whrn approaching the level end
  def __init__(self, width=10, height=20):
    self.__frame = graphics.Frame(width, height)
    self.__frame.print_board()
    self.__stdscr, _, self.__board_padding = self.__frame.stdscr()
    self.__width = width
    self.__height = height
    self.__level = 0
    self.__frame_pause = c.LEVEL_SPEED[self.__level]
    self.__score = 0
    self.__shape = sp.Shapes(self.__level)
    self.__stdscr.keypad(True)
    self.__stdscr.nodelay(True)

  def __del__(self):
    del(self.__frame)

  def drop_new_shape(self):
    x = self.__width // 2
    y = 0
    self.__frame.update_background()
    deleted_rows = self.__frame.remove_filled_lines()
    self.__score += 40 * deleted_rows + 60 * max(
      0, (deleted_rows - 1)) + 200 * max(0, (deleted_rows - 2)) + 900 * max(
        0, (deleted_rows - 3))
    self.__frame.print_board()
    self.__frame.print_score(self.__score)
    if self.__score > c.LEVEL_THRESHOLD[self.__level]:
      self.__shape.level_up()
      self.__level += 1
      self.__frame_pause = c.LEVEL_SPEED[self.__level]
    self.__frame.print_level(self.__level)
    self.__frame.print_next_shape(self.__shape.next_object())

    while True:
      self.__frame[x, y] = [True, self.__shape.object()]
      end_time = time.time() + self.__frame_pause
      while time.time() < end_time:
        key = self.__stdscr.getch()
        if key == curses.KEY_LEFT and self.__frame.shape_fits(
            self.__shape.object(), [x - 1, y]):
          self.__frame[x, y] = [False, self.__shape.object()]
          x -= 1
          self.__frame[x, y] = [True, self.__shape.object()]
        elif key == curses.KEY_RIGHT and self.__frame.shape_fits(
            self.__shape.object(), [x + 1, y]):
          self.__frame[x, y] = [False, self.__shape.object()]
          x += 1
          self.__frame[x, y] = [True, self.__shape.object()]
        elif key == curses.KEY_UP:
          previous_object = self.__shape.object()
          if self.__frame.shape_fits(self.__shape.next(), [x, y]):
            self.__frame[x, y] = [False, previous_object]
            self.__frame[x, y] = [True, self.__shape.object()]
          else:
            self.__shape.prev()
        elif key == curses.KEY_DOWN and self.__frame.shape_fits(
            self.__shape.object(), [x, y + 1]):
          self.__frame[x, y] = [False, self.__shape.object()]
          y += 1
          self.__frame[x, y] = [True, self.__shape.object()]
        elif key == 27:
          del self.__frame
          print("Thanks for playing the pre-beta")
          return False
        elif key == 32:
          self.__frame.pause()
          while True:
            key = self.__stdscr.getch()
            if key == 32:
              self.__frame.pause(False)
              break
      if not self.__frame.shape_fits(self.__shape.object(), [x, y + 1]):
        if y == 0:
          self.game_over()
          return False
        else:
          break
      self.__frame[x, y] = [False, self.__shape.object()]
      y += 1

    next(self.__shape)
    return True

  def game_over(self):
    del(self.__frame)
    print("GAMEOVER! Thanks for playing the pre-beta.")
    print(f'Your score is {self.__score} and your level is {self.__level}')