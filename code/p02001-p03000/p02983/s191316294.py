import sys
import math


def get_iv():
    args = sys.stdin.readline()
    argv = args.split()
    iargv = [int(arg) for arg in argv]
    return iargv


def min_mod_prod(L, R):
    min_rem = 2019
    for i in range(L, R + 1):
        if min_rem == 0:
            break
        for j in range(i + 1, R + 1):
            if min_rem == 0:
                break
            tst = (i * j) % 2019
            if tst < min_rem:
                minij = [i, j]
                min_rem = tst

    minij.append(min_rem)
    return minij


def main():
    specs = get_iv()
    L = specs[0]
    R = specs[1]
    rv = min_mod_prod(L, R)
    # print(rv)
    print(rv[2])


if __name__ == '__main__':
    main()