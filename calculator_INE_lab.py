def calculator(operation, x, y):
    def add():
        print(x + y)

    def subtract():
        print(x - y)

    def multiply():
        print(x * y)

    def divide():
        if y == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(x / y)

    def square():
        print(x ** 2)

    def power():
        print(x ** y)

    import math
    def square_root():
        print(math.sqrt(x))

    if operation == 'add':
        add()
    elif operation == 'subtract':
        subtract()
    elif operation == 'multiply':
        multiply()
    elif operation == 'divide':
        divide()
    elif operation == 'square':
        square()

    elif operation == 'power':
        power()

    elif operation == 'square root':
        square_root()

if __name__ == '__main__':
    while True:
        operation = input(">add\n>subtract\n>multiply\n>divide\n>square\n>power\n>square root\nchoise one of operations above or enter = to stop: ")
        if operation == "=":
            break
        else:
            x = float(input('first number: '))
            if operation != 'square' and 'square root':
                y = float(input('sacond number: '))
            else:
                y=1
            calculator(operation, x, y)
