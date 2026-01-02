from itertools import permutations
import sys

sys.setrecursionlimit(10 ** 6)
from bisect import *
from collections import *
from heapq import *

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def SI(): return sys.stdin.readline()[:-1]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
int1 = lambda x: int(x) - 1
def MI1(): return map(int1, sys.stdin.readline().split())
def LI1(): return list(map(int1, sys.stdin.readline().split()))
p2D = lambda x: print(*x, sep="\n")
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    h,w=MI()
    ss=[[c=="#" for c in SI()] for _ in range(h)]
    dist=[[-1]*w for _ in range(h)]
    q=deque()
    q.append((0,0))
    dist[0][0]=1
    while q:
        i,j=q.popleft()
        d=dist[i][j]
        for di,dj in dij:
            ni,nj=i+di,j+dj
            if (ni,nj)==(h-1,w-1):
                ans = h * w - (d + 1) - sum(sum(row) for row in ss)
                print(ans)
                exit()
            if ni<0 or nj<0 or ni>=h or nj>=w:continue
            if dist[ni][nj]!=-1:continue
            if ss[ni][nj]:continue
            dist[ni][nj]=d+1
            q.append((ni,nj))
    print(-1)

main()
