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
     
patterns = []
def saiki(n, pat):
    if n == 0:
        patterns.append(pat)
        return
    for c in 'ABCX':
        pat += c
        saiki(n-1, pat)
        pat = pat[:-1]
def main():
    N, A, B, C = LI()
    L = []
    ans = inf
    for _ in range(N):
        L.append(I())

    saiki(len(L), '')
    for pat in patterns:
        if 'A' in pat and 'B' in pat and 'C' in pat:
            pass
        else:
            continue

        a, b, c = 0, 0, 0
        MP = 0
        for i, ch in enumerate(pat):
            if ch == 'X':
                continue

            if ch == 'A':
                if a > 0:
                    MP += 10
                a += L[i]
            if ch == 'B':
                if b > 0:
                    MP += 10
                b += L[i]
            if ch == 'C':
                if c > 0:
                    MP += 10
                c += L[i]
        tmp = min(
            abs(A-a) + abs(B-b) + abs(C-c),
            abs(A-a) + abs(B-c) + abs(C-b),
            abs(A-b) + abs(B-a) + abs(C-c),
            abs(A-b) + abs(B-c) + abs(C-a),
            abs(A-c) + abs(B-b) + abs(C-a),
            abs(A-c) + abs(B-a) + abs(C-b),
        )
        MP += tmp
        if MP < ans:
            ans_pat = pat
            ans = min(MP, ans)
    print(ans)

main()

