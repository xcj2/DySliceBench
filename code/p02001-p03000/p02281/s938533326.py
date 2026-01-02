# coding: utf-8
# Your code here!

class Node:
    def __init__(self, id):
        self.parent = -1
        self.id = id
        self.left = -1
        self.right = -1


def preorder(nodes, cur_id, result):
    node = nodes[cur_id]
    result.append(node.id)
    if node.left >= 0:
        preorder(nodes, node.left, result)
    if node.right >= 0:
        preorder(nodes, node.right, result)
    
    return


def inorder(nodes, cur_id, result):
    node = nodes[cur_id]
    if node.left >= 0:
        inorder(nodes, node.left, result)
    result.append(node.id)
    if node.right >= 0:
        inorder(nodes, node.right, result)
    
    
def postorder(nodes, cur_id, result):
    node = nodes[cur_id]
    if node.left >= 0:
        postorder(nodes, node.left, result)
    if node.right >= 0:
        postorder(nodes, node.right, result)
    result.append(node.id)


N = int(input())
nodes = [Node(i) for i in range(N)]
for i in range(N):
    id, left, right = [int(i) for i in input().split()]
    nodes[id].left, nodes[id].right = left, right
    if left >= 0:
        nodes[left].parent = id
    if right >= 0:
        nodes[right].parent = right

root = 0
for i in range(N):
    if nodes[i].parent == -1:
        root = i
        break

print('Preorder')
result = []
preorder(nodes, root, result)
print('', *result)

print('Inorder')
result = []
inorder(nodes, root, result)
print('', *result)

print('Postorder')
result = []    
postorder(nodes, root, result)
print('', *result)

