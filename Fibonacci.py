# recursion
def fibonacci(x):
    if x < 0:
        return "Incorrect input"
    elif x == 0:
        return 0
    elif x == 1 or x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


def fibonacci1(n):

    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1 or n == 2:
        return b
    else:
        for i in range(3, n+2):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(9))
print(fibonacci1(9))
