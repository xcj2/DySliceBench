import sys

def readinput():
    n=int(input())
    nMat=[]
    for _ in range(n):
        m=list(map(int,input().split()))
        nMat.append(m)
    
    return n,nMat

WHITE=0
GRAY=1
BLACK=2
INFTY=sys.maxsize
def prim(n,nMat):

    color=[WHITE]*n
    d=[INFTY]*n
    p=[-1]*n

    d[0]=0
    p[0]=-1

    while True:
        mincost=INFTY
        for i in range(n):
            if color[i]!=BLACK and d[i] < mincost:
                mincost=d[i]
                u=i

        if mincost==INFTY:
            break

        # Tに属する頂点とV-Tに属する頂点をつなぐ辺の中で最小のコストのもの(u,p[u])が選ばれた
        color[u]=BLACK

        # V-Tに属する各頂点vとTに属する頂点をつなぐ辺の中で最小のコストのものが(v,p[v])でそのコストがd[v]
        # uがTに入ったことで辺(u,v)のコストとd[v]を比べてd[v]が大きかったらp[v]=u, d[v]=辺(u,v)のコストで更新
        for v in range(n):
            if color[v]!=BLACK and nMat[u][v]!=-1:
                if nMat[u][v]<d[v]:
                    d[v]=nMat[u][v]
                    p[v]=u
                    color[v]=GRAY
    return p,d


def main(n,nMat):
    p,d=prim(n,nMat)
    
    ans=0
    for i in range(n):
        if p[i] != -1:
            ans+=d[i]
    
    return ans

if __name__=='__main__':
    n,nMat=readinput()
    ans=main(n,nMat)
    print(ans)

