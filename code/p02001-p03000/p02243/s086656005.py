from heapq import heappush, heappop
import sys
INFTY=sys.maxsize

def readinput():
    n=int(input())
    nList=[]
    for _ in range(n):
        nList.append([])
    for _ in range(n):
        l=list(map(int,input().split()))
        i=l[0]
        k=l[1]
        for j in range(k):
            v=l[2+j*2]
            c=l[2+j*2+1]
            nList[i].append([v,c])
    return n,nList

def dijkstra(s,n,nList):
    WHITE=0
    GRAY=1
    BLACK=2
    color=[WHITE]*n
    d=[INFTY]*n

    HQ=[]

    d[s]=0
    heappush(HQ,(d[s],s))

    while(len(HQ)>0):
        du,u=heappop(HQ)
        color[u]=BLACK

        if d[u]<du:
            continue

        for (v,vw) in nList[u]:
            if color[v]!=BLACK:
                if d[u] + vw < d[v]:
                    d[v] = d[u] + vw
                    color[v]=GRAY
                    heappush(HQ, (d[v], v))
    return d


def main(n,nList):
    d=dijkstra(0,n,nList)    
    for i in range(n):
        print('{} {}'.format(i,d[i]))

    return

if __name__=='__main__':
    n,nList=readinput()
    main(n,nList)

        
