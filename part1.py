import random

from HW4 import deal
from decouple import config
from random import randint

money = (config('MY_MONEY'))


def part1(d):
    a = int(input('Choose a number from 1 to 30:'))
    b = random.randint(1, 31)
    if a == b:
        print(f'You won {d*2}')
        money += d*2
    else:
        print(f'You are at loss {d}')
        money -= d

