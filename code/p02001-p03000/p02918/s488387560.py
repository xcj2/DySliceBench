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

def rle(lst):
    res = []
    pre, cnt = lst[0], 1
    for i in range(1, len(lst)):
        if lst[i] == pre:
            cnt += 1
        else:
            res.append((pre, cnt))
            pre = lst[i]
            cnt = 1
    res.append((pre, cnt))
    return res

def solve():
    n, k = MI()
    S = list(input())

    R = rle(S)

    score = 0
    for r in R:
        score += r[1] - 1

    l = len(R)
    for _ in range(k):
        if l > 2:
            score += 2
            l -= 2
        elif l == 2:
            score += 1
            l -= 1
        else:
            break
    print(score)






if __name__ == '__main__':
    solve()
