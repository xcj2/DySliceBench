from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n,x,y=MI()
    to=[[] for _ in range(n)]
    for i in range(n-1):
        to[i].append(i+1)
        to[i+1].append(i)
    to[x-1].append(y-1)
    to[y-1].append(x-1)
    ans=[0]*n
    for i in range(n):
        q=deque()
        q.append(i)
        dist=[-1]*n
        dist[i]=0
        while q:
            u=q.popleft()
            for v in to[u]:
                if dist[v]!=-1:continue
                dist[v]=dist[u]+1
                ans[dist[v]]+=1
                q.append(v)
    for a in ans[1:]:
        print(a//2)

main()