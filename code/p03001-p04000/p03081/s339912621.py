import sys
n,q=map(int,input().split())
s=input()
l=[[i for i in l.split()] for l in sys.stdin]
def right_fallen(x):
  stack=x
  for i in range(q):
    if stack==n:
      return True
    if stack==-1:
      return False
    if l[i][0]==s[stack]:
      if l[i][1]=='R':
        stack+=1
      else:
        stack-=1
  if stack==n:
    return True
  return False
def left_fallen(x):
  stack=x
  for i in range(q):
    if stack==n:
      return False
    if stack==-1:
      return True
    if l[i][0]==s[stack]:
      if l[i][1]=='R':
        stack+=1
      else:
        stack-=1
  if stack==-1:
    return True
  return False
def binary_search():
  ok=n
  ng=-1
  while(abs(ok-ng)>1):
    mid=(ok+ng)//2
    if right_fallen(mid):
      ok=mid
    else:
      ng=mid
  return ok
def binary_search2():
  ok=-1
  ng=n
  while(abs(ok-ng)>1):
    mid=(ok+ng)//2
    if left_fallen(mid):
      ok=mid
    else:
      ng=mid
  return ok
print(binary_search()-binary_search2()-1)