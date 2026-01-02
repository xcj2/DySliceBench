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
    adj = []
    for i in range(N):
        adj.append(S())

    def bfs(v):
        group = [-1] * N
        q = deque([(v, 0)])
        group[v] = 0
        while q:
            cur_v, gid = q.popleft()
            for next_v in range(N):
                if adj[cur_v][next_v] == '0':
                    continue
                if group[next_v] != -1:
                    if abs(group[cur_v] - group[next_v]) > 1:
                        return -1
                    if group[cur_v] == group[next_v]:
                        return -1
                    else:
                        continue
                group[next_v] = gid + 1
                q.append((next_v, gid+1))
        return max(group) + 1

    ans = -1
    for i in range(N):
        ans = max(ans, bfs(i))

    print(ans)

main()

