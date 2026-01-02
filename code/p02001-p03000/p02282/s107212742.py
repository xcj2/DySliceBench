# coding: utf-8
# Your code here!

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = -1
        self.left = -1
        self.right = -1
        
N = int(input())
nodes = [Node(i+1) for i in range(N)]

preorders = [int(i)-1 for i in input().split()]
inorders = [int(i)-1 for i in input().split()]


def dfs(nodes, preo, ino):
    if not preo:
        return

    root = preo[0]
    i = ino.index(root)
    
    if i != 0:
        nodes[root].left = preo[1]
        nodes[preo[1]].parent = root
        dfs(nodes, preo[1:i+1], ino[:i])
    
    if i != len(ino)-1:
        nodes[root].right = preo[i+1]
        nodes[preo[i+1]].parent = root
        dfs(nodes, preo[i+1:], ino[i+1:])
    

def postorder(nodes, root, result):
    node = nodes[root]
    if node.left != -1:
        postorder(nodes, node.left, result)
    if node.right != -1:
        postorder(nodes, node.right, result)
    result.append(root+1)


dfs(nodes, preorders, inorders)

result = []
postorder(nodes, preorders[0], result)

print(*result)
