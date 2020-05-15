s = [23, 434, 323, [1, 2], 65, 254]
s.sort()
s1 = slice(5, 0, -1)
print(s[s1])

# To check for a list of binary numbers divisible by 5
a = [x for x in input('>').split(',')]
c = []
for i in a:
    if not int(i, 2) % 5:
        c.append(i)
print(c)
