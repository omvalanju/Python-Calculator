import math as m


def trino(num1):
    return int(((num1 * num1) + num1) / 2)


print(trino(5))


def infiseries(denominator, endnum):
    x = 0
    for i in range(1, endnum+1):
        y = i / (m.pow(denominator, i))
        x = x + y

    print (x)


infiseries(2,3)