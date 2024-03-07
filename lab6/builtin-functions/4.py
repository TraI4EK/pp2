from math import sqrt
from time import sleep

num = int(input())
miliseconds = int(input())
time_ = miliseconds/1000

sleep(time_)

square = sqrt(num)

print(f"Square root of {num} after {miliseconds} miliseconds is {square}")