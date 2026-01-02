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
    N, X, M = LI()
    A = [X]
    seen = set()
    seen.add(X)
    while True:
        an = A[-1]
        an1 = ((an % M) * (an % M)) % M
        if an1 in seen:
            break
        else:
            A.append(an1)
            seen.add(an1)
    start_loop_i = 0
    for i, a in enumerate(A):
        if an1 == a:
            start_loop_i = i
            break
    loop_len = len(A) - start_loop_i
    loop_sum = sum(A[start_loop_i:])

    end = False
    ans = 0
    for i in range(start_loop_i):
        N -= 1
        ans += A[i]
        if N == 0:
            end = True
            break
    if end:
        print(ans)
        return

    ans += loop_sum * (N // loop_len)
    
    if N % loop_len > 0:
        N %= loop_len
        for i in range(N):
            ans += A[start_loop_i + i]
    print(ans)






main()

