import bisect
import math
from collections import deque

def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))

INF = 1 << 29


def main():
    N,X,Y = isRaw()
    Es = [[1]]+[[n-1,n+1] for n in range(1,N-1)]+[[N-2]]
    Es[X-1].append(Y-1)
    Es[Y-1].append(X-1)
    def shortest(n):
        qu = deque()
        visited = [0]*N
        qu.append(n)
        visited[n]=1
        path =[INF]*N
        path[n]=0
        while len(qu)!=0:
            m = qu.popleft()
            for l in Es[m]:
                if visited[l]!=0:
                    continue
                path[l] = min(path[m]+1,path[l])
                visited[l]=1
                qu.append(l)
        return path
    shortests = [shortest(n) for n in range(N)]
    npathes = [0 for i in range(N-1)]
    for n in range(N):
        for m in range(n+1,N):
            npathes[shortests[n][m]-1]+=1
    return "\n".join([str(a) for a in npathes])

if __name__ == "__main__":
    print(main())
