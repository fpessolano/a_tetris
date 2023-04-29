OBJECTS = {
  "line": [[[1], [1], [1], [1]], [[1, 1, 1, 1]]],
  "square": [[[1, 1], [1, 1]]],
  "elle": [[[1, 0], [1, 0], [1, 1]], [[1, 1, 1], [1, 0, 0]],
           [[1, 1], [0, 1], [0, 1]], [[0, 0, 1], [1, 1, 1]]],
  "mirrored elle": [[[0, 1], [0, 1], [1, 1]], [[1, 0, 0], [1, 1, 1]],
                    [[1, 1], [1, 0], [1, 0]], [[1, 1, 1], [0, 0, 1]]],
  "half plus": [[[0, 1, 0], [1, 1, 1]], [[1, 0], [1, 1], [1, 0]],
                [[1, 1, 1], [0, 1, 0]], [[0, 1], [1, 1], [0, 1]]],
  "z": [[[1, 1, 0], [0, 1, 1]], [[0, 1], [1, 1], [1, 0]], [[1, 1, 0],
                                                           [0, 1, 1]],
        [[0, 1], [1, 1], [1, 0]]],
  "mirrored z": [[[0, 1, 1], [1, 1, 0]], [[1, 0], [1, 1], [0, 1]],
                 [[0, 1, 1], [1, 1, 0]], [[1, 0], [1, 1], [0, 1]]],
  "cross": [[[0, 1, 0], [1, 1, 1], [0, 1, 0]], [[1, 0, 1], [0, 1, 0],
                                                [1, 0, 1]]],
  "dot": [[[1]]],
  "pento":
  [[[0, 1, 1], [1, 1, 0], [0, 1, 0]], [[0, 1, 0], [0, 1, 1], [0, 1, 1]],
   [[0, 0, 1], [1, 1, 0], [1, 0, 1]], [[1, 1, 0], [0, 1, 1], [0, 1, 0]]]
}

LEVEL_THRESHOLD = [200, 500, 1000]
LEVEL_SPEED = [0.35, 0.3, 0.25]

LEVEL_WEIGHTS = {
  0: {
    "line": 2,
    "square": 2,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 3,
    "z": 1,
    "mirrored z": 1,
    "cross": 0,
    "dot": 3,
    "pento": 0
  },
  1: {
    "line": 2,
    "square": 1,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 2,
    "z": 1,
    "mirrored z": 1,
    "cross": 0,
    "dot": 2,
    "pento": 0
  },
  2: {
    "line": 1,
    "square": 1,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 1,
    "z": 1,
    "mirrored z": 1,
    "cross": 1,
    "dot": 1,
    "pento": 0
  },
  3: {
    "line": 2,
    "square": 1,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 1,
    "z": 1,
    "mirrored z": 1,
    "cross": 2,
    "dot": 1,
    "pento": 1
  }
}

if __name__ == "__main__":
  # testing a better random choice
  import random

  def check_presence(L, A):
    for item in L:
        if item not in A:
            return False
    return True
    
  def pick_with_weights(L, weights):
    n_picks = len(L) * 3
    A = [random.choices(L, weights=weights)[0] for i in range(n_picks)]
  
    while not check_presence(L, A):
        random_index = random.randint(0, len(A) - 1)
        if A[random_index] not in L:
            missing_item = random.choice(L)
            A[random_index] = missing_item
  
    return A

  import time
  random.seed(time.time())

  dictionary = {"apple": 10, "banana": 20, "orange": 30, "kiwi": 40}
  weight_list = [10, 20, 30, 40]
  
  items = pick_with_weights(list(dictionary.keys()), weight_list)
  for i in items:
    print(i)

