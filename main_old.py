import page
import curses

screen = curses.initscr()

landing_page = page.Static(width=60, height=20, screen=screen)
landing_page.centred_text_atY(5, "Something new and a major bug being fixed",
                              True)
landing_page.centred_text_atY(7, "UNDER MAINTENANCE")
landing_page.add_overlapping_text(0, 14, "Press a key to quit")
landing_page.add_overlapping_text(0, 14, "")
landing_page.draw_border()
landing_page.draw()
_ = landing_page.getch([])
screen.clear()
curses.endwin()
