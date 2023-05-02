import random, time
import constants as c

# change using periodically randomly lists to make sure all shapes are used


def weighted_random_choice(dict, weights):
  weighted_list = []
  for key, value in weights.items():
    weighted_list += [key] * value
  random_choice = random.choices(weighted_list)[0]
  return dict[random_choice]


class Shapes:
  # shape, need to check somehow frequency to avoid some blocks appears to often
  def __init__(self, level=0):
    current_time = int(time.time())
    random.seed(current_time)
    self.__level = level
    self.__current_object = weighted_random_choice(c.OBJECTS,
                                                   c.LEVEL_WEIGHTS[level])
    self.__cursor = random.randint(0, len(self.__current_object) - 1)
    self.__next_object = weighted_random_choice(c.OBJECTS,
                                                c.LEVEL_WEIGHTS[level])
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

  def __next__(self):
    self.__current_object = self.__next_object
    self.__cursor = self.__cursor_next_object
    self.__next_object = weighted_random_choice(c.OBJECTS,
                                                c.LEVEL_WEIGHTS[self.__level])
    self.__cursor_next_object = random.randint(0, len(self.__next_object) - 1)

if __name__ == '__main__':
  shapes = Shapes()
  print(shapes.object())
  shapes.level_up()
  print(shapes.object())