class Node:
    def __init__(self, num, parent, children):
        self.id = num
        self.parent = -1
        self.depth = 0
        self.type = None
        self.children = children
          
    def show(self):
        print('node {0}: parent = {1}, depth = {2}, {3}, {4}'.format(self.id,self.parent,self.depth,self.type,self.children))
  
  
def set_node(node_data):
    L = list(map(int, node_data.split()))
    num = L[0]
    children = L[2:]
    node = Node(num, -1, children)
    T[num] = node
    for n in children:
        T[-1] -= n
  
def set_pdt(n_i, parent, depth):
    node = T[n_i]
    node.parent = parent
    node.depth = depth
    if node.children:
        node.type = 'internal node'
        for n in node.children:
            set_pdt(n, n_i, depth + 1)
    else:
        node.type = 'leaf'
  
n = int(input())
  
T = [None] * n
  
T.append(int(n * (n - 1) / 2))
  
for i in range(n):
    x = input()
    set_node(x)
  
set_pdt(T[-1], -1, 0)
  
T[T[-1]].type ='root'
  
for n in T[:-1]:
    n.show()