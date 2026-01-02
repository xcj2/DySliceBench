import sys
n = int(input())
class Node:
  def __init__(self,v):
    self.p = None
    self.key = v
    self.left = None
    self.right = None

sys.setrecursionlimit(15000)
r = None
def insert(z):
  global r
  y = None
  x = r
  while x != None:
    y = x
    if z.key < x.key:
      x = x.left
    else:
      x = x.right
  z.p = y

  if y == None:
    r = z
  elif z.key < y.key:
    y.left = z
  else:
    y.right = z

ret = []
def inorder(r):
  if r == None: return
  inorder(r.left)
  ret.append(r.key)
  inorder(r.right)

def preorder(r):
  if r == None: return
  ret.append(r.key)
  preorder(r.left)
  preorder(r.right)

def search(r,key):
  if r == None: return None
  if r.key == key:
    return r
  if r.key < key:
    return search(r.right,key)
  else:
    return search(r.left,key)

def delete(key):
  global r
  z = search(r,key)
  if not z.left or not z.right:
    y = z # node to delete
  else:
    y = z.right
    while y.left:
      y = y.left

  if y.left:
    x = y.left # child node of delete node
  else:
    x = y.right

  if x:
    x.p = y.p

  if y.p == None:
    r = x
  elif y == y.p.left:
    y.p.left = x
  else:
    y.p.right = x

  if y != z:
    z.key = y.key

for i in range(n):
  s = input()
  #print(s)
  if s[0]=="i":
    insert(Node(int(s.split()[1])))
  elif s[0]=="f":
    if search(r,int(s.split()[1])) != None:
      print("yes")
    else:
      print("no")
  elif s[0]=="d":
    #print("d",int(s.split()[1]))
    #print(r.key)
    delete(int(s.split()[1]))
  else:
    #print("p")
    ret = []
    inorder(r)
    print(""," ".join(map(str,ret)))
    ret = []
    preorder(r)
    print(""," ".join(map(str,ret)))

