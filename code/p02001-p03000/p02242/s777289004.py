import sys

INFTY=sys.maxsize
WHITE=0
GRAY=1
BLACK=2

def readinput():
    n=int(input())
    nMap=[]
    for _ in range(n):
        nMap.append([INFTY]*n)

    for _i in range(n):
        l=list(map(int,input().split()))
        i=l[0]
        for jj in range(l[1]):
            j=l[2+jj*2]
            w=l[2+jj*2+1]
            nMap[i][j]=w
    return n, nMap

color=[]
d=[]
p=[]

def dijkstra(s,n,nMap):
    global color
    global d
    global p
    
    color=[WHITE]*n
    d=[INFTY]*n
    p=[-1]*n

    d[s]=0
    p[s]=-1

    while True:
        mincost=INFTY
        for i in range(n):
            if color[i]!=BLACK and d[i] < mincost:
                mincost=d[i]
                u=i
        if mincost==INFTY:
            break
        color[u]=BLACK

        for v in range(n):
            if color[v]!=BLACK and nMap[u][v]!=INFTY:
                if d[u]+nMap[u][v] < d[v]:
                    d[v]=d[u]+nMap[u][v]
                    p[v]=u
                    color[v]=GRAY

def main(n,nMap):

    dijkstra(0,n,nMap)
    for i in range(n):
        print('{} {}'.format(i,d[i]))

if __name__=='__main__':
    n,nMap=readinput()
    main(n,nMap)
    



