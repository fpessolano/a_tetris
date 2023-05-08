import tetris
import page
import curses

VERSION = 'v.0.4.2'

screen = curses.initscr()

# Title Page
title_page = page.Static(width=60, height=20, screen=screen)
title_page.centred_text_atY(5, "Just another ASCII TETRIS!", True)
title_page.centred_text_atY(7, VERSION)
title_page.add_overlapping_text(0, 14, "Press p to play")
title_page.add_overlapping_text(0, 14, "Press c for controls")
title_page.draw_border()
title_page.draw()
option = title_page.getch([ord('p'), ord('c')])

if option == ord('c'):
  # optional controls page
  title_page.clear()
  title_page[12, 5] = ["left arrow\t->\t move left", False]
  title_page[12, 6] = ["right arrow\t->\t move right", False]
  title_page[12, 7] = ["down arrow\t->\t move down", False]
  title_page[12, 8] = ["up arrow\t->\t rotate", False]
  title_page[12, 9] = ["space\t->\t pause game", False]
  title_page[12, 10] = ["esc\t \t->\t sudden quit", False]
  title_page.add_overlapping_text(0, 14, "Press any key to play")
  title_page.add_overlapping_text(0, 14, "")
  title_page.draw()
  title_page.getch([])

title_page.clear(False)
del (title_page)

new_game = tetris.Tetris(screen)
while new_game.drop_new_shape():
  pass

curses.endwin()
score, level = new_game.score()
print("GAMEOVER!\nThanks for playing the game.")
print(f'Your score is {score} and your level is {level}\n')
