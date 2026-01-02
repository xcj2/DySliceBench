import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N = I()
    A = sorted(LI())
    B = sorted(LI())
    C = sorted(LI())
    cnt = 0
    B_lt_A = [0] * N
    C_lt_B = [0] * N

    b_ix = 0
    for a_ix, a in enumerate(A):
        while b_ix < N and a >= B[b_ix]:
            b_ix += 1
        B_lt_A[a_ix] = N - b_ix

    c_ix = 0
    for b_ix, b in enumerate(B):
        while c_ix < N and b >= C[c_ix]:
            c_ix += 1
        C_lt_B[b_ix] = N - c_ix
    cumsum = [0] * (N+1)
    for i in range(N):
        cumsum[i+1] = cumsum[i] + C_lt_B[i]

    for i in range(N):
        B_lt_A[i] = N - B_lt_A[i]
    for c_ix in B_lt_A:
        cnt += (cumsum[-1] - cumsum[c_ix])

    print(cnt)
main()

