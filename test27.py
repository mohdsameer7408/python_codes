import datetime        # datetime module
# items = [
#     ('Product1', 10),
#     ('Product2', 9),
#     ('Product3', 12)
# ]


# def sort_price(item):
#     return item[1]
#
#
# items.sort(key=sort_price)
# print(items)

# items.sort(key=lambda item: item[1])
# print(items)

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)

# prices = list(map(lambda item: item[1], items))
# print(f"Prices: {prices}")
#
# n = [3, 51, 2, 8, 6]
# # n.sort(reverse=True)
# print(sorted(n, reverse=True))

# Understanding __repr__ ==> unambiguous and __str__ ==> easy to read ......
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return 'Car({self.color}, {self.mileage})'.format(self=self)

    def __str__(self):
        return '__str__ for Car'


my_car = Car('red', '4234')
print(my_car)

today = datetime.date.today()
print(str(today))
print(repr(today))
