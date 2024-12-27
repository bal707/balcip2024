from karel.stanfordkarel import *

"""
Karel is be able to place 20 beepers, then 24 beepers, 
and end facing East to  the right of the 24 beepers.
"""

def main():
    #Karel complete her task in this function. 
    karel_celebration()

#make a drop of 20 and 24 beepers    
def karel_celebration():    
    move_20()
    move_24()

#make a drop of 20 beepers and move a step ahead    
def move_20():
    for i in range(20):
        put_beeper()
    move()

#make a drop of 24 beepers and move a step ahead
def move_24():
    for i in range(24):
        put_beeper()
    move()
    
    
if __name__ == '__main__':
    main()