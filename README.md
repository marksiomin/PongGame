A retro Pong game using Python for the game logic, with Arduino for inputhandling. Currently compatible with a keyboard (under development), with future plans tointegrate a custom-designed PCB joystick for enhanced gameplay

list of modules:
-main.py
-graphics.py: handles the ui of buttons, frames, labels and canvasas 
-sounds.py: includes collision and score soundeffects, and handles the soundtrack
-logic.py: handles the game mechanics such collision between objects, winner announcements, restarting the game, and going back to the main screen
-config.py: handles key bindings, initial player and ball locations, initialzing the tk.window widget and the frames used 
