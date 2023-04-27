import curses
import graphics
import shapes as sp
import time


class Tetris:

  def __init__(self, width=10, height=15, frame_pause=0.4):
    self.__frame = graphics.Frame(width, height)
    self.__frame.print_board()
    self.__stdscr, _, self.__board_padding = self.__frame.stdscr()
    self.__width = width
    self.__height = height
    self.__frame_pause = frame_pause
    self.__level = 0
    self.__score = 0
    self.__shape = sp.Shapes(self.__level)
    self.__stdscr.keypad(True)
    self.__stdscr.nodelay(True)

  def __del__(self):
    del(self.__frame)

  def drop_new_shape(self):
    x = self.__width // 2
    y = 0
    shape = sp.Shapes()
    self.__frame.update_background()
    deleted_rows = self.__frame.remove_filled_lines()
    self.__score += 40 * deleted_rows + 60 * max(
      0, (deleted_rows - 1)) + 200 * max(0, (deleted_rows - 2)) + 900 * max(
        0, (deleted_rows - 3))
    self.__frame.print_board()
    self.__frame.print_score(self.__score)
    self.__frame.print_next_shape(shape.next_object())

    while True:
      self.__frame[x, y] = [True, shape.object()]
      end_time = time.time() + self.__frame_pause
      while time.time() < end_time:
        key = self.__stdscr.getch()
        if key == curses.KEY_LEFT and self.__frame.shape_fits(
            shape.object(), [x - 1, y]):
          self.__frame[x, y] = [False, shape.object()]
          x -= 1
          self.__frame[x, y] = [True, shape.object()]
        elif key == curses.KEY_RIGHT and self.__frame.shape_fits(
            shape.object(), [x + 1, y]):
          self.__frame[x, y] = [False, shape.object()]
          x += 1
          self.__frame[x, y] = [True, shape.object()]
        elif key == curses.KEY_UP:
          previous_object = shape.object()
          if self.__frame.shape_fits(shape.next(), [x, y]):
            self.__frame[x, y] = [False, previous_object]
            self.__frame[x, y] = [True, shape.object()]
          else:
            shape.prev()
        elif key == curses.KEY_DOWN and self.__frame.shape_fits(
            shape.object(), [x, y + 1]):
          self.__frame[x, y] = [False, shape.object()]
          y += 1
          self.__frame[x, y] = [True, shape.object()]
        elif key == 27:
          # this is for debugging
          # test = self.__frame.value()
          del self.__frame
          # import pprint as pp
          # pp.pprint(test)
          print("Thanks for playing the pre-beta")
          return False
      if not self.__frame.shape_fits(shape.object(), [x, y + 1]):
        if y == 0:
          self.game_over()
          return False
        else:
          break
      self.__frame[x, y] = [False, shape.object()]
      y += 1

    next(shape)
    return True

  def game_over(self):
    del(self.__frame)
    print("GAMEOVER! Thanks for playing the pre-beta.")
    print(f'Your score is {self.__score}')