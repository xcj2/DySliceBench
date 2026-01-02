n = int(input())

class Node:
    def __init__(self, idd, neighbors):
        self.idd = idd
        self.neighbors = neighbors
        self.dist = -1
        
    def __repr__(self):
        return "{0} {1}".format(self.idd, self.dist)
    
def breadthFirstSearch(Nodes):
    stack = [Nodes[0]]
    Nodes[0].dist = 0
    while len(stack) > 0:
        current = stack.pop(0)
        for v in current.neighbors:
            v_node = Nodes[v-1]
#             print('current:{}, v_node:{}'.format(current, v_node))
            if(v_node.dist == -1):
                v_node.dist = current.dist + 1
                stack.append(v_node)
            else:
                v_node.dist = v_node.dist if v_node.dist < current.dist + 1 else current.dist + 1
    return Nodes

Nodes = [None] * n
for i in range(n):
    row = [int(tt) for tt in input().split()]
    Nodes[row[0]-1] = Node(row[0], [ row[j + 2] for j in range(row[1])])

Nodes = breadthFirstSearch(Nodes)
for node in Nodes:
    print(node)
