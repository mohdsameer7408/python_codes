wt = input("Enter your weight = ")
u = input("Enter the weight unit ( L for ponds and K for kilograms  = ")
if u.upper() == 'L':
    print(f"your weight is {float(wt)*0.45} kilos")
elif u.upper() == 'K':
    print(f"your weight is {float(wt)/0.45} ponds")
else:
    print("invalid unit")
