import curses


class Frame:

  def __init__(self, width, height, padding=[15, 3]):
    self.__width = width
    self.__height = height
    self.__paddings = padding
    self.__current = [[0 for i in range(width)] for j in range(height)]
    self.__snapshot = [[0 for i in range(width)] for j in range(height)]
    self.__stdscr = curses.initscr()
    curses.cbreak()
    curses.curs_set(0)
    self.__stdscr.refresh()

  def stdscr(self):
    return self.__stdscr, [self.__width, self.__height], self.__paddings

  def print(self):
    for y in range(self.__height):
      self.__stdscr.move(self.__paddings[1] + y, self.__paddings[0])
      self.__stdscr.addstr('<!')
      for x in range(self.__width):
        if self.__current[y][x] == 1:
          self.__stdscr.addstr('[].')
        else:
          self.__stdscr.addstr('  .')
      self.__stdscr.addstr('!>')
    self.__stdscr.move(self.__paddings[1] + self.__height,
                       self.__paddings[0] + 2)
    self.__stdscr.addstr(''.join(['=' for i in range(3 * self.__width)]))
    self.__stdscr.refresh()

  def __del__(self):
    curses.endwin()

  def __setitem__(self, coords, value):
    if coords[0] >= self.__width or coords[1] >= self.__height or len(
        value) == 0:
      return
    mark, shape = value
    block = "[]" if mark else "  "
    for y, line in enumerate(shape):
      for x, el in enumerate(line):
        if (y + coords[1]) < self.__height and (x + coords[0]) < self.__width:
          self.__current[y + coords[1]][x + coords[0]] = int(el and mark)
          self.__stdscr.move(coords[1] + self.__paddings[1] + y,
                             (coords[0] + x) * 3 + self.__paddings[0] + 2)
          if el:
            self.__stdscr.addstr(block)
    self.__stdscr.refresh()

  def shape_fits(self, shape, coords):
    if coords[0] + len(shape[0]) > self.__width or \
        coords[0] < 0 or coords[1] + len(shape) > self.__height or \
        coords[1] < 0:
      return False
    for y, line in enumerate(shape):
      for x, el in enumerate(line):
        if el and self.__snapshot[coords[1] + y][coords[0] + x]:
          return False
    return True

  def take_snapshot(self):
    self.__snapshot = [[self.__current[j][i] for i in range(self.__width)]
                       for j in range(self.__height)]

  # this seems not to work properly
  def remove_filled_lines(self):
    # refresh = False
    for y in range(self.__height):
      if all(item == 1 for item in self.__current[y]):
        # refresh = True
        for x in range(self.__width):
          self.__current[y][x] = 0
          self.__stdscr.move(self.__paddings[1] + y,
                       self.__paddings[0] + 2 + x*3)
          self.__stdscr.addstr("  .")
      # if refresh:
      #   non_zero_rows = []
      #   for i in range(len(self.__current)-1, -1, -1):
      #     if all(item == 0 for item in self.__current[i]):
      #       removed_row = self.__current.pop(i)
      #     else:
      #       non_zero_rows = [self.__current[i]] + non_zero_rows
      #       self.__current[i] = self.__current[i-1]
      #   self.__current = non_zero_rows + [removed_row]
      #   self.print()