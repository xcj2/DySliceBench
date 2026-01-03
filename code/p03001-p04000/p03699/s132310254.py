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
    s = [II() for __ in range(N)]
    return (N, s)


def solve(N, s):
    n_sum = sum(s)
    s_sorted = sorted(s)
    if n_sum % 10 != 0:
        ans = n_sum
    else:
        for n in s_sorted:
            if (n_sum - n) % 10 != 0:
                ans = n_sum - n
                break
        else:
            ans = 0

    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
