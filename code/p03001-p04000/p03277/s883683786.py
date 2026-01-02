N=int(input())
A=[int(i) for i in input().split()]
sorted_A=sorted(A)

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
  B=[0]*(n*2+1)
  invs=0
  for i in range(n):
      s=A[i]+n
      invs+=sums(B,s)
      add(B,s,n*2)
  return n*(n-1)//2-invs
  
def Check(x):
  S=[0]
  for i in range(N):
    if A[i]>sorted_A[x]:
      S.append(S[-1]+1)
    else:
      S.append(S[-1]-1)
  return invnumber(N+1,S)
      
l,r=0,N-1
while l<r:
  m=(l+r)//2
  if Check(m)>N*(N+1)//4:
    r=m
  else:
    l=m+1
print(sorted_A[l])
