from collections import deque
import sys
sys.setrecursionlimit(100000)

class Node():
    def __init__(self, p=None, l=None, r=None):
        self.parent = p
        self.left = l
        self.right = r
        self.depth = None

n = int(input())
nodes = [Node() for i in range(n)]
for i in range(n):
    id, k, *c = list(map(int, input().split(' ')))
    if k == 0: continue
    nodes[id].left = c[0]
    nodes[c[0]].parent = id
    for j in range(1, k):
        nodes[c[j-1]].right = c[j]
        nodes[c[j]].parent = id

root = None
for i in range(n):
    if nodes[i].parent == None:
        root = i

def get_childs(i):
    if nodes[i].left == None: return []
    j = 0
    childs = [nodes[i].left]
    while nodes[childs[j]].right != None:
        childs.append(nodes[childs[j]].right)
        j += 1
    return childs

# 再帰だと segmentation faultが発生する
# while で実装

def set_depth(s):
    nodes[s].depth = 0
    queue = deque([s])
    while len(queue) > 0:
        u = queue.popleft()
        par_depth = nodes[u].depth
        next_child = nodes[u].left
        while next_child != None:
            nodes[next_child].depth = par_depth + 1
            queue.append(next_child)
            next_child = nodes[next_child].right

set_depth(root)

for i in range(n):
    nodetype = 'internal node'
    childs = get_childs(i)
    if childs == []:
        nodetype = 'leaf'
    parent = nodes[i].parent
    if parent == None:
        parent = -1
        nodetype = 'root'
    print('node ' + str(i) + ': parent = ' + str(parent) + ', depth = ' + str(nodes[i].depth) + ', ' + nodetype + ', ' + str(childs))

