class BIT():
  def __init__(self,n):# 0-indexed
    self.n=n
    self.bit=[0]*(n+1)
  def add(self,i,x):
    i+=1
    while i<=self.n:
      self.bit[i]+=x
      i+=i&-i
  def _sum(self,i):
    s=0
    while i>0:
      s+=self.bit[i]
      i-=i&-i
    return s
  def get(self,i,j):# get sum between [i,j)
    return self._sum(j)-self._sum(i)
n,k=map(int,input().split())
a=[int(input()) for i in range(n)]
cumsum_a=[0]*(n+1)
for i in range(n):
  cumsum_a[i+1]=cumsum_a[i]+a[i]
for i in range(n+1):
  cumsum_a[i]-=k*i
  
def compress(list1):
  list2=sorted(set(list1))
  memo={value:index for index,value in enumerate(list2)}
  for i in range(len(list1)):
    list1[i]=memo[list1[i]]
  return list1
cumsum_a=compress(cumsum_a)
bit=BIT(n+1)
ans=0
for i in range(n+1):
  ans+=bit.get(0,cumsum_a[i]+1)
  bit.add(cumsum_a[i],1)
print(ans)