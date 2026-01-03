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
    N, M = ILI()
    edges = IAI(M)
    return (N, M, edges)


def solve(N, M, edges):
    ans = [0] * N
    for edge in edges:
        a, b = map(lambda x: x - 1, edge)
        ans[a] += 1
        ans[b] += 1
    
    return ans


def main():
    params = read()
    ans = solve(*params)
    for i in ans:
        print(i)


if __name__ == "__main__":
    main()
