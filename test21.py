# About inheritance!
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog = Dog()
dog.walk()
