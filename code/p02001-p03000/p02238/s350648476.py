n = int(input())

class Node:
    def __init__(self, idd, neighbors):
        self.idd = idd
        self.neighbors = neighbors
        self.foundAt = 0
        self.completeAt = 0
        
    def __repr__(self):
        return "{0} {1} {2}".format(self.idd, self.foundAt, self.completeAt)

Nodes = [None] * n
for i in range(n):
    row = [int(tt) for tt in input().split()]
    Nodes[row[0]-1] = Node(row[0], [ row[j + 2] for j in range(row[1])])
        
def depthSearch(Nodes):
    stack = [Nodes[0]]
    
    time = 2
    current = stack[-1]
    current.foundAt = 1
    while len(stack) > 0 or any([node.foundAt==0 for node in Nodes]):
        if(len(stack)==0):
            newStart = [node for node in Nodes if node.foundAt==0][0]
            newStart.foundAt = time
            stack.append(newStart)
            time += 1
        current = stack[-1]
        if(len(current.neighbors) > 0):
            next_n = Nodes[current.neighbors.pop(0)-1]
            if(next_n.foundAt != 0):
                continue
            next_n.foundAt = time
            stack.append(next_n)
        else:
            current.completeAt = time
            stack.pop(-1)
        time += 1
    return Nodes
Nodes = depthSearch(Nodes)
for node in Nodes:
    print(node)
