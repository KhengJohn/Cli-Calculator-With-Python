print("CLI Calculator With Python")


def Addition(number1, number2):
    solution = number1 + number2
    return solution


def Subtraction(number1, number2):
    solution = number1 - number2
    return solution


def Multiplication(number1, number2):
    solution = number1 * number2
    return solution


def Division(number1, number2):
    solution = number1 / number2
    return solution


def Modulus(number1, number2):
    solution = number1 % number2
    return solution


def input_number():
    number1 = input("Enter First Number >> ")
    number2 = input("Enter Second Number >> ")
    number1 = int(number1)
    number2 = int(number2)
    return number1, number2


while True:
    print("""
        A for Addition
        S for Subtraction
        M for Multiplication
        D for Division
        R for Modulus

        E for Escape
        """)
    option = input(">> ")
    option = option.lower()

    if option == "a":
        number1, number2 = input_number()
        solution = Addition(number1, number2)
        print("Answer Is " + str(solution))

    if option == "s":
        number1, number2 = input_number()
        solution = Subtraction(number1, number2)
        print("Answer Is " + str(solution))

    if option == "m":
        number1, number2 = input_number()
        solution = Multiplication(number1, number2)
        print("Answer Is " + str(solution))

    if option == "d":
        number1, number2 = input_number()
        solution = Division(number1, number2)
        print("Answer Is " + str(solution))

    if option == "r":
        number1, number2 = input_number()
        solution = Modulus(number1, number2)
        print("Answer Is " + str(solution))

    if option == "e":
        exit()
