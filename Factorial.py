# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        print(n * factorial(n - 1))
        return n * factorial(n - 1)


# Refactored
def factorial1(x):
    total = 1
    while x > 0:
        total *= x
        x = x - 1
    print(total)
    return total


# Original
def factorial2(m):
    if m == 0:
        return 1
    elif m == 1:
        return m
    else:
        for z in range(1, m):
            m *= z
            print(m)
    return m


print("Factorial #1")
factorial(4)
print("Factorial #2")
factorial1(5)
print("Factorial #3")
factorial2(6)
