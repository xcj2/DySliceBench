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
   
N, M = LI()
mat = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = LI_()
    mat[a][b] = 1
    mat[b][a] = 1 
seen = [0 for _ in range(N)]
ans = 0

def dfs(i, count):
    global ans
    import pdb
    # pdb.set_trace()
    if count == N:
        return True

    for j, reachable in enumerate(mat[i]):
        if reachable and not seen[j]:
            seen[j] = 1
            if dfs(j, count + 1):
                ans += 1
            seen[j] = 0

    return False

def main():
    seen[0] = 1
    dfs(0, 1)
    print(ans)
main()

