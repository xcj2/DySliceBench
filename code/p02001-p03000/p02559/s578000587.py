from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
J=10**19
###############################################################################\n=17
n,q=INPUT()
A=INPUT()
T=[0]*(n+1)
def update(i,x):
    while(i<=n):
        T[i]+=x
        i+=i&(-i)
def query(i):
    ans=0
    while(i>0):
        ans+=T[i]
        i-=i&(-i)
    return ans
for i in range(n):
    update(i+1,A[i])
#print(*T)

for _ in range(q):
    s,l,r=INPUT()
    if s==0:
        update(l+1,r)
    else:
        print(query(r)-query(l))
    #print()
