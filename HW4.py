import random
from random import randint


def deal(d):
    a = random.randint(1, 31)
    b = int(input('Choose a number from 1 to 30:'))
    if a == b:
        print(f'You win {d*2}')
    else:
        print(f'You are at loss {d}')
