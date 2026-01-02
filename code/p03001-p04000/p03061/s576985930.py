from math import sqrt
from sys import exit
N=int(input())
A=list(map(int,input().split()))

if len(A)==2:
    print(max(A))
    exit()

def gcd(a,b):
    if a<b: a,b=b,a
    if a%b==0: return b
    return gcd(b,a%b)
    
g=gcd(A[0],A[-1])

p=[]

for i in range(1,int(sqrt(g)+1)):
    if g%i==0:
        if i*i==g: p.append(i)
        else: p+=[i,g//i]
        
def ok(n):
    f=False
    for a in A[1:-1]:
        if a%n:
            if f: return False
            f=True
    return True
    
def GCD(L):
    if len(L)==1: return L[0]
    ans=gcd(L[0],L[1])
    if len(L)>2:
        for l in L[2:]:
            ans=gcd(ans,l)
    return ans

p.sort(reverse=True)
for num in p:
    if ok(num):
        ans=num
        break
p1=GCD(A[1:-1])
print(max([ans,gcd(p1,A[0]),gcd(p1,A[-1])]))
