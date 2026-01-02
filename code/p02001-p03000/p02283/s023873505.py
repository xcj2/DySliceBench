#!/usr/bin/env python3
import sys
n = int(input())
class Node:
  def __init__(self,v):
    self.p = None
    self.key = v
    self.left = None
    self.right = None

sys.setrecursionlimit(1500)
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

for i in range(n):
  s = input()
  if s[0]=="i":
    insert(Node(int(s.split()[1])))
  else:
    ret = []
    inorder(r)
    print(""," ".join(map(str,ret)))
    ret = []
    preorder(r)
    print(""," ".join(map(str,ret)))
