def collatz(number):
    value = 0
    if number % 2 == 0:
        value = number // 2
        print(value)
    elif number % 2 == 1:
        value = 3 * number + 1
        print(value)
    return value

while True:
    print('Please enter a number: ')
    try:
        user_input = int(input())
        break
    except ValueError:
        print('Invalid Number, Enter Numeric Value')

while True:
    result = collatz(user_input)
    if result == 1:
        break
    else:
        user_input = result
