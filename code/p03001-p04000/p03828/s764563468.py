import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def SI(): return input().split()

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

from math import ceil, floor, log2
from collections import deque
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product
from heapq import heapify, heappop, heappush

def solve():
    n = II()

    keta = [0] * (n+1)
    for i in range(2, n+1):
        # iを素因数分解
        for j in range(2, int(pow(i, 0.5))+1):
            if i % j: continue
            ex = 0
            while i % j == 0:
                i = i // j
                ex += 1
            keta[j] += ex
        if i != 1:
            keta[i] += 1
    # print(fact)

    mod = 1000000007
    ans = 1
    for ex in keta:
        ans = ans * (ex + 1)
        ans %= mod
    print(ans)


if __name__ == '__main__':
    solve()
