from collections import defaultdict as dd
dicLeft = dd(lambda: -1)
dicRight = dd(lambda: -1)
dicParent = dd(lambda: -1)

n = int(input())
for i in range(n):
  id, left, right = map(int, input().split())
  dicLeft[id] = left
  dicRight[id] = right
  dicParent[left] = id
  dicParent[right] = id

def depth(dicPar, id):
  if dicPar[id] == -1:
    return 0
  else:
    return depth(dicPar, dicPar[id]) + 1

def height(dicLeft, dicRight, id):
  left = dicLeft[id]
  right = dicRight[id]
  if left == -1 and right == -1:
    return 0
  elif left == -1:
    return height(dicLeft, dicRight, right) + 1
  elif right == -1:
    return height(dicLeft, dicRight, left) + 1
  else:
    return max(height(dicLeft, dicRight, left), height(dicLeft, dicRight, right)) + 1

def degree(dicLeft, dicRight, id):
  counter = 0
  if dicLeft[id] != -1:
    counter += 1
  if dicRight[id] != -1:
    counter += 1
  return counter

def sibling(dicParent, dicLeft, dicRight, id):
  parent = dicParent[id]
  if parent == -1:
    return -1
  else:
    if dicLeft[parent] == id:
      return dicRight[parent]
    elif dicRight[parent] == id:
      return dicLeft[parent]

def nodeType(dicPar, dicLeft, dicRight, id):
  if dicPar[id] == -1:
    return "root"
  elif dicLeft[id] == -1 and dicRight[id] == -1:
    return "leaf"
  else:
    return "internal node"

#print(depth(dicPar, 1))
for id in range(n):
  print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(id, dicParent[id], sibling(dicParent, dicLeft, dicRight, id), degree(dicLeft, dicRight, id), depth(dicParent, id), height(dicLeft, dicRight, id), nodeType(dicParent, dicLeft, dicRight, id)))
