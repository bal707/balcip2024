from karel.stanfordkarel import *

#function makes Karel  pick up all the beepers in the world.
def main():    
    move_forward()

def move_forward():
    while front_is_clear():
        move()
        while beepers_present():
            pick_beeper()
   
if __name__ == '__main__':
    main()