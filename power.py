def power(x,y):
    if y == 0:
        return 1

    elif y == 1:
        return x

    else:
        i = 0
        z = x * x
        while i < y-2:
            z = z * x
            i = i + 1

    return z

print(power(2,2))