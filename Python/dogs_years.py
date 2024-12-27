# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    # Asks user to enter humans years
    human_years = int(input("Enter an age in calendar years: "))

    # Calculates dogs age: multiplies constant times human years
    dog_years = human_years * DOG_YRS_MULTIPLIER
    
    # Prints dogs years based on humans
    print("That's" +" "+ str(dog_years) +" "+ "in dog years!")

if __name__ == '__main__':
    main()