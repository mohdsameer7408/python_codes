# Exception handling in python :)!!!
try:
    age = int(input("Age : "))
    income = 20000
    risk = income / age
    print(f"Age = {age},  Risk = {risk}")
except ZeroDivisionError:
    print("Age can't be zero!")
except ValueError:
    print("Invalid value!")
