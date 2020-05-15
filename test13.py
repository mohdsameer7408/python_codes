numbers = [2,3,1,44,20]
g = numbers[0]
for i in numbers:
    if g < i:
        g = i
print(f"Greatest number is = {g}")
num = numbers.copy()
num.append(10)
print(num, numbers)
n = [2,2,4,6,5,4,5,4,6]
a = []
for n1 in n:
    if n1 not in a:
        a.append(n1)
print(a)
tuple1 = (1,2,3)
x,y,z = tuple1
print(x,y,z)
list1 = [1,2,3]
x,y,z = list1
print(x,y,z)