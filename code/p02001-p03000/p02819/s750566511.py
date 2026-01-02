import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**5)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    x = gete(int)
    MAX_I = 100005
    p = [True] * MAX_I
    p[0], p[1] = False, False

    for i in range(2, MAX_I):
        if p[i]:
            for j in range(2 * i, MAX_I, i):
                p[j] = False

    for i in range(x, MAX_I):
        if p[i]:
            print(i)
            break


if __name__ == "__main__":
    main()