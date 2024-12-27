"""
Program calculates social security deductions, 
employer contributions, and income taxes for individuals 
in the Dominican Republic, offering a user-friendly interface 
for input, accurate tax computations, and detailed summaries 
of deductions and net income.
"""

def main():
    print("""
Welcome to Social Security Treasury and Tax deduction calculator
""")
    name = input("What is your name? ")
    greeting = f"Nice meeting you, {name}!"
    print(greeting)
    
    income_value = income(name)
    if income_value is not None:
        net_income, sfs_econtribution, afp_econtribution = sfs_afp(income_value)
        srl_contribution = srl(income_value)
        income_tax = isr(net_income)
        print(f"""
Taxes & total income
- ISR - Income tax: RD${income_tax:.2f}
- Total income after deductions: RD${net_income - income_tax:.2f}""")
        print(f"""
Employer contributions
- ARS - Insurance contribution: RD${sfs_econtribution:.2f}
- AFP - Retirement contribution: RD${afp_econtribution:.2f}
- SRL - Occupational Risk Insurance: RD${srl_contribution:.2f}""")

def income(name):
    valid_options = [1, 2]  # List of valid options
    max_attempts = 3  # Number of allowed tries

    for attempt in range(max_attempts):
        try:
            user_input = int(input("""Choose your type of income:
    1. Fixed salary
    2. Hourly paid
    """))
            if user_input not in valid_options:
                print(f"Invalid option. {name}, please select a valid entry.")
            else:
                break  # Valid option, exit the loop
        except ValueError:
            print(f"Invalid input. {name}, please enter a number (1 or 2).")
    else:
        print(f"I am sorry, {name}. You have reached the maximum attempts. Please, try again later...")
        return None

    if user_input == 1:
        try:
            salary = float(input("Enter your salary RD$: "))
            print(f"{name}, your entered salary is RD${salary}.")
            return salary
        except ValueError:
            print("Invalid input. Please enter a numeric value for the salary.")
            return None
    elif user_input == 2:
        try:
            hourly_rate = float(input("Enter your hourly rate RD$: "))
            day_hours = float(input("Enter your daily worked hours: "))
            monthly_income = hourly_rate * day_hours * 22  # Assuming 22 working days in a month
            print(f"{name}, your entered hourly rate is RD${hourly_rate}, times {day_hours} worked hours per day, your monthly earning is RD${monthly_income}.")
            return monthly_income
        except ValueError:
            print("Invalid input. Please enter a numeric value for the hourly rate and hours.")
            return None

def sfs_afp(income):
    # Insurance contributions by employee and employer
    sfs_worker_percentage = 3.04
    sfs_employer_percentage = 7.09
    sfs_wdeduction = (income * sfs_worker_percentage) / 100
    sfs_econtribution = (income * sfs_employer_percentage) / 100
    
    # Retirement fund contributions by employee and employer
    afp_worker_percentage = 2.87
    afp_employer_percentage = 7.10
    afp_wdeduction = (income * afp_worker_percentage) / 100
    afp_econtribution = (income * afp_employer_percentage) / 100
    
    net_income = income - sfs_wdeduction - afp_wdeduction

    print(f"""
TSS - Social Security Treasury deductions
    - ARS - Insurance deduction: RD${sfs_wdeduction:.2f}
    - AFP - Retirement deduction: RD${afp_wdeduction:.2f}""")
    
    return net_income, sfs_econtribution, afp_econtribution
    
def srl(income):
    # Occupational Risk Insurance by employer
    srl_percentage = 1.10
    srl_contribution = (income * srl_percentage) / 100
    return srl_contribution

def isr(net_income):
    level1 = 34685
    level2 = 52027.42
    level3 = 72260.25

    if net_income <= level1:
        return 0
    elif net_income <= level2:
        return (net_income - level1) * 0.15
    elif net_income <= level3:
        return (net_income - level2) * 0.20 + 2601.36
    else:
        return (net_income - level3) * 0.25 + 6647.92

if __name__ == "__main__":
    main()
