import tkinter as tk
from graphics import Main_Screen, Help_Frame, Credit_Frame, Custom_Frame

### Key bindings, player and ball movements, frame configs are here

def key_press(event):
        key_state[event.keysym] = True

def key_release(event):
        key_state[event.keysym] = False

def is_key_pressed(key):
    return key_state.get(key)

def bind_keys(root):
    root.bind("<w>", key_press)
    root.bind("<s>", key_press)
    root.bind("<Up>", key_press)
    root.bind("<Down>", key_press)
    root.bind("<KeyRelease-w>", key_release)
    root.bind("<KeyRelease-s>", key_release)
    root.bind("<KeyRelease-Up>", key_release)
    root.bind("<KeyRelease-Down>", key_release)

# Event handling when hovering over button, will increase their size whilst ensuring padding between the other widgets
def on_enter(event):
    pass

def on_leave(event):
    pass
    

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

root = tk.Tk()
root.title('Pong Game')
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
root.config(background='black')
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(True, icon)
root.resizable(False, False)
bind_keys(root)


frames = {
    'main': Main_Screen(root),
    'help': Help_Frame(root),
    'credit': Credit_Frame(root),
    'play': Custom_Frame(root)}
frame = 'main'

ball_velocity = 4
ball_moving = True
player1_moving = True
player2_moving = True
game_destroyed = False


PLAYER1_START_LOC = (100, 350)
PLAYER2_START_LOC = (900, 350)


key_state = {
        "w": False,  # Player 1's up key
        "s": False,  # Player 1's down key
        "Up": False,  # Player 2's up key
        "Down": False,  # Player 2's down key
    }

# Ball location at the start of the game
BALL_LOCATIONS = [(550,400), 
                      (550,100), 
                      (550,700), 
                      (450,400), 
                      (450,100), 
                      (450,700)]

# Multiplied by the ball velocity to dictate initial (x,y) speed    
starting_velocity = [-1,1]
