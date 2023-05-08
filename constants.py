# All game constants

# Objects defines as 4x4 matrices including all possible rotations
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
  "cross": [[[0, 1, 0], [1, 1, 1], [0, 1, 0]]],
  "dot": [[[1]]],
  "pento":
  [[[0, 1, 1], [1, 1, 0], [0, 1, 0]], [[0, 1, 0], [0, 1, 1], [0, 1, 1]],
   [[0, 0, 1], [1, 1, 0], [1, 0, 1]], [[1, 1, 0], [0, 1, 1], [0, 1, 0]]],
  "x": [[[1, 0, 1], [0, 1, 0], [1, 0, 1]]],
  "triangle": [[[0, 0, 1], [0, 1, 1], [1, 1, 1]],[[1, 0, 0], [1, 1, 0], [1, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 0]],[[1, 1, 1], [0, 1, 1], [0, 0, 1]],
]
}

# Score triggering the next level
LEVEL_THRESHOLD = [100, 200, 500, 750, 1000, 1500, 2000]

# game speed at a given level
LEVEL_SPEED = [0.6, 0.6, 0.6, 0.6, 0.4, 0.4, 0.4, 0.2]  # delayes below 0.4 seesm to create a problem ...

# Levels are defined by giving a weight in the randomness of each shape
LEVEL_WEIGHTS = {
    0: {
    "line": 1,
    "square": 1,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 1,
    "z": 1,
    "mirrored z": 1,
    "cross": 0,
    "dot": 0,
    "pento": 0,
    "x": 0,
    "triangle": 0
  },
  1: {
    "line": 1,
    "square": 1,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 1,
    "z": 1,
    "mirrored z": 1,
    "cross": 0,
    "dot": 1,
    "pento": 0,
    "x": 0,
    "triangle": 0
  },
  2: {
    "line": 1,
    "square": 2,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 3,
    "z": 1,
    "mirrored z": 1,
    "cross": 0,
    "dot": 3,
    "pento": 0,
    "x": 0,
    "triangle": 0
  },
  3: {
    "line": 2,
    "square": 1,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 2,
    "z": 1,
    "mirrored z": 2,
    "cross": 1,
    "dot": 2,
    "pento": 0,
    "x": 0,
    "triangle": 0
  },
  4: {
    "line": 2,
    "square": 2,
    "elle": 1,
    "mirrored elle": 2,
    "half plus": 2,
    "z": 2,
    "mirrored z": 2,
    "cross": 1,
    "dot": 2,
    "pento": 0,
    "x": 0,
    "triangle": 1
  },
  5: {
    "line": 2,
    "square": 2,
    "elle": 1,
    "mirrored elle": 2,
    "half plus": 2,
    "z": 2,
    "mirrored z": 2,
    "cross": 1,
    "dot": 2,
    "pento": 1,
    "x": 0,
    "triangle": 1
  },
  6: {
    "line": 2,
    "square": 2,
    "elle": 1,
    "mirrored elle": 2,
    "half plus": 2,
    "z": 2,
    "mirrored z": 2,
    "cross": 1,
    "dot": 2,
    "pento": 1,
    "x": 1,
    "triangle": 1
  },
  7: {
    "line": 1,
    "square": 1,
    "elle": 1,
    "mirrored elle": 1,
    "half plus": 1,
    "z": 1,
    "mirrored z": 1,
    "cross": 1,
    "dot": 1,
    "pento": 1,
    "x": 1,
    "triangle": 1
  }
}
