import sys
n = int(input())
class Node:
  def __init__(self):
    self.p = -1 # parent
    self.l = -1 # left most child
    self.r = -1 # right sibling

T = [Node() for _ in range(n)]
sys.setrecursionlimit(1500)

for i in range(n):
    v,l,r = map(int,input().split())
    T[v].r = r
    if r != -1:
      T[r].p = v
    T[v].l = l
    if l != -1:
      T[l].p = v

for i in range(n):
  #print(i,T[i].p,T[i].l,T[i].r)
  if T[i].p == -1 : r = i

ret = []
def preorder(v):
  if v == -1: return
  ret.append(v)
  preorder(T[v].l)
  preorder(T[v].r)

def inorder(v):
  if v == -1: return
  inorder(T[v].l)
  ret.append(v)
  inorder(T[v].r)

def postorder(v):
  if v == -1: return
  postorder(T[v].l)
  postorder(T[v].r)
  ret.append(v)

ret = []
preorder(r)
print("Preorder")
print(""," ".join(map(str,ret)))
ret = []
inorder(r)
print("Inorder")
print(""," ".join(map(str,ret)))
ret = []
postorder(r)
print("Postorder")
print(""," ".join(map(str,ret)))


