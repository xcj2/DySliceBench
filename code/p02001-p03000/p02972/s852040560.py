from collections import Counter
N=int(input())
A=[0]+list(map(int,input().split()))

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
    
min_factors=fast_factorization_init(2*10**5+10)
def fast_factorization(n):
    res=[]
    while n>1:
        res.append(min_factors[n])
        n//=min_factors[n]
    return res

def factors(n):
    res=[1]
    for i,j in Counter(fast_factorization(n)).items():
        res+=[r*i**(b+1) for r in res for b in range(j)]
    return res

res=[0]*(N+1)
num=0
for n in reversed(range(N)):
    res[n+1]=A[n+1]
    if A[n+1]:
        num+=1
        for m in factors(n+1):
            A[m]=(A[m]+1)%2
print(num)
print(*[i+1 for i in range(N) if res[i+1]>0],sep='\n')