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
def s(): return input()

def cuts(H):
    for i in range(1<<H):
        yield bin(i)[2:].zfill(H)

def main():
    H, W, K = LI()
    S = []
    for _ in range(H):
        S.append(s())
    ans = inf
    for cut in cuts(H-1):
        p = sum([1 for x in cut if x == '1'])
        cnt = p
        lines = [[0 for _ in range(W)] for __ in range(p+1)]
        cumr = 0
        for c in range(W):
            n_line = 0
            for r in range(H):
                if S[r][c] == '1':
                    cumr += 1
                if r >= H-1:
                    continue
                if cut[r] == '1':
                    lines[n_line][c] += cumr
                    n_line += 1
                    cumr = 0
            lines[-1][c] = cumr
            cumr = 0

        ng = False
        cumsum = [[0 for _ in range(W+1)] for __ in range(p+1)]

        for i in range(p+1):
            line = lines[i]
            for j in range(W):
                cumsum[i][j+1] = line[j] + cumsum[i][j]

        before = 0
        for j in range(1, W+1):
            # import pdb
            # pdb.set_trace()
            for i in range(p+1):
                if ng:
                    break
                if cumsum[i][j] - cumsum[i][before] > K:
                    if j - before == 1:
                        ng = True
                    cnt += 1
                    before = j - 1
                    break
        if ng:
            continue
        ans = min(ans, cnt)
    print(ans)
main()

