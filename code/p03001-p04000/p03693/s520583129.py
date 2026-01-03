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
    r, g, b = ILI()
    return (r, g, b)


def solve(r, g, b):
    num = r * 100 + g * 10 + b
    num_div = num % 4
    if num_div == 0:
        ans = "YES"
    else:
        ans = "NO"
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
