import random
randomous = 100

"""
Program that helps other people learn arithmetic metics! 
It randomly generates a simple arithmetic problem (addition, substraction, others)
based on 100 for the user, reads in the answer from the user, and then checks to 
see if they got it right or wrong.
"""

def main():
    do = int(input(""" Welcome to Khansole Calculator
    Choose an option (number)
    1. Addition
    2. Substraction 
    3. Multiplication
    4. Division
    5. Module \n"""))

    while do >= 0 or do <= 6:

        if do == 1:
            addition()
        elif do == 2:
            substraction()
        elif do == 3:
            multiplication()
        elif do == 4:
            division()
        elif do == 5:
            module()
        else:
            print("Complete entry")
            break

def module():
    correct = 0

    for _ in range(3):
        
        print("Khansole Academy Module")
        
        num1 = random.randint(1, randomous)
        num2 = random.randint(1, randomous)

        print("What is " + str(num1) + " % " + str(num2) + "?")
        module = int(input(""))

        total_module = num1 % num2 

        print("Your answer: " + str(module))

        if module == total_module:
            print("Correct!")
            correct +=1
            print("You've gotten " + str(correct) + " correct in a row. ")
        else:
            print("Incorrect. \nThe expected answer is " + str(total_module))

        print("")

def division():
    correct = 0

    for _ in range(3):
        
        print("Khansole Academy Division")
        
        num1 = random.randint(1, randomous)
        num2 = random.randint(1, randomous)

        print("What is " + str(num1) + " / " + str(num2) + "?")
        division = int(input(""))

        total_division = num1 / num2 

        print("Your answer: " + str(division))

        if division == total_division:
            print("Correct!")
            correct +=1
            print("You've gotten " + str(correct) + " correct in a row. ")
        else:
            print("Incorrect. \nThe expected answer is " + str(total_division))

        print("")

def multiplication():
    correct = 0

    for _ in range(3):
        
        print("Khansole Academy Multiplication")
        
        num1 = random.randint(1, randomous)
        num2 = random.randint(1, randomous)

        print("What is " + str(num1) + " * " + str(num2) + "?")
        multiplication = int(input(""))

        total_multiplication = num1 * num2 

        print("Your answer: " + str(multiplication))

        if multiplication == total_multiplication:
            print("Correct!")
            correct +=1
            print("You've gotten " + str(correct) + " correct in a row. ")
        else:
            print("Incorrect. \nThe expected answer is " + str(total_multiplication))

        print("")

def substraction():
    correct = 0

    for _ in range(3):
        
        print("Khansole Academy Subtraction")
        
        num1 = random.randint(1, randomous)
        num2 = random.randint(1, randomous)

        print("What is " + str(num1) + " - " + str(num2) + "?")
        substraction = int(input(""))

        total_substraction = num1 - num2 

        print("Your answer: " + str(substraction))

        if substraction == total_substraction:
            print("Correct!")
            correct +=1
            print("You've gotten " + str(correct) + " correct in a row. ")
        else:
            print("Incorrect. \nThe expected answer is " + str(total_substraction))

        print("")

def addition():
    correct = 0

    for _ in range(3):
        
        print("Khansole Academy Addition")
        
        num1 = random.randint(1, randomous)
        num2 = random.randint(1, randomous)

        print("What is " + str(num1) + " + " + str(num2) + "?")
        addition = int(input(""))

        total_addition = num1 + num2 

        print("Your answer: " + str(addition))

        if addition == total_addition:
            print("Correct!")
            correct +=1
            print("You've gotten " + str(correct) + " correct in a row. ")
        else:
            print("Incorrect. \nThe expected answer is " + str(total_addition))

        print("")

if __name__ == '__main__':
    main()