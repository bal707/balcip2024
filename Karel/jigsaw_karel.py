from karel.stanfordkarel import *

"""
Karel finishes the puzzle by picking up a last beeper 
(puzzle piece) and placing it in the right spot. Karel ends
in the same position where she starts in -- the bottom left 
corner of the world.
"""

def main():
#move and pict up beeper
#put puzzle piece in place
#return to starting point
    pick_piece()
    put_puzzle()
    return_Karel()

#piece pickin
def pick_piece():   
    for p in range(2):
        move()
    pick_beeper()

#puzzling
def put_puzzle():
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    put_beeper()

#returning 
def return_Karel():
    for t in range(2):
        turn_left()
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_right()
        while front_is_clear():
            move()
        for r in range(2):
            turn_right()

#turning right 
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()