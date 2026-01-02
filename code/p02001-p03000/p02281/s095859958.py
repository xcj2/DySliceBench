class Tree:
  def __init__(self):
    self.parent = -1
    self.brother = -1
    self.lchild = -1
    self.rchild = -1

n = int(input())

A = [Tree() for _ in range(n)]

for i in range(n):
  id, *children = [int(x) for x in input().split()]
  A[id].lchild, A[id].rchild = children
  if A[id].lchild != -1 and A[id].rchild != -1:
    A[A[id].lchild].brother = A[id].rchild
  for child in children:
    if child != -1:
      A[child].parent = id

root = [i for i, x in enumerate(A) if x.parent == -1][0]

def preorder(A,C,a):
  C.append(a)
  F = []
  if A[a].lchild != -1:
    preorder(A,C,A[a].lchild)
    if A[a].rchild != -1:
      F.append(A[a].rchild)
  elif A[a].rchild != -1:
    preorder(A,C,A[a].rchild)
  elif A[a].brother != -1:
    preorder(A,C,A[a].brother)
  while F != []:
    f = F.pop()
    if not f in C:
      preorder(A,C,f)
  return C

def start(A,a):
  global b
  b = A[a].lchild
  if b != -1:
    start(A,b)
  else:
    b = a
  return b

def inorder(A,D,a):
  if A[a].lchild == -1:
    D.append(a)
    if A[a].rchild != -1:
      inorder(A,D,start(A,A[a].rchild))
  if A[a].parent != -1:
    c = A[a].parent
    if a == A[c].lchild and A[c].rchild != -1:
      D.append(c)
      inorder(A,D,start(A,A[c].rchild))
    elif a == A[c].lchild and A[c].rchild == -1:
      D.append(c)
      inorder(A,D,c)
    elif a == A[c].rchild and A[c].lchild != -1:
      inorder(A,D,c)

def postorder(A,E,a,e):
  if A[a].lchild == -1 and A[a].rchild != -1:
    postorder(A,E,start(A,A[a].rchild),A[a].rchild)
  E.append(a)
  if a != e:
    if A[a].brother != -1:
      postorder(A,E,start(A,A[a].brother),e)
    else:
      postorder(A,E,A[a].parent,e)

C = []
D = []
E = []

print("Preorder")
print(" ",end="")
print(" ".join(map(str, preorder(A,C,root))))
print("Inorder")
print(" ",end="")
s = start(A,root)
inorder(A,D,s)
print(" ".join(map(str, D)))
print("Postorder")
print(" ",end="")
postorder(A,E,s,root)
print(" ".join(map(str, E)))
