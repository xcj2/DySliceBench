# modulo:mod

# inverse x^(-1)
def inv(x):
    global mod
    return pow(x,mod-2,mod)

# factorial x!
def fact(x):
    global mod
    res=1
    for i in range(2,x+1):
        res=res*i%mod
    return res

# combination nCr
def combi(n,r):
    if r<0 or r>n:
        return 0
    else:
        return fact(n)*inv(fact(r))*inv(fact(n-r))%mod

mod=10**9+7

N,K=map(int,input().split())
A=[-10**10] # 1-ind
A.extend(list(map(int,input().split())))
A.sort()

# print(A)

ans=0
# min
p=1
for i in range(N-K+1,0,-1):
    # print(i,A[i],p)
    temp=A[i]*p%mod    
    ans=(ans-temp)%mod
    # print((N-i+1)*inv(N-K-i+2))
    p=p*(N-i+1)*inv(N-K-i+2)%mod
# max
p=1
for j in range(K,N+1):
    # print(j,A[j],p)
    temp=A[j]*p%mod
    ans=(ans+temp)%mod
    p=p*j*inv(j-K+1)%mod

print(ans)