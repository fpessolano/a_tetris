import curses
import graphics
import shapes as sp
import time
import constants as c
import sounds as sounds


class Tetris:
    """
    This is the game core loop (including control and any additional logic).
    """

    def __init__(self, screen, sounds, width=10, height=15):
        self.__frame = graphics.Frame(
            width=width, height=height, screen=screen)
        self.__sounds = sounds
        self.__frame.print_board()
        self.__stdscr, _, self.__board_padding = self.__frame.stdscr()
        self.__width = width
        self.__height = height
        self.__level = 0
        self.__frame_pause = c.LEVEL_SPEED[self.__level]
        self.__score = 0
        self.__line_count = 0
        self.__shape = sp.Shapes(self.__level)
        self.__stdscr.keypad(True)
        self.__stdscr.nodelay(True)

    def drop_new_shape(self):
        x = self.__width // 2
        y = 0
        self.__frame.update_background()
        deleted_rows = self.__frame.remove_filled_lines()
        if deleted_rows:
            self.__sounds.points.play()
        self.__line_count += deleted_rows
        self.__score += (
            40 * deleted_rows
            + 60 * max(0, (deleted_rows - 1))
            + 200 * max(0, (deleted_rows - 2))
            + 900 * max(0, (deleted_rows - 3))
        )
        self.__frame.print_board()
        self.__frame.print_score(self.__score)
        self.__frame.line_count(self.__line_count)
        # BUG: when level goes up the object buffet is reset and the next shape is not what shown
        if (
            self.__level < len(c.LEVEL_THRESHOLD)
            and self.__score > c.LEVEL_THRESHOLD[self.__level]
        ):
            self.__shape.level_up()
            self.__level += 1
            self.__frame_pause = c.LEVEL_SPEED[self.__level]
            # self.__sounds.points.stop()
            self.__sounds.levelup.play()
        self.__frame.print_level(self.__level)
        self.__frame.print_next_shape(self.__shape.next_object())

        while True:
            self.__frame[x, y] = [True, self.__shape.object()]
            end_time = time.time() + self.__frame_pause
            while time.time() < end_time:
                key = self.__stdscr.getch()
                if key == curses.KEY_LEFT and self.__frame.shape_fits(  # type: ignore
                    self.__shape.object(), [x - 1, y]
                ):
                    self.__frame[x, y] = [False, self.__shape.object()]
                    x -= 1
                    self.__frame[x, y] = [True, self.__shape.object()]
                elif key == curses.KEY_RIGHT and self.__frame.shape_fits(  # type: ignore
                    self.__shape.object(), [x + 1, y]
                ):
                    self.__frame[x, y] = [False, self.__shape.object()]
                    x += 1
                    self.__frame[x, y] = [True, self.__shape.object()]
                elif key == curses.KEY_UP:  # type: ignore
                    previous_object = self.__shape.object()
                    if self.__frame.shape_fits(self.__shape.next(), [x, y]):
                        self.__frame[x, y] = [False, previous_object]
                        self.__frame[x, y] = [True, self.__shape.object()]
                    else:
                        self.__shape.prev()
                elif key == curses.KEY_DOWN and self.__frame.shape_fits(  # type: ignore
                    self.__shape.object(), [x, y + 1]
                ):
                    self.__frame[x, y] = [False, self.__shape.object()]
                    y += 1
                    self.__frame[x, y] = [True, self.__shape.object()]
                    self.__sounds.drop.stop()
                    self.__sounds.drop.play()
                elif key == 27:
                    return False
                elif key == 32:
                    self.__frame.pause()
                    while True:
                        key = self.__stdscr.getch()
                        if key == 32:
                            self.__frame.pause(False)
                            break
            if not self.__frame.shape_fits(self.__shape.object(), [x, y + 1]):
                if y == 0:
                    return False
                else:
                    break
            self.__sounds.drop.stop()
            self.__sounds.drop.play()
            self.__frame[x, y] = [False, self.__shape.object()]
            y += 1

        next(self.__shape)
        return True

    def score(self):
        return self.__score, self.__level
