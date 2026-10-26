# Python program to create calculator

def add(x:float, y:float) -> float:
    """
    Add two numbers
    :param x: The first number
    :param y: The second number
    :return: The sum of x and y
    """
    return x + y

def subtract(x:float, y:float) -> float:
    """
    Subtract two numbers
    :param x: The first number
    :param y: The second number
    :return: The difference of y from x
    """
    return x - y

def multiply(x:float, y:float) -> float:
    """
    Multiply two numbers
    :param x: The first number
    :param y: The second number
    :return: The product of x and y
    """
    return x * y

def divide(x:float, y:float) -> float:
    """
    Divide two numbers
    :param x: The first number
    :param y: The second number
    :return: The result of dividing x by y
    """
    if y == 0:
        return "Error. Division by zero"
    return x / y

def calculator()->None:
    """
    Simple calculator
    :return: None
    """

    print("\n\n_______Simple Calculator______")
    print("Enter your choice\n 1.Add\n 2.Subtract" \
    " 3.Multiply\n 4.Divide\n 5.Exit")

    while True:

        choice = input("Enter your choice")

        
        if choice == '5':
            break

        if choice in ('1','2','3','4'):
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1,num2)}")

            if choice == '2':
                print(f"{num1} - {num2} = {subtract(num1,num2)}")

            if choice == '3':
                print(f"{num1} * {num2} = {multiply(num1,num2)}")

            if choice == '4':
                print(f"{num1} / {num2} = {divide(num1,num2)}")


        else:
            print("Enter valid choice")

calculator()

        