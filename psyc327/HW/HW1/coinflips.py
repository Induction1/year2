import sys
import numpy as np


def coinflips(n):
    t = 0.0
    for i in np.random.random_sample(n):
        t += i < 0.5

    return t/n


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(coinflips(n))