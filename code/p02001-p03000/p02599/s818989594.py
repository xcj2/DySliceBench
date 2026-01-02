import sys
input=sys.stdin.readline
from operator import itemgetter
n,q=map(int,input().split())
c=list(map(int,input().split()))
l=[list(map(int,input().split())) for i in range(q)]
for i in range(q):
  l[i].append(i)
l.sort(key=itemgetter(1))

L=[-1]*(5*10**5+1)

class Bit:
  def __init__(self,n):
    self.size=n
    self.tree=[0]*(n + 1)
    self.depth=n.bit_length()

  def sum(self,i):
    s=0
    while i>0:
      s+=self.tree[i]
      i-=i&-i
    return s

  def add(self,i,x):
    while i<=self.size:
      self.tree[i]+=x
      i+=i&-i

BIT=Bit(n+1)

ans=[0]*q
ct=0
for i in range(q):
  while ct<=l[i][1]:
    if L[c[ct-1]-1]!=-1:
      BIT.add(L[c[ct-1]-1],-1)
    L[c[ct-1]-1]=ct+1
    BIT.add(ct+1,1)
    ct+=1
  ans[l[i][2]]=BIT.sum(l[i][1]+1)-BIT.sum(l[i][0])

for i in range(q):
  print(ans[i])