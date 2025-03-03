import config as c
import logic as lg
import sound 


def main():
    lg.switch_frames('main')
    sound.play_soundtrack()
    c.root.mainloop()
    


if __name__ == '__main__':
    main() 

