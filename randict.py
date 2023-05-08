import random
import time
import math


class RandDict(object):
  """
    This is a class that takes a dictionary and item frequency weights 
    to generate an infinite random list from which items can be popped.
    Every item of the original dictionary is guaranteed to be pop-ed at 
    least once in every k*len(dictionary) tries.
    """

  def __init__(self, d, w, k, tries=50, max_freq=0.3, max_seq=3):
    """
    d: a dictionary of strings
    w: a dictionary of weights for each string
    k: the minimum priodicity of an item to be popped
    tries: maximum number of tries to enforce periodicity, maximum frequency and sequence length
    max_freq: the maximum frequency of an item in its periodicity
    max_seq: the maximum length of a sequence for any item
    """
    self.__od = d
    self.__weights = w
    self.__tries = tries
    self.__k = k
    self.__max_freq = max_freq
    self.__max_seq = max_seq
    self.__frame = []
    self.fill()

  def __repr__(self):
    return f'{str(self.__frame)}'

  def pop(self):
    retval = self.__frame[0]
    if len(set(self.__frame).difference(set(self.__frame[1:]))) > 0:
      self.__frame = self.__frame[1:]
      self.fill(False)
    else:
      self.__frame = self.__frame[1:]

    return retval, self.__od[retval]

  def peek(self):
    return self.__frame[0], self.__od[self.__frame[0]]

  def __frequencies(self):
    freq_dict = {}
    for item in self.__frame:
      if item in freq_dict:
        freq_dict[item] += 1
      else:
        freq_dict[item] = 1
    total = sum(freq_dict.values())
    return {
      key: math.trunc(value * 10 / total) / 10
      for key, value in freq_dict.items()
    }

  def max_sequence(self):
    longest = (1, 0)
    current = (1, 0)
    for i in range(1, len(self.__frame)):
      if self.__frame[i] == self.__frame[i - 1]:
        current = (current[0] + 1, current[1])
      else:
        if current[0] > longest[0]:
          longest = current
        current = (1, i)
    if current[0] > longest[0]:
      longest = current
    return longest

  def fill(self, force_reset=True):
    random.seed(time.time())
    if force_reset:
      current = []
    else:
      current = self.__frame
    l = list(self.__od.keys())
    n_picks = len(l) * self.__k - len(self.__frame)
    for i in range(self.__tries):
      self.__frame = current + [
        random.choices(l, weights=self.__weights)[0] for i in range(n_picks)
      ]
      if set(l).issubset(set(self.__frame)):
        if max(self.__frequencies().values()) <= self.__max_freq:
          if self.max_sequence()[0] <= self.__max_seq:
            break
