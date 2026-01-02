a,b=map(int,input().split())
def gcd(a,b):
    if b==0:
        return a 
    return gcd(b,a%b)
g=gcd(a,b)

from math import sqrt as S
#print(gcd(a,b))
def get_div(x):
    if x==1:
        return [1]
    div=[1,x]
    for i in range(2,int(S(x))+1):
        if x%i==0:
            div.append(i)
            if i!=x//i:
                div.append(x//i)
    return div 
div=get_div(g)
p=10**6+5 
def sieve():
    l=[1]*p 
    i=2 
    while i*i<=p:
        if l[i]:
            for j in range(i*i,p,i):
                l[j]=0 
        i+=1 
    l[0]=0 
    return l 
isp=sieve()
cnt=0 
def pr(n):
    if n<=1:
        return 0 
    return all(n%i for i in range(2,int(S(n))+1))
for i in div:
    if i<=10**6:
        if isp[i]:
            cnt+=1 
    else:
        if pr(i):
            cnt+=1 
print(cnt)