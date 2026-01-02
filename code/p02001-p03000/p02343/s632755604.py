



class Node:
    def __init__(self, num):
        self.num = num
        self.parent = self
        self.rank = 0
    
def findSet(node):
    tmp = []
    while node.parent != node:
        tmp.append(node)
        node = node.parent
    
    while tmp:
        tmp.pop().parent = node
    return node

def unite(x, y):
    node1 = findSet(nodes[x])
    node2 = findSet(nodes[y])
    if node1.rank == node2.rank:
        node2.parent = node1
        node1.rank += 1
    elif node1.rank > node2.rank:
        node2.parent = node1
    else:
        node1.parent = node2

def same(x, y):
    node1 = findSet(nodes[x])
    node2 = findSet(nodes[y])
    return node1.parent == node2.parent

nums=list(map(int,input().split()))
n = nums[0]
q = nums[1]

nodes = []
for i in range(n):
    nodes.append(Node(i))

for i in range(q):
    nums=list(map(int,input().split()))
    if nums[0] == 0:
        unite(nums[1], nums[2])
    else:
        if same(nums[1], nums[2]):
            print(1)
        else:
            print(0)
        








