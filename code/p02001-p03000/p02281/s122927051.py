import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
P = [-1]*n
C = [[] for i in range(n)]
Pre, In, Post = [], [], []

for i in range(n):
  s = [int(i) for i in input().split()]
  id = s[0]
  l = s[1]
  r = s[2]
  C[id] = (l,r)
  if l != -1:
    P[l] = id
  if r != -1:
    P[r] = id

for i in range(n):
  if P[i] == -1:
    root = i

def Prewalk(x):
  Pre.append(x)
  l,r = C[x]
  if l == -1 and r == -1:
    return
  if l != -1:
    Prewalk(l)
  if r != -1:
    Prewalk(r)
  
def Inwalk(x):
  l,r = C[x]
  if l == -1 and r == -1:
    In.append(x)
    return
  if l != -1:
    Inwalk(l)
  In.append(x)
  if r != -1:
    Inwalk(r)
  
def Postwalk(x):
  l,r = C[x]
  if l == -1 and r == -1:
    Post.append(x)
    return
  if l != -1:
    Postwalk(l)
  if r != -1:
    Postwalk(r)
  Post.append(x)
  
Prewalk(root)
Inwalk(root)
Postwalk(root)

print("Preorder")
print(" "+" ".join(map(str, Pre)))
print("Inorder")
print(" "+" ".join(map(str, In)))
print("Postorder")
print(" "+" ".join(map(str, Post)))
