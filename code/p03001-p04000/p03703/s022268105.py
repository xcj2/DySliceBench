def add(B,a,n):
    x = a
    while x<=n:
        B[x]+=1
        x+=x&(-x)
        
def sums(B,a):
    x=a
    S=0
    while x!=0:
        S+=B[x]
        x-=x&(-x)
    return S
  
def invnumber(n,A):
  S=[0]*n
  A=sorted([(A[i],i) for i in range(n)])
  for i in range(1,n):
     S[A[i][1]]=i
  B=[0]*(n*2+1)
  invs=0
  for i in range(n):
      s=S[i]+n
      invs+=sums(B,s)
      add(B,s,n*2)
  return invs
N,K=map(int,input().split())     
A=[int(input())-K for i in range(N)]
T=[0]
for i in range(N):
  T.append(T[-1]+A[i])

print(invnumber(N+1,T))
  
  