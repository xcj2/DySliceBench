# coding: utf-8
import array, bisect, collections, heapq, itertools, math, random, re, string, sys, time

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7


def II(): return int(input())
def ILI(): return list(map(int, input().split()))
def IAI(LINE): return [ILI() for __ in range(LINE)]
def IDI(): return {key: value for key, value in ILI()}


def solve(N, W, w_v):
    memo = collections.defaultdict(int)
    memo[0] = 0
    for w, v in w_v:
        for w_memo, v_memo in sorted(list(memo.items()), key=lambda x: -x[0]):
            if w + w_memo > W:
                continue
            if memo[w + w_memo] < v_memo + v:
                memo[w + w_memo] = v_memo + v

    return max(memo.values())


def main():
    N, W = ILI()
    w_v = IAI(N)
    print(solve(N, W, w_v))


if __name__ == "__main__":
    main()
