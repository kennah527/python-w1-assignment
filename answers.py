signs = ['+', '-', '*', '/']

number1 = input('Enter the first Number: ')
sign = input('Enter the operator sign: ')
number2 = input('Enter the second Number: ')

if sign not in signs:
    print("The sign is invalid")
else:
    number1 = int(number1)
    number2 = int(number2)
    result = 0
    if sign == '+':
        result = number1+number2
        print(f'The result of {number1} {sign} {number2} is {result}')
    elif sign == '-':
        result = number1 - number2
        print(f'The result of {number1} {sign} {number2} is {result}')
    elif sign == '*':
        result = number1*number2
        print(f'The result of {number1} {sign} {number2} is {result}')
    elif sign =='/':
        result = number1/number2
        print(f'The result of {number1} {sign} {number2} is {result}')
    else:
        print("INVALID INPUT")
