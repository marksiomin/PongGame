import tkinter as tk
import config as c
import logic as lg

### Custom designs for Buttons, Text and Frames


class Custom_Button(tk.Button):

    def __init__(self, text, command, master=None):
        default_setup = {'bg':'black',
        'activebackground':'black',
        'activeforeground':'white',
        'fg':'white',
        'relief':'flat',
        'font':('Fixedsys', 40),
        'bd':0}

        super().__init__(master, text=text, command=command, **default_setup)
        self.bind("<Enter>", c.on_enter)
        self.bind("<Leave>", c.on_leave)

    
class Custom_Frame(tk.Frame):
    def __init__(self, root):
        default_setup = {'width':1000,
                         'height':800,
                         'background':'black'}
        
        super().__init__(root, **default_setup)

class Custom_Text(tk.Label):
    def __init__(self, root, text):
        default_setup = {'font':('Fixedsys', 20), 
                         'fg':'white', 
                         'bg':'black'}

        super().__init__(root, text=text, **default_setup)

class Scoreboard:
    def __init__(self, frame):
        self.score_left = tk.Label(frame, text='0', font=('Fixedsys', 120), bg='black', fg='white')
        self.score_left.place(x=250, y=100, anchor='center')

        self.score_right = tk.Label(frame, text='0', font=('Fixedsys', 120), bg='black', fg='white')
        self.score_right.place(x=750, y=100, anchor='center')

class Net(tk.Canvas):
    def __init__(self, frame):
        super().__init__(frame, height=1000, width=10, background='black')  
        self.create_line(500, 0, 500, 1000, fill='white', width=10, dash=(50, 50)) 
        self.pack(fill=tk.BOTH, expand=True) 

class Restart_Window(Custom_Frame):
    def __init__(self, frame):
        self.restart_frame = Custom_Frame(frame)
        self.restart_frame.config(width=600, height=300)

        self.winner = tk.Label(self.restart_frame, text='Placeholder', font=('Fixedsys', 80), bg='black', fg='white')
        self.winner.pack(side=tk.TOP)

        self.restart_label = tk.Label(self.restart_frame, text="Restart?", font=('Fixedsys', 30), bg='black', fg='white')
        self.restart_label.pack(side=tk.LEFT, padx=30)

 
        self.yes_button = Custom_Button('Yes', command=None, master=self.restart_frame)
        self.yes_button.pack(side=tk.LEFT)

        self.no_button = Custom_Button('No', command=None, master=self.restart_frame)
        self.no_button.pack(side=tk.LEFT)

class Help_Frame(Custom_Frame):
    def __init__(self, master):
        super().__init__(master)
        controls = Custom_Text(self, text='Controls')
        controls.place(relx=0.5, rely=0.2, anchor='center')

        l1 = Custom_Text(self, text='Player 1')
        l2 = Custom_Text(self, text='Up: W')
        l3 = Custom_Text(self, text='Down: S')

        l4 = Custom_Text(self, text='Player 2')
        l5 = Custom_Text(self, text='Up: ▲')
        l6 = Custom_Text(self, text='Down: ▼')

        rules = Custom_Text(self, text='The classic pong game, first to 3 wins!')

        ball_speed = Custom_Text(self, text='Ball Speed')

        scale = tk.Scale(self, from_=1, to=10, orient=tk.HORIZONTAL, bg='black', fg='white', troughcolor='white', activebackground='black', font=('Fixedsys', 20))
        scale.set(5)

        def on_scale_change(scale_velocity):
            c.ball_velocity = int(scale_velocity)

        scale.config(command=on_scale_change)

        l1.place(relx=0.3, rely=0.3)
        l2.place(relx=0.3, rely=0.35)
        l3.place(relx=0.3, rely=0.4)

        l4.place(relx=0.6, rely=0.3)
        l5.place(relx=0.6, rely=0.35)
        l6.place(relx=0.6, rely=0.4)

        ball_speed.place(relx=0.35, rely=0.51)
        scale.place(relx=0.55, rely=0.5)

        rules.place(relx=0.5, rely=0.7, anchor='center')

        return_button_help = Custom_Button('RETURN TO MAIN SCREEN', command=self.return_to_main_screen, master=self)
        return_button_help.place(relx=0.5, rely=0.9, anchor='center')

    def return_to_main_screen(self):
        lg.switch_frames('main') 
        
class Credit_Frame(Custom_Frame):
    def __init__(self, master):
        super().__init__(master)
        credit_label = Custom_Text(self, text='Special thanks goes to Polina <3')
        credit_label.place(relx=0.5, rely=0.5, anchor='center')

        return_button_credit = Custom_Button('RETURN TO MAIN SCREEN', command=self.return_to_main_screen, master=self)
        return_button_credit.place(relx=0.5, rely=0.9, anchor='center')

    def return_to_main_screen(self):
        lg.switch_frames('main')  

class Main_Screen(Custom_Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(master)
    
        play_button = Custom_Button('PLAY', self.play_window, master=self)
        play_button.place(relx=0.5, rely=0.4, anchor='center')
        
        help_button = Custom_Button('HELP', self.help_window, master=self)
        help_button.place(relx=0.5, rely=0.5, anchor='center')
        
        credit_button = Custom_Button('CREDIT', self.credit_window, master=self)
        credit_button.place(relx=0.5, rely=0.6, anchor='center') 

    def play_window(self):
        lg.switch_frames('play') 
        game = lg.Game(c.frames['play'], self.master)
        game.start_game()

    def help_window(self):
        lg.switch_frames('help')  

    def credit_window(self):
        lg.switch_frames('credit')  
