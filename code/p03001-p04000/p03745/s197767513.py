# coding: utf-8
import array, bisect, collections, heapq, itertools, math, random, re, string, sys, time
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
 
 
def II(): return int(input())
def ILI(): return list(map(int, input().split()))
def IAI(LINE): return [ILI() for __ in range(LINE)]
def IDI(): return {key: value for key, value in ILI()}
 
 
def solve(N, A):
    flag = 0
    ans = 1
    for i in range(N - 1):
        if A[i] < A[i + 1]:
            if flag == -1:
                ans += 1
                flag = 0
            else:
                flag = 1

        if A[i] > A[i + 1]:
            if flag == 1:
                ans += 1
                flag = 0
            else:
                flag = -1

    return ans


def main():
    N = II()
    A = ILI()
    print(solve(N, A))
 
 
if __name__ == "__main__":
    main()
