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

def fact(x):
    if x<1:
        return 1
    global p
    res=1
    for i in range(2, x+1):
        res=(res*i)%p
    return res

def combi(n,r):
    if r<0 or r>n:
        return 0
    else:
        a=fact(n)
        b=inv(fact(r))
        c=inv(fact(n-r))
        return(((a*b)%p)*c)%p

N,K=map(int,input().split())
p=1000000007

for i in range(1,K+1):
    print((combi(K-1,i-1)*combi(N-K+1,i))%p)