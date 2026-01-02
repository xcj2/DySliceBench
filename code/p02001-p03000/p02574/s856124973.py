import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]

def make_sfp(N):
    F = [False] * (N + 1)
    P = [10 ** 7] * (N + 1)
    for i in range(2, N + 1):
        if F[i]:
            continue

        P[i] = i
        for j in range(i, N + 1, i):
            F[j] = True
            P[j] = min(P[j], i)
    return P


def dev_p(P, n):
    S = set()
    while n != 1:
        S.add(P[n])
        n //= P[n]
        
    return S


def main():
    N = int(input())
    A = read_list()
    D = dict()
    P = make_sfp(max(A))

    for a in A:
        S = dev_p(P, a)
        for s in S:
            D[s] = D.setdefault(s, 0) + 1
    
    is_pairwise = True
    for v in D.values():
        if v == N:
            print("not coprime")
            return
        elif v >= 2:
            is_pairwise = False
    
    print("pairwise coprime" if is_pairwise else "setwise coprime")
        

if __name__ == "__main__":
    main()

