# a simple console calculator

def simpleCalculator():
    while True:

        num1 = float(input('enter first no.:'))
        operator = input('enter operation.:')
        num2 = float(input('enter second no.:'))
        # num3 = input(*args, **kwargs )

        if operator == '+':
            Answer = num1 + num2
        elif operator == '-':
            Answer = num1 - num2
        elif operator == '*':
            Answer = num1 * num2
        elif operator == '/':
            Answer = num1 / num2
        else:
            print('operation not supported!')
            continue

        print('The answer =', Answer)

        viewChoice = input("Would you like to continue (y/n):")

        if viewChoice.lower() != 'y':
            break


simpleCalculator()
