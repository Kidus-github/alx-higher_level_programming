#!/usr/bin/python3
import random

for _ in range(5):
    number = random.randint(-10, 10)
    if number > 0:
        print(f"{number:d} is positive")
    elif number == 0:
        print(f"{number:d} is zero")
    else:
        print(f"{number:d} is negative")
