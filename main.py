import tetris
import page
import curses
import sounds as sounds
import records
import sys

VERSION = "v.0.6.4"


screen = curses.initscr()  # type: ignore
sounds = sounds.Bit8()
high_scores = records.HighScores()

# Title Page
static_page = page.Static(width=60, height=20, screen=screen)
static_page.centred_text_atY(5, "Just another ASCII TETRIS!", True)
static_page.centred_text_atY(7, VERSION)
static_page.add_overlapping_text(0, 14, "Press p to play")
static_page.add_overlapping_text(0, 14, "Press c for controls")
static_page.add_overlapping_text(0, 14, "Press r for records")
static_page.add_overlapping_text(0, 14, "Press q to quit")
static_page.draw_border()
static_page.draw()
option = static_page.getch([ord("p"), ord("c"), ord("r"), ord("q")])

if option == ord("c"):
    # optional controls page
    static_page.clear()
    static_page[12, 5] = ["left arrow\t->\t move left", False]
    static_page[12, 6] = ["right arrow\t->\t move right", False]
    static_page[12, 7] = ["down arrow\t->\t move down", False]
    static_page[12, 8] = ["up arrow\t->\t rotate", False]
    static_page[12, 9] = ["space\t->\t pause game", False]
    static_page[12, 10] = ["esc/e\t \t->\t sudden quit", False]
    static_page.add_overlapping_text(0, 14, "Press p to play")
    static_page.add_overlapping_text(0, 14, "Press r for records")
    static_page.add_overlapping_text(0, 14, "Press q to quit")
    static_page.draw()
    option = static_page.getch([ord("p"), ord("r"), ord("q")])
    
    if option == ord("r"):
        static_page.display_records(high_scores.get_scores())
        static_page.getch([])
    elif option == ord("q"):
        static_page.clear(False)
        curses.endwin()
        sounds.stop_music()
        print("Thanks for playing!")
        exit()
elif option == ord("r"):
    # Show records page
    static_page.display_records(high_scores.get_scores())
    option = static_page.getch([ord("p"), ord("c"), ord("q")])
    if option == ord("c"):
        # Show controls from records
        static_page.clear()
        static_page[12, 5] = ["left arrow\t->\t move left", False]
        static_page[12, 6] = ["right arrow\t->\t move right", False]
        static_page[12, 7] = ["down arrow\t->\t move down", False]
        static_page[12, 8] = ["up arrow\t->\t rotate", False]
        static_page[12, 9] = ["space\t->\t pause game", False]
        static_page[12, 10] = ["esc/e\t \t->\t sudden quit", False]
        static_page.add_overlapping_text(0, 14, "Press p to play")
        static_page.add_overlapping_text(0, 14, "Press r for records")
        static_page.add_overlapping_text(0, 14, "Press q to quit")
        static_page.draw()
        option = static_page.getch([ord("p"), ord("r"), ord("q")])
        
        if option == ord("r"):
            static_page.display_records(high_scores.get_scores())
            static_page.getch([])
        elif option == ord("q"):
            static_page.clear(False)
            curses.endwin()
            sounds.stop_music()
            print("Thanks for playing!")
            exit()
    elif option == ord("q"):
        static_page.clear(False)
        curses.endwin()
        sounds.stop_music()
        print("Thanks for playing!")
        exit()
elif option == ord("q"):
    # Quit immediately
    static_page.clear(False)
    curses.endwin()
    sounds.stop_music()
    print("Thanks for playing!")
    exit()

static_page.clear(False)

sounds.play_music()
while True:
    new_game = tetris.Tetris(screen, sounds)
    while new_game.drop_new_shape():
        pass

    sounds.stop_music()
    sounds.gameover.play()
    screen.clear()
    screen.refresh()
    score, level = new_game.score()

    # Check for high score
    if high_scores.is_high_score(score):
        initials = static_page.get_player_initials()
        position = high_scores.add_score(initials, score, level)
        
        # Show congratulations with position
        static_page.clear(False)
        static_page.draw_border()
        static_page.centred_text_atY(5, "CONGRATULATIONS!")
        static_page.centred_text_atY(7, f"New high score: {score}")
        static_page.centred_text_atY(8, f"Rank #{position}")
        static_page.add_overlapping_text(0, 14, "Press any key to see records")
        static_page.draw()
        static_page.getch([])
        
        # Show updated records
        static_page.display_records(high_scores.get_scores(), show_options=False)
        static_page.getch([])

    static_page.clear(False)
    static_page.centred_text_atY(5, "GAME OVER !!!")
    static_page.centred_text_atY(7, "your score: " + str(score))
    static_page.centred_text_atY(10, "your level: " + str(level))
    static_page.add_overlapping_text(0, 14, "Press p to play")
    static_page.add_overlapping_text(0, 14, "Press q to quit")
    static_page.add_overlapping_text(0, 14, "Press r for records")
    static_page.draw_border()
    static_page.draw()
    option = static_page.getch([ord("p"), ord("q"), ord("r")])
    
    if option == ord("r"):
        # Show records before continuing
        static_page.display_records(high_scores.get_scores())
        option = static_page.getch([ord("p"), ord("c"), ord("q")])
        
        if option == ord("c"):
            # Show controls from records
            static_page.clear()
            static_page[12, 5] = ["left arrow\t->\t move left", False]
            static_page[12, 6] = ["right arrow\t->\t move right", False]
            static_page[12, 7] = ["down arrow\t->\t move down", False]
            static_page[12, 8] = ["up arrow\t->\t rotate", False]
            static_page[12, 9] = ["space\t->\t pause game", False]
            static_page[12, 10] = ["esc/e\t \t->\t sudden quit", False]
            static_page.add_overlapping_text(0, 14, "Press p to play")
            static_page.add_overlapping_text(0, 14, "Press q to quit")
            static_page.draw()
            option = static_page.getch([ord("p"), ord("q")])
        elif option == ord("q"):
            pass  # Will be handled below
    
    static_page.clear(False)
    if option == ord("q"):
        break
    sounds.gameover.stop()
    sounds.play_music()

static_page.clear(False)
curses.endwin()  # type: ignore
sounds.stop_music()
print("Thanks for playing!")
