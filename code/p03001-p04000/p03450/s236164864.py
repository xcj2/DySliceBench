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
    N, M = LI()
    if M == 0:
        print("Yes")
        return

    G = [[] for _ in range(N)]
    for i in range(M):
        l, r, d = LI()
        l -= 1
        r -= 1
        G[l].append((r, d))
        G[r].append((l, -d))
    val = [inf] * N
    global_visited = set()

    def bfs(ini):
        flag = True
        q = deque([ini])
        visited = set()
        visited.add(ini)
        while q:
            v = q.popleft()
            for next_v, d in G[v]:
                if next_v in visited:
                    if val[next_v] == val[v] + d:
                        continue
                    else:
                        return False
                val[next_v] = val[v] + d
                visited.add(next_v)
                global_visited.add(next_v)
                q.append(next_v)
        return True

    can = True
    for i in range(N):
        if i in global_visited:
            continue
        v = i
        val[v] = 0
        if not bfs(v):
            can = False
            break

    if can:
        print("Yes")
    else:
        print("No")
    return


main()


