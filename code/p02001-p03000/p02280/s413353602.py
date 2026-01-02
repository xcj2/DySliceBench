class NullNode():
    def __init__(self):
        self.id = -1

class Node():
    def __init__(self, id):
        self.id = id
        self.parent = NullNode()
        self.left = NullNode()
        self.right = NullNode()
        self.sibling = NullNode()

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.parent.id, self.left.id, self.right.id, self.sibling.id)

    def getHeight(self, right_height=0, left_height=0):
        if self.left.id != -1:
            left_height += 1
            left_height = self.left.getHeight(left_height, left_height)
        if self.right.id != -1:
            right_height += 1
            right_height = self.right.getHeight(right_height, right_height)
        return max(left_height, right_height)

    def getDepth(self, depth=0):
        if self.parent.id != -1:
            depth += 1
            depth = self.parent.getDepth(depth)
        return depth

    def getDegree(self):
        degree = 0
        if self.left.id != -1:
            degree += 1
        if self.right.id != -1:
            degree += 1
        return degree

    def getType(self):
        if self.parent.id == -1:
            return 'root'
        elif self.left.id == -1 and self.right.id == -1:
            return 'leaf'
        else:
            return 'internal node'

n = int(input())
node_list = [Node(id) for id in range(n)]
for i in range(n):
    [id, left, right] = [int(j) for j in input().split()]
    i_node = node_list[id]
    if left != -1:
        i_node.left = node_list[left]
        node_list[left].parent = node_list[id]
        if right != -1:
            node_list[left].sibling = node_list[right]
    if right != -1:
        i_node.right = node_list[right]
        node_list[right].parent = node_list[id]
        if left != -1:
            node_list[right].sibling = node_list[left]

for id in range(n):
    i_node = node_list[id]
    parent = i_node.parent.id
    sibling = i_node.sibling.id
    degree = i_node.getDegree()
    depth = i_node.getDepth()
    height = i_node.getHeight()
    type = i_node.getType()
    print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'.format(id, parent, sibling, degree, depth, height, type))

