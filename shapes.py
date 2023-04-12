import random
import constants as c


def weighted_random_choice(dict, weights):
  weighted_list = []
  for key, value in weights.items():
    weighted_list += [key] * value
  random_choice = random.choices(weighted_list)[0]
  return dict[random_choice]


class Shapes:

  def __init__(self):
    # self.__current_object = random.choice(list(OBJECTS.values()))
    self.__current_object = weighted_random_choice(c.OBJECTS, c.WEIGHTS_LEVEL1)
    self.__cursor = random.randint(0, len(self.__current_object) - 1)

  def object(self):
    return self.__current_object[self.__cursor]

  def next(self):
    self.__cursor = (self.__cursor + 1) % len(self.__current_object)
    return self.__current_object[self.__cursor]

  def prev(self):
    self.__cursor = (self.__cursor - 1) % len(self.__current_object)
    return self.__current_object[self.__cursor]
