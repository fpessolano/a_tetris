import curses
import random
import time
import string
import repeat_event as rpe


class TitlePage:

  def __init__(self):
    self.__stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    self.__stdscr.nodelay(True)
    self.__stdscr.clear()

  def __del__(self):
    curses.endwin()

  def __animate_string(self, y, x, message, refresh_time, reveal_time):
    chars = string.ascii_letters + string.digits + string.punctuation
    curses.curs_set(0)
    str_len = len(message)
    reveal_string = "%" * str_len
    reveal_counter = reveal_time
    reveal_index = -1

    while reveal_index < str_len:
      time.sleep(refresh_time)
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
        reveal_counter = reveal_time
      else:
        reveal_counter -= refresh_time

      self.__stdscr.addstr(y, x, rand_str)
      self.__stdscr.refresh()

  def draw(self, change_speed, reveal_time):
    title = "Just another ASCII TETRIS"
    subtitle = "version 0.4.1"
    message_1 = "Press p to play"
    message_2 = "Press c for controls"
    offsets = [15, 7]
    width = len(title) + 2 * offsets[0]
    height = 6 + 2 * offsets[1]
    for x in range(1, height - 1):
      self.__stdscr.addstr(x, 0, "||")
      self.__stdscr.addstr(x, width - 2, "||")
    for y in range(width):
      self.__stdscr.addstr(0, y, "=")
      self.__stdscr.addstr(height - 1, y, "=")
    self.__stdscr.refresh()

    self.__animate_string(offsets[1], offsets[0], title, change_speed,
                          reveal_time)
    self.__animate_string(offsets[1] + 2, offsets[0] + 6, subtitle,
                          change_speed, reveal_time)

    def show_play():
      self.__stdscr.move(offsets[1] + 7, offsets[0] + 2)
      self.__stdscr.clrtoeol()
      self.__stdscr.addstr(offsets[1] + 7, width - 2, "||")
      self.__stdscr.addstr(offsets[1] + 7, offsets[0] + 5, message_1)
      self.__stdscr.refresh()

    def show_instruction():
      self.__stdscr.move(offsets[1] + 7, offsets[0] + 2)
      self.__stdscr.clrtoeol()
      self.__stdscr.addstr(offsets[1] + 7, width - 2, "||")
      self.__stdscr.addstr(offsets[1] + 7, offsets[0] + 3, message_2)
      self.__stdscr.refresh()

    repeating_function = rpe.RepeatingFunction([show_play, show_instruction])
    repeating_function.start()
    while True:
      key_pressed = self.__stdscr.getch()
      if key_pressed == ord("p") or key_pressed == ord("c"):
        repeating_function.stop()
        return key_pressed


if __name__ == "__main__":
  test = TitlePage()
  k = test.draw(.01, .05)
  del (test)
  print(k)
