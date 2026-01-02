import sys
sys.setrecursionlimit(10**6)

def get_par(x):
  if x == par_list[x]:
    return x
  else:
    par_list[x] = get_par(par_list[x])
    return par_list[x]

def merge(x,y):
  par_x = get_par(x)
  par_y = get_par(y)
  if par_x != par_y:
    par_list[par_y] = par_x

def is_same(x,y):
  return get_par(x) == get_par(y)

N=int(input())
if N<=2:
  print(1)
  sys.exit(0)

xylist=[]
for i in range(N):
  x,y=map(int,input().split())
  xylist.append((x,y))
xylist.sort()
#print(xylist)

pqset=set()
for i in range(N):
  x1,y1=xylist[i]
  for j in range(i+1,N):
    x2,y2=xylist[j]
    p=x2-x1
    q=y2-y1
    pqset.add((p,q))
#print(len(pqset))
    
answer=50
for p,q in pqset:
  par_list=list(range(N))
  for i in range(N):
    x1,y1=xylist[i]
    for j in range(i+1,N):
      x2,y2=xylist[j]
      if p==x2-x1 and q==y2-y1:
        merge(i,j)
        
  comp_set=set()
  for i in range(N):
    comp_set.add(get_par(i))
  answer=min(answer,len(comp_set))
    
print(answer)