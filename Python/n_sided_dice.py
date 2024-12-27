import random

"""
Program takes an input the number of sides on a dice.  
Then, simulate rolling a dice with that many sides. 
At the end, it prints the outcome of the roll. 
"""

def main():
    num_sides = int(input("How many sides does your dice have? "))
    die = random.randint(1, num_sides)
    print("Your roll is ", die)


if __name__ == '__main__':
    main()