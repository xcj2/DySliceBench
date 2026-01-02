from heapq import heappush, heappop
import sys
INFTY=sys.maxsize

def readinput():
    n,x,y=list(map(int,input().split()))
    return n,x,y

def dijkstra(s,n,nList):
    '''優先度付きキューを使用したダイクストラ法

    パラメーター
    s: 始点
    n: 頂点の数
    nList: [ 
        [vertex1, cost1], [vertex2, cost2], ...
        [vertex1, cost1], [vertex2, cost2], ...
        ...
    ]

    返り値
    d: 始点sから各頂点vまでの最短経路上の辺の重みの総和d[v]のリスト
    '''

    WHITE=0
    GRAY=1
    BLACK=2
    color=[WHITE]*n
    d=[INFTY]*n

    HQ=[]

    d[s]=0
    heappush(HQ,(d[s],s))

    while(len(HQ)>0):
        #print(HQ)
        du,u=heappop(HQ)
        color[u]=BLACK

        if d[u]<du:
            continue

        for v in nList[u]:
            vw=1
            if color[v]!=BLACK:
                if d[u] + vw < d[v]:
                    d[v] = d[u] + vw
                    color[v]=GRAY
                    heappush(HQ, (d[v], v))
    return d

def main(n,x,y):
    nList=[]
    #nList.append([])
    nList.append([1])
    for i in range(1,n-1):
        nList.append([i-1,i+1])
    nList.append([n-2])
    nList[x-1].append(y-1)
    nList[y-1].append(x-1)
    #print(nList)

    dList=[]
    for i in range(n):
        dList.append(dijkstra(i,n,nList))
    #print(dList)
    
    hist=[0]*n
    for i in range(n-1):
        for j in range(i+1,n):
            hist[dList[i][j]]+=1
    
    for i in range(1,n):
        print(hist[i])


if __name__=='__main__':
    n,x,y=readinput()
    main(n,x,y)
