from karel.stanfordkarel import *

"""
Karel repaires each of the columns in the temple
"""

def main():
    build_move()
    for m in range(4):
        move()
    build_move()
    for r in range(2):
        turn_right()
    while front_is_clear():
        move()
        put_beeper()
    turn_left()

#builds a column and moves avoiding obstacles
def build_move():
    turn_left()
    build_column()
    put_beeper()
    if front_is_blocked():
        turn_right()
    for c in range(4):
        move()
    if front_is_clear():
        turn_right()
        build_column()
    put_beeper()
    turn_left()

#builds a colum
def build_column():
    while front_is_clear():
       put_beeper()
       move()

#makes a right turn
def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()