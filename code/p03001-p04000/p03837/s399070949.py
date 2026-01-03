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
    inf=10**9
    n,m=MI()
    dist=[[inf]*n for _ in range(n)]
    abc=[]
    for _ in range(m):
        a,b,c=MI()
        a,b=a-1,b-1
        abc.append((a,b,c))
        dist[a][b]=dist[b][a]=c
    for i in range(n):dist[i][i]=0
    for j in range(n):
        for i in range(n):
            for k in range(n):
                dist[i][k]=dist[k][i]=min(dist[i][k],dist[i][j]+dist[j][k])
    ans=0
    for a,b,c in abc:
        if dist[a][b]<c:ans+=1
    print(ans)

main()