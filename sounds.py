import pygame
import threading
import os
import time


class Bit8:
    def __init__(self) -> None:
        os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
        pygame.mixer.init()

    def play_music(self):
        def music():
            pygame.mixer.music.load('./assets/tetris.mp3')
            pygame.mixer.music.play(-1)  # Play the music on loop
            while pygame.mixer.music.get_busy():
                continue

        music_thread = threading.Thread(target=music)
        music_thread.start()

    def stop_music(self):
        pygame.mixer.music.stop()

    def move(self):
        pygame.mixer.Sound('./assets/pluck.mp3').play()

    def levelup(self):
        pygame.mixer.Sound('./assets/confirm.mp3').play()

    def gameover(self):
        pygame.mixer.Sound('./assets/gameover.mp3').play()

    def points(self):
        pygame.mixer.Sound('./assets/pickup.mp3').play()
