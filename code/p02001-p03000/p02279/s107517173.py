NIL = -1


class Node():
  def __init__(self, nid):
    self.nid = nid
    self.parent = -1
    self.left = self.right = None
    self.depth = None

  def __str__(self):

    template = "node {}: parent = {}, depth = {}, {}, {}"
    if self.parent == -1:
      ntype = "root"
    elif self.left is None:
      ntype = "leaf"
    else:
      ntype = "internal node"

    children = self.get_childs()
    chidlren = ", ".join(map(str,children))
    parend_id = self.parent.nid if self.parent != -1 else -1
    return template.format(
      self.nid, parend_id, self.depth, ntype, children
    )
  
  def get_childs(self):
    c = self.left
    children = []
    while c is not None:
      children.append(c.nid)
      c = c.right
    return children
  
      


def set_depth(node, p):
  node.depth = p
  if node.right is not None:
    set_depth(node.right, p)
  if node.left is not None:
    set_depth(node.left, p+1)

def main():
  n = int(input())
  T = [Node(i) for i in range(n)]
  for i in range(n):
    tmp = list(map(int, input().split()))
    nid = tmp[0]
    k = tmp[1]
    c = tmp[2:]
    if len(c) == 0:
      continue
    T[nid].left = T[c[0]]
    for idx in c:
      T[idx].parent = T[nid]
    for j in range(k-1):
      T[c[j]].right = T[c[j+1]]
  for i in range(n):
    if T[i].parent == -1:
      break
  set_depth(T[i], 0)
  for x in T:
    print(x)



if __name__ == "__main__":
    import io, sys
    sys.setrecursionlimit(200000)
    main()
