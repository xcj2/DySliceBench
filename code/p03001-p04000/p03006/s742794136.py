import sys
import re
sys.setrecursionlimit(10 ** 7)


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def SI(): return input()


def main():
    N = int(input())
    X = []
    A = {(0, 0): 0}
    for _ in range(N):
        x, y = LI()
        X.append((x, y))
    for i in range(N):
        for j in range(i+1, N):
            x, y = X[i]
            xi, yi = X[j]
            dx = x-xi
            dy = y-yi
            if (dx, dy) in A:
                A[(dx, dy)] += 1
            else:
                A[(dx, dy)] = 1
            if (-dx, -dy) in A:
                A[(-dx, -dy)] += 1
            else:
                A[(-dx, -dy)] = 1
    print(N-max(A.values()))


main()
