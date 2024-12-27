from karel.stanfordkarel import *

# function makes Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    move2()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_right()
    turn_right()
    move2()
    move()
    turn_right()
    move()
    turn_right()

# Makes Karel to move 2 steps    
def move2():
    move()
    move()

# Make Karel to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()