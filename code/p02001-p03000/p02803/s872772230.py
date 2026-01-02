import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    inf=1000
    h,w=MI()
    ss=[[c=="#" for c in input()] for _ in range(h)]
    mx=0
    for si in range(h):
        for sj in range(w):
            if ss[si][sj]:continue
            bfs={}
            bfs[si,sj]=0
            vis=[[False]*w for _ in range(h)]
            vis[si][sj]=True
            while bfs:
                nxt={}
                for (i,j),d in bfs.items():
                    if d>mx:mx=d
                    for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                        if ni<0 or nj<0 or ni>=h or nj>=w:continue
                        if ss[ni][nj]:continue
                        if vis[ni][nj]:continue
                        vis[ni][nj]=True
                        nxt[ni,nj]=d+1
                bfs=nxt
    print(mx)

main()