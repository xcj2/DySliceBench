# E

N=int(input())
A=list(map(int,input().split()))

def gcd(a,b):
    if a>b:
        a,b=b,a
    while a%b:
        a,b=b,(a%b)
    return b

def fast_factorization_init(N):
    res=list(range(N))
    for i in range(2,N):
        if i*i>N:
            break
        for j in range(i*i,N,i):
            if res[j]==j:
                res[j]=i
        if res[i]<i:
            continue
    return res            
    
min_factors=fast_factorization_init(10**6+10)
def fast_factorization(n):
    res=[]
    while n>1:
        res.append(min_factors[n])
        n//=min_factors[n]
    return list(set(res))

res2=0
P=[]
for i in range(N):
    if i!=0:
        res1=gcd(A[i],res1)
    else:
        res1=A[0]
    P += fast_factorization(A[i])

if len(set(P))==len(P):
    res2=1

if res2==1:
    print('pairwise coprime')
elif res1==1:
    print('setwise coprime')
else:
    print('not coprime')