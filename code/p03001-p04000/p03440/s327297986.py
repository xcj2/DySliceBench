from collections import*
from heapq import*
def main():
  n,m,*a=map(int,open(0).read().split())
  table=[-1]*n
  def root(x):
    while table[x]>=0:x=table[x]
    return x
  def unite(x,y):
    s1=root(x)
    s2=root(y)
    if s1!=s2:
      if table[s1]>table[s2]:s1,s2=s2,s1
      table[s1]+=table[s2]
      table[s2]=s1
  d=defaultdict(list)
  for x,y in zip(*[iter(a[n:])]*2):unite(x,y)
  for i,v in enumerate(a[:n]):d[root(i)]+=v,
  if len(d)<2:
    print(0)
    return
  *d,=map(sorted,d.values())
  c=sum(heappop(t)for t in d)
  l=[]
  for t in d:l+=t
  i=len(d)-2
  if len(l)<i:
    print('Impossible')
  else:
    print(c+sum(sorted(l)[:i]))
main()