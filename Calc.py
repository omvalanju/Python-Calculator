def power(x, y):
    if y == 0:
        return 1

    elif y == 1:
        return x

    else:
        i = 0
        z = x * x
        while i < y - 2:
            z = z * x
            i = i + 1

    return z


# Defining add function
def add(num1, num2):
    return num1 + num2


# Defining subtract function
def subtract(num1, num2):
    return num1 - num2


# Defining multiplication function
def multiply(num1, num2):
    return num1 * num2


# Defining divide function
def divide(num1, num2):
    return num1 / num2


# Defining triangular number function
def trino(num1):
    return int(((num1 * num1) + num1) / 2)


def infiseries(denominator, endnum):
    x = 0
    for i in range(1, endnum + 1):
        y = i / (power(denominator, i))
        x = x + y

    return x


# Defining calculator function
def calc(num1, num2, operator):
    while True:  # Keeps code running until user selects exit option
        try:
            if operator == '1':  # if user selects addition operation
                return add(num1, num2)

            elif operator == '2':  # if user selects subtract operation
                return subtract(num1, num2)

            elif operator == '3':  # if user selects multiplication operation
                return multiply(num1, num2)

            elif operator == '4':  # if user selects division operation
                try:
                    return divide(num1, num2)
                except ZeroDivisionError:  # Exception for divide by zero error
                    return "Undefined"

            elif operator == "5":
                return trino(num1)

            elif operator == "6":
                return infiseries(num1, num2)

            elif operator == "7":
                exit()

        except TypeError:
            return "Enter a number"

        else:
            return "Invalid input"


print("-------------------CALCULATOR--------------------")

while True:
    while True:
        try:
            print("Select Operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. "
                  "Triangular number \n 6. Infinite series \n 7. String operations \n 8. Exit")

            operator = (input("Enter Operation Number: "))

            if operator == "8":
                exit()

        except ValueError:
            print("Enter an Integer")
            continue

        else:
            break

    while True:
        print("Enter number(s):")

        if operator == "7":
            while True:
                try:
                    x = eval(input("Enter string:"))
                    print("Answer:",x)
                    break

                except NameError:
                    print ("Enter integers")
                    continue

                except TypeError:
                    print("Unsupported Operator")
                    continue

            break

        if operator == "6":
            try:
                num1 = int(input("Enter Denominator: "))
                if num1 == 0:
                    print("Enter a Non Zero Value")
                    continue
            except ValueError:
                print("Enter an Integer")
                continue

            else:
                break
        else:
            try:
                num1 = int(input("Number 1: "))

            except ValueError:
                print("Enter an Integer")
                continue

            else:
                break

    while True:
        if operator == "7":
            break

        if operator == "5":
            num2 = 0
            break

        elif operator == "6":
            try:
                num2 = int(input("Enter end value: "))

            except ValueError:
                print("Enter an Integer")
                continue

            else:
                break


        else:
            try:
                num2 = int(input("Number 2: "))

            except ValueError:
                print("Enter an Integer")
                continue

            else:
                break

    # if __name__=="__main__":
    if operator == "7":
        break

    else:
        solution = (calc(num1, num2, operator))
        print("Answer:", solution)

    while True:
        print("Select option: \n 1. Clear \n 2. Continue operation \n 3. Exit")
        try:
            option = int(input("Enter option number: "))
            if option == 1:
                break

            if option == 2:
                print("Select Operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. "
                      "Triangular number \n 6. Infinite series \n 7. Exit")

                operator = (input("select operator: "))

                if operator == "7":
                    exit()

                else:
                    num1 = solution
                    num2 = int(input("Enter number: "))

                    solution = (calc(num1, num2, operator))
                    print("Answer:", solution)

                    continue

            if option == 3:
                exit()

        except ValueError:
            print("Enter an Integer")
            continue

        else:
            break
