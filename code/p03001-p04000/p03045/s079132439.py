class Node:
    def __init__(self, val):
        self.num = val
        self.val = val
        self.is_parent = True
        self.parent = None
        self.childs = []

    def show(self):
        print(self.num, end=" ")
        print(self.is_parent, end=" ")
        for child in self.childs:
            print(child.num, end=" ")

def root(node):
    depth = 0
    while node.parent != None:
        node = node.parent
        depth += 1
    return node, depth

N, M = map(int, input().split())

roots = [Node(i) for i in range(N)]
count = N

for i in range(M):
    x, y, z = map(int, input().split())
    x = roots[x-1]
    y = roots[y-1]
    if x.is_parent and y.is_parent:
            y.is_parent = False
            y.parent = x
            count -= 1
            x.childs.append(y)
    else:
        root_x, depth_x = root(x)
        root_y, depth_y = root(y)
        if root_x != root_y:
            if depth_x >= depth_y:
                root_y.is_parent = False
                root_y.parent = root_x
                count -= 1
                root_x.childs.append(root_y)
            else:
                root_x.is_parent = False
                root_x.parent = root_y
                count -= 1
                root_y.childs.append(root_x)

print(count)