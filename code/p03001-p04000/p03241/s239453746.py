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
    N, M = MI()

    ans = 1
    for i in range(1, int(pow(M, 0.5))+1):
        if M % i: continue
        j = M // i

        if i * N <= M: ans = max(ans, i)
        if j * N <= M: ans = max(ans, j)
    print(ans)




if __name__ == '__main__':
    solve()
