# Ýć x^n
def pow(x,n):
    global p
    res=1
    prod=x
    while n>0:
        if n%2==1:
            res=(res*prod)%p
        prod=(prod*prod)%p
        n//=2
    return res

# t x^(-1)
def inv(x):
    global p
    res=1
    prod=x
    e=p-2
    while e>0:
        if e%2==1:
            res=(res*prod)%p
        prod=(prod*prod)%p
        e//=2
    return res

# Kć x!
def fact(x):
    if x<1:
        return 1
    global p
    res=1
    for i in range(2, x+1):
        res=(res*i)%p
    return res
    
# gš nCr
def combi(n,r):
    if r<0 or r>n:
        return 0
    else:
        a=fact(n)
        b=inv(fact(r))
        c=inv(fact(n-r))
        return(((a*b)%p)*c)%p

p=10**9+7
X,Y=map(int,input().split())
if (X+Y)%3!=0 or 2*X<Y or 2*Y<X:
    ans=0
else:
    a=(2*X-Y)//3
    b=(-X+2*Y)//3
    ans=combi(a+b,a)
print(ans)