
import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
def Yes(x):print("Yes")if x==True else print("No")

D=N()
c=[0]+L()
s=[[0]*27]+[[0]+L() for i in range(D)]

dp=[]
T=[0]+LN(D)
sc=sum(c)
def point():
    ld=[0]*(27)
    score=-sc*((D+1)*D//2)
    for i in range(1,D+1):
        t=T[i]
        score+=s[i][t]+(i-ld[t])*(D-i+1)*c[t]
        ld[t]=i
    return score


m=N()
now=point()
for i in range(m):
    d,q=NM()
    old=T[d]
    T[d]=q
    new=point()
    print(new)