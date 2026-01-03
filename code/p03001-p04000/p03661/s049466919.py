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
    return N, a


def solve(N, a):
    sum_a = sum(a)
    l_sum_a = [a[0]]
    for i in range(1, len(a) - 1):
        l_sum_a.append(l_sum_a[i - 1] + a[i])
    l_changed = [abs(ele * 2 - sum_a) for ele in l_sum_a]
    ans = min(l_changed)
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
