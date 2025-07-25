import random
import constants as c
import randict as rd


class Shapes:
  """
    This is a class that handles all shapes including sequences and rotations
    """
  
  def __init__(self, level=0):
    random.seed()
    self.__level = level
    level_weights = [
      c.LEVEL_WEIGHTS[self.__level][x] for x in list(c.OBJECTS.keys())
    ]
    self.__objects = rd.RandDict(c.OBJECTS, level_weights, 3)
    _, self.__current_object = self.__objects.pop()
    self.__cursor = random.randint(0, len(self.__current_object) - 1)
    _, self.__next_object = self.__objects.peek()
    self.__cursor_next_object = random.randint(0, len(self.__next_object) - 1)

  def object(self):
    return self.__current_object[self.__cursor]

  def next(self):
    self.__cursor = (self.__cursor + 1) % len(self.__current_object)
    return self.__current_object[self.__cursor]

  def prev(self):
    self.__cursor = (self.__cursor - 1) % len(self.__current_object)
    return self.__current_object[self.__cursor]

  def next_object(self):
    return self.__next_object[self.__cursor_next_object]

  def level_up(self):
    if self.__level < len(c.LEVEL_WEIGHTS.keys()) - 1:
      self.__level += 1
      level_weights = [
        c.LEVEL_WEIGHTS[self.__level][x] for x in list(c.OBJECTS.keys())
      ]
      self.__objects = rd.RandDict(c.OBJECTS, level_weights, 3)
      # Keep the current shape, only update next shape from new level
      _, self.__next_object = self.__objects.peek()
      self.__cursor_next_object = random.randint(0,
                                                 len(self.__next_object) - 1)

  def __next__(self):
    _, self.__current_object = self.__objects.pop()
    self.__cursor = self.__cursor_next_object
    _, self.__next_object = self.__objects.peek()
    self.__cursor_next_object = random.randint(0, len(self.__next_object) - 1)


if __name__ == '__main__':
  shapes = Shapes()
  print(shapes.object())
  shapes.level_up()
  print(shapes.object())
  print()
  for _ in range(30):
    next(shapes)
    print(shapes.object())
