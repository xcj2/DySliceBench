#!python3

def iim():
    return map(int, input().rstrip().split())

from math import factorial
def calc(a):
    N = len(a)
    aa = []
    bk = [factorial(i) for i in range(N-1, 0, -1)]

    bl = [0] * N
    for i in range(N-1, 0, -1):
        x = a[i]
        for j in range(i):
            if a[j] > x:
                bl[j] += 1

    n = 0
    for i in range(0, N-1):
        n += bk[i] * bl[i]

    return n

def resolve():
    N = int(input())
    P = list(iim())
    Q = list(iim())

    print(abs(calc(P) - calc(Q)))

if __name__ == "__main__":
    resolve()
