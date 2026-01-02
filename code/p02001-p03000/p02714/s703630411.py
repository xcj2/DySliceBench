def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]

# from math import comb
def comb(n,r):
    if r==2:
        return n*(n-1)//2
    else:
        return n*(n-1)*(n-2)//6
n=n0()
s=s0()
r=s.count("R")
g=s.count("G")
b=s.count("B")
ans=0
for i in range(1,(n-1)//2+1):
    for j in range(0,n-2*i):
        ans+=1
        if s[j]==s[j+i]==s[j+2*i]:
            ans-=1
        elif s[j]==s[j+i] or s[j]==s[j+2*i] or s[j+i]==s[j+2*i]:
            ans-=1
            
ans+=comb(r,3)+comb(g,3)+comb(b,3)+comb(r,2)*(g+b)+comb(g,2)*(r+b)+comb(b,2)*(r+g)
print(comb(n,3)-ans)