from collections import Counter,defaultdict,deque
import sys,bisect,math,itertools,string,queue,copy
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
def sortx(x,n,k):
    if k == 0:x.sort(key=lambda y:y[1,n])
    else:x.sort(reversed=True, key=lambda y:y[1,n])
def graph():
    n,m=inpm()
    g=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=inpm()
        a-=1
        b-=1
        g[a].append(b)
        #g[b].append(a)
    return n,m,g

def main():
    n,m=inpm()
    py=[]
    num=[1 for _ in range(n)]
    for i in range(m):
        p,y=inpm()
        py.append([y,p,i])
    py.sort()
    ans=[]
    for i in range(m):
        ID_head=list(str(py[i][1]))
        ID_back=list(str(num[py[i][1]-1]))
        num[py[i][1]-1]+=1
        if len(ID_head)<6:
            ID_head=['0' for _ in range(6-len(ID_head))] + ID_head
        if len(ID_back)<6:
            ID_back=['0' for _ in range(6-len(ID_back))] + ID_back
        ID=ID_head+ID_back
        ans.append( [ py[i][2] , ID ] )
    ans.sort()
    for i in range(m):
        print(''.join(ans[i][1]))
        
if __name__ == "__main__":
    main()
