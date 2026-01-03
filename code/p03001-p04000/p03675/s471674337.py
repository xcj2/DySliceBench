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
    n = II()
    a = list(map(str, input().split()))
    return n, a


def solve(n, a):
    b = collections.deque([])
    if n % 2 == 0:
        for i, ele in enumerate(a):
            if i % 2 == 0:
                b.append(ele)
            else:
                b.appendleft(ele)
    else:
        for i, ele in enumerate(a):
            if i % 2 == 0:
                b.appendleft(ele)
            else:
                b.append(ele)

    ans = " ".join(list(b))
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
