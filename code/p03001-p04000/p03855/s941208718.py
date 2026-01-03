from collections import Counter
def find(x):
  if x==Tree[x]:
      return x
  else:
      Tree[x]=find(Tree[x])
      return Tree[x]
def unite(x,y):
  s1=find(x)
  s2=find(y)
  if s1!=s2:
    Tree[s2]=s1
def find2(x):
  if x==Tree2[x]:
      return x
  else:
      Tree2[x]=find2(Tree2[x])
      return Tree2[x]
def unite2(x,y):
  s1=find2(x)
  s2=find2(y)
  if s1!=s2:
    Tree2[s2]=s1
N,K,L=map(int,input().split())
Tree=[i for i in range(N)]
Tree2=[i for i in range(N)]
ans=[]
for i in range(K):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  unite(a,b)
for i in range(L):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  unite2(a,b)
l=[(find(i),find2(i)) for i in range(N)]
lc=Counter(l)
for i in range(N):
  ans.append(lc[l[i]])
print(" ".join(map(str,ans)))