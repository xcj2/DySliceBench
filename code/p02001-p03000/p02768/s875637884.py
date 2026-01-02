n,a,b=map(int,input().split())
p=1000000007
def pmod(N,K,p):
  s=1
  for i in range(K):
    s=(s*(N-i))%p
  return (s)

def bin(N):
    lists=[]
    t=0
    while N>0:
        lists.append(N%2)
        N=N//2
        t=t+1
    lists.append(t)
    return (lists)

def digb(N):
    t=0
    while N>0:
        N=N//2
        t=t+1
    return (t)

def mod(a,N,p):
    listm=[]
    for i in range(digb(N)):#2**(2**i)%pの余を記録
        listm.append(a*bin(N)[i])
        a=(a**2)%p
    s=1
    for i in range(digb(N)):
        if listm[i]!=0:
            s=(s*listm[i])%p
    return(s)

print ((mod(2,n,p)-pmod(n,a,p)*mod(pmod(a,a,p),p-2,p)-pmod(n,b,p)*mod(pmod(b,b,p),p-2,p)-1)%p)