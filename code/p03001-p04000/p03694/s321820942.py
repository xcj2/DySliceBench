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
    N = II()
    a = ILI()
    return (N, a)


def solve(N, a):
    num_min = min(a)
    num_max = max(a)
    ans = num_max - num_min
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
