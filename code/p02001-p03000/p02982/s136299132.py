import bisect
import sys
import math

verbose = False


def get_iv():
    args = sys.stdin.readline()
    argv = args.split()
    iargv = [int(arg) for arg in argv]
    return iargv


def get_fv():
    args = sys.stdin.readline()
    argv = args.split()
    iargv = [float(arg) for arg in argv]
    return iargv


def calc_dist(Lhs, Rhs):
    dist = 0
    for off in range(len(Lhs)):
        dx = Lhs[off] - Rhs[off]
        dist += dx * dx
    dist = math.sqrt(dist)
    return dist


def is_int(fl):
    ifl = int(fl + .5)
    df = abs(ifl - fl)
    return df < 1e-4


def num_sqare(N, X):
    rv = 0
    for i in range(N):
        for j in range(i + 1, N):
            dist = calc_dist(X[i], X[j])
            if is_int(dist):
                rv += 1
    return rv


def main():
    specs = get_iv()
    N = specs[0]
    D = specs[1]
    X = []
    for i in range(N):
        v = get_iv()
        X.append(v)
    rv = num_sqare(N, X)
    print(rv)


if __name__ == '__main__':
    main()
    # mock()