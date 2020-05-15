# A program to find the greatest number!!!
def find_max(numbers):
    g = numbers[0]
    for i in numbers:
        if g < i:
            g = i
    return g
