import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--bd',
        type=int,
        required=True,
        help='brirth day user'
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

def cal_todayVbd(bd):
    td = datetime.today().strftime('%d')
    return bd-int(td)

if __name__ == "__main__":
    input_v = parse_input()
    print('This is my frist .py')
    printHello(input_v.name)
    print(f'your birthday is {cal_todayVbd (input_v.bd)} from.today')

