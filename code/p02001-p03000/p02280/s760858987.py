import sys

nil = -1

class Node:
    def __init__(self):
        self.parent = nil
        self.sibling = nil
        self.degree = 0
        self.left = nil
        self.right = nil
        self.depth = nil
        self.height = nil
        self.ntype = 'leaf'

def set_depth(v, depth):
    bitree[v].depth = depth

    if bitree[v].left != nil:
        set_depth(bitree[v].left, depth + 1)

    if bitree[v].right != nil:
        set_depth(bitree[v].right, depth + 1)

def get_height(v):
    h1 = 0
    h2 = 0

    if bitree[v].left != nil:
        h1 = get_height(bitree[v].left) + 1
    if bitree[v].right != nil:
        h2 = get_height(bitree[v].right) + 1

    bitree[v].height = max(h1, h2)

    return bitree[v].height

n = int(input())
bitree = [Node() for i in range(n)]
leaves = set()

for i in range(n):
    line = [int(j) for j in input().split()]
    t_id = line[0]
    bitree[t_id].left = line[1]
    bitree[t_id].right = line[2]
    bitree[t_id].degree = (line[1] != nil) + (line[2] != nil)

    if bitree[t_id].degree > 0:
        bitree[t_id].ntype = 'internal node'

        if bitree[t_id].left != nil:
            bitree[bitree[t_id].left].parent = t_id

        if bitree[t_id].right != nil:
            bitree[bitree[t_id].right].parent = t_id

        if bitree[t_id].degree == 2:
            bitree[bitree[t_id].left].sibling = bitree[t_id].right
            bitree[bitree[t_id].right].sibling = bitree[t_id].left
    else:
        leaves.add(t_id)

for t_id in range(n):
    if bitree[t_id].parent == nil:
        bitree[t_id].ntype = 'root'
        r = t_id
        break

set_depth(r, 0)

get_height(r)

for t_id in range(n):

    print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(
            t_id, bitree[t_id].parent, bitree[t_id].sibling, bitree[t_id].degree,
            bitree[t_id].depth, bitree[t_id].height, bitree[t_id].ntype))