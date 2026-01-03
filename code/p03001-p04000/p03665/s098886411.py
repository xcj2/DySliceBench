# coding: utf-8
import array, bisect, collections, copy, heapq, itertools, math, random, re, string, sys, time

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7


def II(): return int(input())
def ILI(): return list(map(int, input().split()))
def IAI(LINE): return [ILI() for __ in range(LINE)]
def IDI(): return {key: value for key, value in ILI()}


def read():
    N, P = ILI()
    A = ILI()
    return N, P, A


def nCr(n, r):
    if r == 0:
        return 1

    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def solve(N, P, A):
    n_even = 0
    n_odd = 0
    for a in A:
        if a % 2 == 1:
            n_odd += 1
        else:
            n_even += 1

    ans = 0
    if P == 0:
        sum_even = 2 ** n_even
        n_odd_div = n_odd // 2
        sum_odd = 0
        for i in range(0, n_odd_div + 1):
            sum_odd += nCr(n_odd, i * 2)
        ans = sum_even * sum_odd

    elif P == 1:
        if n_odd == 0:
            ans = 0
        else:
            sum_even = 2 ** n_even
            n_odd_div = n_odd // 2
            sum_odd = 0
            for i in range(n_odd_div):
                sum_odd += nCr(n_odd, i * 2 + 1)
            ans = sum_even * sum_odd

    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
