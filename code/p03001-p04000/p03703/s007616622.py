#座標圧縮
#a=list
#flag=0...座圧済みa flag=1...座圧指標dict
def position_zip(a,flag):
  j=0
  d={}
  for i in sorted(a):
    if i in d:continue
    d[i]=j
    j+=1
  if flag==1:return d
  return [d[i] for i in a]

#-----BinaryIndexedTree-----(0-indexed)
#O(logN)で累積和取得と値の更新
#add(i,x)...i番目にxを加算
#sum(i,j)...[i,j]の累積和を取得
class BinaryIndexedTree:
  def __init__(self,n):
    self.bit=[0]*n
  def add(self,i,x):
    i+=1
    while i<=len(self.bit):
      self.bit[i-1]+=x
      i+=i&-i
  def sum_sub(self,i):
    a=0
    i+=1
    while i:
      a+=self.bit[i-1]
      i-=i&-i
    return a
  def sum(self,i,j):
    a=self.sum_sub(j)
    if i!=0:a-=self.sum_sub(i-1)
    return a

n,k=map(int,input().split())
a=[int(input())-k for _ in range(n)]
b=[0]
for i in a:b.append(b[-1]+i)
b=position_zip(b,0)
bit=BinaryIndexedTree(n+1)
ans=0
for i in b:
  ans+=bit.sum(0,i)
  bit.add(i,1)
print(ans)