from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
J=int(1e9)+7

###############################################################################\n=17
def power(a,n):
    res=1
    while(n):
        if n&1:
            res=res*a
        a=a*a
        n//=2
        res%=J
        a%=J
    return res%J
s=int(input())

ans=0
def C(n,r):
    if r==0:
        return 1
    res=1
    for i in range(n,n-r,-1):
        res=(res*i)%J
    for j in range(1,r+1):
        res=(res*power(j,J-2))%J
    return res
#print(C(9,9))
ans=0
for i in range(s//3):
    ans=(ans+C(s-3*(i+1)+i,i))%J
    #print(ans)
print(ans)
