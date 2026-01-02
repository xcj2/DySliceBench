import sys
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(200000)
N,u,v=map(int,input().split())
s=[[]for i in range(N)]
for i in range(N-1):
    A,B=map(lambda x: int(x)-1,input().split())
    s[A].append(B)
    s[B].append(A)
a=[None]*N
t=[None]*N
t[u-1]=0
a[v-1]=0
def hu(n,c):
    for i in s[n]:
        if a[i]==None:
            a[i]=c
            hu(i,c+1)
hu(v-1,1)
A=0
k=a[u-1]
def hu2(n,c):
    global k
    for i in s[n]:
        if t[i]==None and c<a[i]:
            t[i]=c
            if k<a[i]:
                k=a[i]
            hu2(i,c+1)
hu2(u-1,1)
print(k-1)