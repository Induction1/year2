import sys


def repeat(s, t):
    return " ".join([s for i in range(t)]).capitalize() + "."


if __name__ == "__main__":
    s = sys.argv[1]
    t = int(sys.argv[2])
    print(repeat(s, t))