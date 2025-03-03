import pygame
import random

def play_soundtrack():
    pygame.mixer.init()
    pygame.mixer.music.load(theme)
    pygame.mixer.music.play(loops=-1)

def play_collision():
    pygame.mixer.init()
    pygame.mixer.Sound(random.choice(collisions)).play()

def play_score():
    pygame.mixer.init()
    pygame.mixer.Sound(score).play()

def stop_soundtrack():
    pygame.mixer.music.stop()


collisions = [
    'sounds/collision_1.mp3',
    'sounds/collision_2.mp3',
    'sounds/collision_3.mp3']


score = 'sounds/score.mp3'
theme = 'sounds/theme.mp3'