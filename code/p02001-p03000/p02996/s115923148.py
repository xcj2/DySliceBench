import sys
from operator import itemgetter
import numpy as np
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def main():
    N = readint()
    ab = sorted([list(readnums()) for _ in range(N)], key=itemgetter(1))
    a = np.cumsum(np.array(list(map(lambda x: x[0], ab))))
    b = list(map(lambda x: x[1], ab))
    for A, B in zip(a, b):
        if A > B:
            print('No')
            sys.exit()

    print('Yes')


if __name__ == "__main__":
    main()
