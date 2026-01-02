from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
###############################################################################\
def power(a,p,m):
    if m==0:
        return 0
    res=1
    while(p>0):
        if p&1:
            res=(res*a)%m
        a=(a*a)%m
        p//=2
    return res%m
n=int(input())
s=input()
A=list(int(i) for i in s)
R=[]
for i in range(n-1,-1,-1):
    R.append(A[i])
one=0
for e in A:
    if e==1:
        one+=1
max=one+1
min=one-1
ansmax=0
ansmin=0
#print(one)
for i in range(n):
    ansmax=(ansmax+power(2,i,max)*(R[i]))%max
    if min!=0:
        ansmin=(ansmin+power(2,i,min)*R[i])%min
def popcount(z):
    ans=0
    while(z!=0):
        if z%2==1:
            ans+=1
        z//=2
    return ans
#print(ansmax,ansmin)
B=[]
for i in range(n):
    if R[i]==1:
        if min!=0:
            r=(ansmin-power(2,i,min))%min
            count=1
            while(r!=0):
                count+=1
                r=r%popcount(r)
        else:
            count=0
        B.append(count)
    else:
        r=(ansmax+power(2,i,max))%max
        count=1
        while(r!=0):
            count+=1
            r=r%popcount(r)
        B.append(count)
B.reverse()
for ele in B:
    print(ele)
