import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    T, A = 1, 1
    for _ in range(N):
        Ti, Ai = read_ints()
        # T  A   T    A
        # Ti Ai  Ti*x Ai*x
        #
        # Ti*x >= T, Ai*x >= A, min x?
        # x >= T/Ti
        # x >= A/Ai
        if T%Ti == 0:
            x0 = T//Ti
        else:
            x0 = T//Ti+1
        if A%Ai == 0:
            x1 = A//Ai
        else:
            x1 = A//Ai+1
        x = max(x0, x1)
        T, A = Ti*x, Ai*x
    return T+A


if __name__ == '__main__':
    print(solve())
