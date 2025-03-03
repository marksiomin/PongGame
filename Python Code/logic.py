import tkinter as tk
import config as c
import random as random
import graphics as gr
import sound 

# Module for Game mechanics, ball movement, collision, restarting game etc.

def switch_frames(frame_key):
    current_frame = c.frames.get(c.frame)
    next_frame = c.frames.get(frame_key)

    print(f'current frame:{current_frame} | next frame {next_frame}')
            
    current_frame.pack_forget() 
    c.frame = frame_key 
    next_frame.tkraise()  
    next_frame.pack(fill=tk.BOTH, expand=True)


class Ball(tk.Canvas):
    def __init__(self, master=None):
        default_setup = {'height':10, 
                         'width':10, 
                         'bg':'white'}

        (self.pos_x, self.pos_y) = random.choice(c.BALL_LOCATIONS)
        (self.vel_x, self.vel_y) = (random.choice(c.starting_velocity) * c.ball_velocity, random.choice(c.starting_velocity) * c.ball_velocity)
        super().__init__(master, **default_setup)

    def place(self):
        super().place(x=self.pos_x, y=self.pos_y)

    def move(self):
        if not c.ball_moving:  
            return

        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def collision(self, player_1, player_2, score_right, score_left):
        if (c.player1_moving and c.player2_moving) == False:
            return

        if self.pos_y <= 0 or self.pos_y >= 780:  # 780 is the bottom boundary
            sound.play_collision()
            self.vel_y = -self.vel_y

        if (100 <= self.pos_x <= 110 and player_1.winfo_y() <= self.pos_y <= player_1.winfo_y() + 100):
            sound.play_collision()
            if (player_1.winfo_y() + 45 <= self.pos_y <= player_1.winfo_y() + 55):
                self.vel_y = 0  
            elif (player_1.winfo_y() <= self.pos_y <= player_1.winfo_y() + 45):
                self.vel_y = -abs(c.ball_velocity)
            else:
                self.vel_y = abs(c.ball_velocity)
            self.vel_x = -self.vel_x

        if (900 >= self.pos_x >= 890 and player_2.winfo_y() <= self.pos_y <= player_2.winfo_y() + 100):
            sound.play_collision()
            if (player_2.winfo_y() + 45 <= self.pos_y <= player_2.winfo_y() + 55):
                self.vel_y = 0
            elif (player_2.winfo_y() <= self.pos_y <= player_2.winfo_y() + 45):
                self.vel_y = -abs(c.ball_velocity)
            else:
                self.vel_y = abs(c.ball_velocity)
            self.vel_x = -self.vel_x
        

        if self.pos_x <= 0:  # Right player scores
            sound.play_score()
            update_score = int(score_right.cget("text"))
            
            if update_score < 3:
                update_score += 1
                score_right.config(text=str(update_score))
                
            if update_score == 3:
                return 'PLAYER 2 WON'
            
            self.reset_position()
    
       
        if self.pos_x >= 1000:  # Left player scores
            sound.play_score()
            update_score = int(score_left.cget("text"))
            
            if update_score < 3:
                update_score += 1
                score_left.config(text=str(update_score))
                
            if update_score == 3:
                return 'PLAYER 1 WON'
            
            self.reset_position()

    def reset_position(self):
            (self.pos_x, self.pos_y) = random.choice(c.BALL_LOCATIONS)
            (self.vel_x,self.vel_y) = (random.choice(c.starting_velocity)*c.ball_velocity, random.choice(c.starting_velocity)*c.ball_velocity)
            self.place()


class Paddle(tk.Canvas):
    def __init__(self, player, master=None):
        default_setup = {'height':100, 
                         'width':10, 
                         'bg':'white'}
        
        self.player = player
        (self.pos_x, self.pos_y) = (c.PLAYER1_START_LOC[0], c.PLAYER1_START_LOC[1]) if self.player == 1 else (c.PLAYER2_START_LOC[0], c.PLAYER2_START_LOC[1])

        super().__init__(master, **default_setup)

    def place(self):
        super().place(x=self.pos_x, y=self.pos_y) 

    def move(self):
        if self.player == 1:
            if c.is_key_pressed("w"):
                self.move_up()
            if c.is_key_pressed("s"):
                self.move_down()

        elif self.player == 2:
            if c.is_key_pressed("Up"):
                self.move_up()
            if c.is_key_pressed("Down"):
                self.move_down()

    def move_up(self):
        new_y = self.winfo_y() - 20
        if new_y >= 0 and (c.player1_moving or c.player2_moving):  # Ensure the paddle stays within the screen
            self.pos_x, self.pos_y = self.winfo_x(), new_y
            self.place()

    def move_down(self):
        new_y = self.winfo_y() + 20
        if new_y <= 700 and (c.player1_moving or c.player2_moving):  # Ensure the paddle stays within the screen
            self.pos_x, self.pos_y = self.winfo_x(), new_y
            self.place()

    def reset_position(self):
        (self.pos_x, self.pos_y) = (c.PLAYER1_START_LOC[0], c.PLAYER1_START_LOC[1]) if self.player == 1 else (c.PLAYER2_START_LOC[0], c.PLAYER2_START_LOC[1])
        self.place()


class Game(Paddle, Ball):
    def __init__(self, frame, root):
        self.frame = frame
        self.root = root
        self.net = gr.Net(frame)
        self.scoreboard = gr.Scoreboard(frame)
        
        self.ball = Ball(master=frame)
        self.player_1 = Paddle(player=1, master=frame)
        self.player_2 = Paddle(player=2, master=frame)

        self.restart_window = gr.Restart_Window(self.frame)

        c.game_destroyed = False
        self.player_1.place()
        self.player_2.place()
        self.ball.place()

    def end_game(self, result):
        c.ball_moving, c.player1_moving, c.player2_moving = False, False, False

        self.restart_window.restart_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.restart_window.winner.config(text=result)
        
        self.restart_window.yes_button.config(command=self.restart_game)
        self.restart_window.no_button.config(command=self.close_game)

    def restart_game(self):
        c.ball_moving, c.player1_moving, c.player2_moving = True, True, True

        self.ball.reset_position()
        self.player_1.reset_position()
        self.player_2.reset_position()

        self.scoreboard.score_left.config(text='0') 
        self.scoreboard.score_right.config(text='0')  
        self.restart_window.restart_frame.place_forget()  

    def close_game(self):
        c.game_destroyed = True

        self.restart_window.restart_frame.destroy()
        self.ball.destroy()
        self.net.destroy()
        self.player_1.destroy()
        self.player_2.destroy()
        
        
        
        sound.play_soundtrack()
        switch_frames('main')
        
    def start_game(self):
        c.ball_moving, c.player1_moving, c.player2_moving = True, True, True
        sound.stop_soundtrack()
        self.move_ball()
        self.move_paddles()

    def move_paddles(self):
        self.player_1.move()
        self.player_2.move()
        self.root.after(10, self.move_paddles)

    def move_ball(self):
        self.ball.move()
        winner = self.ball.collision(self.player_1, self.player_2, self.scoreboard.score_right, self.scoreboard.score_left)

        if winner:
            sound.play_score()
            self.end_game(winner)

        if not(c.game_destroyed):
            self.ball.place()  
            self.root.after(10, self.move_ball)