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


def solve():
    n = II()
    A = LI()
    box = [-1] * n
    ans = deque([])
    for i in range(n, 0, -1):
        sm = 0
        for j in range(i+i, n+1, i):
            # print(sm, box[j-1])
            sm ^= box[j-1]
        # print(A[i-1], sm)
        box[i-1] = A[i-1] ^ sm
        if box[i-1]:
            ans.appendleft(i)

    # print(box)
    print(sum(box))
    if sum(box):
        printlist(ans, ' ')

if __name__ == '__main__':
    solve()
