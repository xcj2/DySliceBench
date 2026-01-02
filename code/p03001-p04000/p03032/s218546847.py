import sys
input=sys.stdin.readline
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
n,k=NM()
l=L()
ans=0
for a in range(n+1):
    for b in range(n-a+1):
        for c in range(a+1):
            for d in range(b+1):
                if a+b+c+d>k:
                    continue
                x=l[:a]
                y=l[-1:-b-1:-1]
                x.sort()
                y.sort()
                ans=max(ans,sum(x[c:])+sum(y[d:]))
print(ans)