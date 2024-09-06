import sys


def factorial(x):
    if x <= 0:
        return 1

    res = 1
    for i in range(1, x+1):
        res *= i
    return res


if __name__ == "__main__":
    x = int(sys.argv[1])
    print(factorial(x))