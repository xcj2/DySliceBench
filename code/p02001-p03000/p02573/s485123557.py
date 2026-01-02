# unionfind:連結成分が欲しい場合などに使用
import sys
sys.setrecursionlimit(10**9)

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
    siz_list[par_x]+= siz_list[par_y]
def is_same(x,y):
  return get_par(x) == get_par(y)

N,M=map(int,input().split())

par_list = list(range(N+1))
siz_list = [1]*(N+1)

# ここでmergeを繰り返すした後、馴らす
for _ in range(M):
  A,B=map(int,input().split())
  merge(A,B)

for i in range(1,N+1):
  par_list[i]=get_par(i)
  siz_list[i]=siz_list[par_list[i]]
#print(par_list,siz_list)

print(max(siz_list))