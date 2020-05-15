name = input('Enter your name = ')
length = len(name)
if length < 3:
    print("Name must be at least 3 characters long")
elif length > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")