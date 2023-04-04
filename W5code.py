def fizz_buzz_sumz(i):
    sum = 0
    for x in range(1, i+1):
        if x % 3 == 0 and x % 5 != 0:
            sum = sum + 3 * x
        elif x % 5 == 0 and x % 3 != 0:
            sum = sum + 5 * x
        elif x % 3 == 0 and x % 5 == 0:
            sum = sum + 0 * x
        else:
            sum = sum + x
    return sum


def fizz_buzz_sumz(i):
    sum = 0
    for x in range(1, i+1):
        if x % 3 == 0 and x % 5 == 0:
            continue
        elif x % 3 == 0:
            sum += 3*x
        elif x % 5 == 0:
            sum += 5*x
        else:
            sum +=x
    return sum


