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

N,M=map(int,input().split())
plist=list(map(int,input().split()))
#print(plist)

par_list=list(range(N+1))
for i in range(M):
  x,y=map(int,input().split())
  merge(x,y)
#print(par_list)

index_dic={}
comp_list=[]
for i in range(1,N+1):
  par=get_par(par_list[i])
  comp_list.append(par)
  if par in index_dic:
    index_dic[par].append(i)
  else:
    index_dic[par]=[i]
#print(comp_list)
#print(index_dic)

answer=0
for par,vlist in index_dic.items():
  v2set=set()
  for v in vlist:
    v2set.add(plist[v-1])
      
  #print(vlist)
  #print(v2set)
  for v in vlist:
    if v in v2set:
      answer+=1
      
print(answer)