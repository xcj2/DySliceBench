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
    n=inp()
    a=inplm(n)
    a.sort()
    n1 = 0
    n2 = 0
    minus = n//2

    for i in range(n):
        if i<minus-1:
            n1-=2*a[i]
        elif i==minus-1:
            n1-=(1+n%2)*a[i]
        elif i==minus:
            n1+=a[i]
        elif i==minus+1 and n%2==1:
            n1+=a[i]
        else:
            n1+=2*a[i]

    a.reverse()
    plus = n//2
    for i in range(n):
        if i<plus-1:
            n2+=2*a[i]
        elif i==plus-1:
            n2+=(1+n%2)*a[i]
        elif i==plus:
            n2-=a[i]
        elif i==plus+1 and n%2==1:
            n2-=a[i]
        else:
            n2-=2*a[i]

    print(max(n1,n2))

if __name__ == "__main__":
    main()