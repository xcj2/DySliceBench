import sys, math
from collections import defaultdict
from itertools import product
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    A = list(mi())

    stock = 0
    money = 1000

    u = []
    d = []

    i = 0
    while i < N-1:
        if A[i] <= A[i+1]:
            tmp = i
            while i+1 < N and A[i] <= A[i+1]:
                i += 1
            u.append((tmp, i))
        else:
            i += 1

    for v in u:
        stock += money//A[v[0]]
        money -= A[v[0]] * (money//A[v[0]])

        money += A[v[1]] * stock
        stock = 0

    print(money)

if __name__ == '__main__':
    main()