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
  #print(x,y,par_list)
for i in range(1,N+1):
  par_list[i]=get_par(i)
#print(par_list)
  
answer=0
for i in range(N):
  if get_par(i+1)==get_par(plist[i]):
    answer+=1
    
print(answer)