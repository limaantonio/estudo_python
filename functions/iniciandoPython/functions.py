def call_number():
    for number in range(0, 10):
        print(number)


def call_number_with_limit(limit):
    list = range(0, 10)
    for number in range(limit):
        print(number)


def calculator(x, y):
    return x-y

result  = calculator(x = -10, y = 5)
print(result)