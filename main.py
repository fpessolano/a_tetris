"""
 what needs to change:
  - graphics needs to be split into a container class, a score class, a board class and a debug class. Container is the top level while the others are just curse pads
  - the container will manage the pads, the game will manage the the container
  - the container will have a non blocking getch on all pads to avoid game control issues
  - debug one is optional

"""

import tetris

new_gate = tetris.Tetris()

while new_gate.drop_new_shape():
 pass

