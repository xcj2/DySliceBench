from sys import stdin,stdout 
from bisect import bisect,bisect_left,bisect_right
def gt(): return map(int, stdin.readline().split())
def gi(): return int(stdin.readline())
def gl(): return list(map(int, stdin.readline().split())) 
def gs(): return stdin.readline()
def getmax(BITTree,i): 
    s = 0
    i = i+1
    while i > 0:
        s = max(s,BITTree[i])
        i -= i & (-i) 
    return s 

def updatebit(BITTree , n , i ,v): 
    i += 1
    while i <= n: 
        BITTree[i] = max(v,BITTree[i]) 
        i += i & (-i) 
def construct( n): 
    BITTree = [0]*(n+1) 
    # for i in range(n): 
    #     updatebit(BITTree, n, i, arr[i])
    return BITTree 
n=gi()
h=gl()
a=gl() 
m=max(h)
BITTree = construct(m+1)
for i in range(n):
    updatebit(BITTree,m+1,h[i],getmax(BITTree,h[i]-1)+a[i])
ans=0
print(getmax(BITTree,m))
    