from karel.stanfordkarel import *

def main():
    move_to_beeper()
    
# gen_action: Karel moves and puts beepers
# pre-condition: Karel at starting point facing East
# post-condition: Karel at ending point facing East
def move_to_beeper():   
    while front_is_clear(): # undefine condition - move
        move()
        if beepers_present(): # define condition - turn and build up
            turn_left()
            build_hospital()
            
# Builds full 3x2 hospital 
# pre-condition: Karel faces East/right
# post-condition: Karel faces East/right   
def build_hospital():
    for i in range(2): # for loop to move and put beepers
        move()
        put_beeper()
    turn_right()
    move()
    turn_right()
    for i in range(3):
        put_beeper()
        if front_is_clear(): 
            move()
    turn_left()
        
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()