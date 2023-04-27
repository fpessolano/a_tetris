import tetris
import pyfiglet

ascii_banner = pyfiglet.figlet_format("ASCII Tetris !!")
print(ascii_banner)
print("\t\t\t\t\tVersion 0.3")
print("\t\t\t\t\tby whileTRUEpass\n\n")
_ = input("\t\t\t\t\tPress enter to play...")
print("\033[H\033[J", end="")

new_gate = tetris.Tetris()

while new_gate.drop_new_shape():
  pass
