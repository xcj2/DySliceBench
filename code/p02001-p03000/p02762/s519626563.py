import math
import sys
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))
mod = 10**9 + 7 
sys.setrecursionlimit(1000010)

N,M,K = nm()

# parent
# if negative, it means the node is root and the value is the size of the group. 
par=[-1] * N  

# return the root node number of the group which the node x belong to  
def find(x):  
  if par[x]<0:  # this means that node x is a root node of the group
    return x    
  else:
    par[x]=find(par[x])  # the parent nodes is expected to have root node number info.
        # if the parent node were not root node, par[x] will be update to be a root node.
        # For the next search par[x] will be the root node. 
    return par[x]

# Unite the group which node x belongs to and the group which node y belongs to 
def unite(x,y):
  x=find(x)  # x will be a root node of the original x node 
  y=find(y)  # y will be a root node of the original y node
  if x==y:   # x and y belong to the same group already, do nothing and just return False 
    return False
  else:  
    if par[x]>par[y]: # Note this is size comparison
      # Size of the group x is smaller than that of the group y, then swap x and y  
      # Note, we are using negative number 
      x,y=y,x
    par[x]+=par[y]  # the size of the group x is increased by the size of the group y 
    par[y]=x  # now the parent of the node y is set to node x.
       # At this moment, parent of other nodes which belonged to the old group y is 
       # stil node Y. However, after find() for those nodes will be update the info  
    return True

def same(x,y):
  return find(x)==find(y)

def size(x):
  return -par[find(x)]

links=[0]*N   # set to all -1. Nubmer of friend and block + 1 
F = [0]* N 
for _ in range(M):
    A,B = nm()
    unite(A-1,B-1)
    links[A-1] +=1 
    links[B-1] +=1

for _ in range(K):
    C,D = nm()
    if same(C-1,D-1):
        links[C-1]+=1
        links[D-1]+=1

for i in range(N):
    F[i] = size(i) - 1 - links[i]
print(*F)
