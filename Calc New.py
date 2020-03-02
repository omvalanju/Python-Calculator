print("-------------------CALCULATOR--------------------")

print("Enter two numbers:")


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calc(num1, num2, operator):
    if operator == '1':
        return add(num1, num2)

    elif operator == '2':
        return subtract(num1, num2)

    elif operator == '3':
        return multiply(num1, num2)

    elif operator == '4':
        try:
            return divide(num1, num2)
        except ZeroDivisionError:
            return "Undefined"

    elif operator == "5":
        exit()

    elif operator == "6":
        i = 0
        solution = (calc(num1, num2, operator))
        i = i + solution
        print(i)

        while True:
            num1 = i
            num2 = int(input("Number: "))
            operator = input("Operator: ")

        y = calc(num1, num2, operator)

        i = y

        print(y)


    else:
        return "Invalid input"


i = 0
solution = (calc(num1, num2, operator))
i = i + solution
print(i)

# while True:
# num1 = i
# num2 = int(input("Number: "))
# operator = input("Operator: ")

# y = calc(num1, num2, operator)

# i = y

# print(y)


elif operator == "6":
i = 0
solution = (calc(num1, num2, operator))
i = i + solution
print(i)

while True:
    num1 = i
    num2 = int(input("Number: "))
    operator = input("Operator: ")

y = calc(num1, num2, operator)

i = y

print(y)