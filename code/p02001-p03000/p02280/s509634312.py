import sys
n = int(input())
class Node:
  def __init__(self):
    self.p = -1 # parent
    self.l = -1 # left most child
    self.r = -1 # right sibling

T = [Node() for _ in range(n)]
D = [0]*n
sys.setrecursionlimit(1500)
def rec(u,p):
  D[u] = p
  if T[u].r != -1: rec(T[u].r,p+1)
  if T[u].l != -1: rec(T[u].l,p+1)

H = [0]*n
def rec1(u):
  r = l = 0
  if T[u].r != -1: r = rec1(T[u].r)+1
  if T[u].l != -1: l = rec1(T[u].l)+1
  H[u] = max(r,l)
  return H[u]
def sib(n):
  if T[n].p == -1:
    return -1
  if T[T[n].p].l == n:
    return T[T[n].p].r
  if T[T[n].p].r == n:
    return T[T[n].p].l
for i in range(n):
    v,l,r = map(int,input().split())
    T[v].r = r
    if r != -1:
      T[r].p = v
    T[v].l = l
    if l != -1:
      T[l].p = v
    #print(v,T[v].p,T[v].l,T[v].r)
#print("a1")
for i in range(n):
  #print(i,T[i].p,T[i].l,T[i].r)
  if T[i].p == -1 : r = i
#print("a2")
rec(r,0)
rec1(r)
#print("a3")
for i in range(n):
  #print(i,T[i].p,T[i].l,T[i].r)
  d = 0
  if T[i].l != -1:
    d += 1
  if T[i].r != -1:
    d += 1  
  if T[i].p == -1:
    kind = "root"
  elif d == 0: kind = "leaf"
  else: kind = "internal node"
  print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}"
        .format(i,T[i].p,sib(i),d,D[i],H[i],kind))
