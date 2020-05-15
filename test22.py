# About modules!
import test16
from test16 import emoji_converter
from utils import find_max
from bubble_sort import bubble_sort

print(test16.emoji_converter("good morning :)"))
print(emoji_converter("I am sad :("))

n = int(input('Enter a limit for the numbers = '))
num_l = []
print(f'Enter any {n} numbers :')
for i in range(0, n):
    num = int(input("> "))
    num_l.append(num)
print(f"Numbers are : {num_l}")
print(f"The greatest number from the above list is = {find_max(num_l)}")
print(f"The numbers after sorting is : {bubble_sort(num_l)}")
