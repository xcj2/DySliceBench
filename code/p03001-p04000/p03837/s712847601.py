from collections import Counter,defaultdict,deque
import sys
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
    
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])

def warshall_floyd(): # 全点対最短路問題O(N^3)
    n,w = inpm() #n:頂点数　w:辺の数
    d = [[10**10 for i in range(n)] for i in range(n)] 
    #d[u][v] : 辺uvのコスト(存在しないときはinf)
    xyz=[]
    for i in range(w):
        x,y,z = inpm()
        x -= 1
        y -= 1
        xyz.append((x,y,z))
        d[x][y] = z
        d[y][x] = z
    for i in range(n):
        d[i][i] = 0 #自身のところに行くコストは0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return n,w,d,xyz

def main():
    n,w,d,edge=warshall_floyd()
    cnt=0
    for i in range(w):
        flag = False
        x=edge[i][0]
        y=edge[i][1]
        z=edge[i][2]
        for j in range(n):
            if d[j][x] + z == d[j][y]:
                flag = True
                break
            if d[j][y] + z == d[j][x]:
                flag = True
                break
        if not flag:
            cnt+=1
    print(cnt)





if __name__ == "__main__":
    main()