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
    S = str(input())
    return (S,)


def solve(S):
    count = collections.Counter([char for char in S])
    for c in count.values():
        if c >= 2:
            ans = "no"
            break
    else:
        ans = "yes"
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
