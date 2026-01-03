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
    A, B = ILI()
    return (A, B)


def solve(A, B):
    if A + B >= 10:
        ans = "error"
    else:
        ans = A + B
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
