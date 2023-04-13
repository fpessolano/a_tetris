import curses
import board
import shapes as sp
import time


class Tetris:

  def __init__(self, width=10, height=20, frame_pause=0.4):
    self.__frame = board.Frame(width, height)
    self.__frame.print()
    self.__stdscr, _, self.__board_padding = self.__frame.stdscr()
    self.__width = width
    self.__height = height
    self.__frame_pause = frame_pause
    self.__stdscr.keypad(True)
    self.__stdscr.nodelay(True)

  def __del__(self):
    del (self.__frame)

  def drop_new_shape(self):
    x = self.__width // 2
    y = 0
    shape = sp.Shapes()
    self.__frame.update_background()
    self.__frame.remove_filled_lines()

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
          exit()
      if not self.__frame.shape_fits(shape.object(), [x, y + 1]):
        break
      self.__frame[x, y] = [False, shape.object()]
      y += 1
