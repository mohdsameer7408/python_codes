input = int(input('>'))


def fizz_buzz(input):
    if not(input % 3) and not(input % 5):
        print('FizzBuzz')
    elif not(input % 3):
        print('Fizz')
    elif not(input % 5):
        print('Buzz')
    else:
        print(input)


fizz_buzz(input)
