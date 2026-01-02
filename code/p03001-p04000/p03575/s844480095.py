N,M=map(int,input().split())

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

ablist=[]
for i in range(M):
  a,b=map(int,input().split())
  ablist.append((a,b))
#print(ablist)

answer=0
for i in range(M):
  par_list = list(range(N+1))
  for j in range(M):
    if i==j:
      continue
    a,b=ablist[j]
    merge(a,b)

  comp_set=set()
  for i in range(1,N+1):
    comp_set.add(get_par(i))
  
  if len(comp_set)>1:
    answer+=1
  
print(answer)
