import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--dob',
        type=str,
        required=True,
        help='Date of birth in the format DD-MM-YYYY (e.g., 25-12-1990)'
    )

    parser.add_argument(
        '--name',
        default='Parames',
        type=str,
        help='input for the name of people using the app'
    )

#    parser.add_argument(
#        '--name',
#        type=int,
#        default=7,
#        help='input for XX'
#    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello World!,{who}!!")

def calculate_days_from_birth(dob):
    try:
        birth_date = datetime.strptime(dob, '%d-%m-%Y')
        today = datetime.today()
        delta = today - birth_date
        return delta.days
    except ValueError:
        raise ValueError("Invalid date format. Please use DD-MM-YYYY.")

if __name__ == "__main__":
    input_v = parse_input()
    print('This is my frist .py')
    printHello(input_v.name)
    print(f'your were born {calculate_days_from_birth (input_v.dob)} day from birth')

