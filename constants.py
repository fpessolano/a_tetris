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
LEVEL_SPEED = [0.6, 0.4, 0.4, 0.2] # delayes below 0.4 seesm to create a problem ...

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
  level = 0
  a = [LEVEL_WEIGHTS[level][x] for x in list(OBJECTS.keys())]
  print(a)