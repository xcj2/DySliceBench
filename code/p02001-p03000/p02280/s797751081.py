import sys
sys.setrecursionlimit(2 ** 20)

class Node():
    def __init__(self, parent=-1, left=-1, right=-1):
        '''
        :param parent: parent node
        :param left: left child
        :param right: right child
        '''
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return '<Node object: parent={}, left={}, right={}>' .format(self.parent, self.left, self.right)

    def get_node_type(self):
        if self.parent == -1:
            return 'root'
        elif self.left == -1 and self.right == -1:
            return 'leaf'
        else:
            return 'internal node'

    def get_degree(self):
        degree = 0
        if self.left != -1:
            degree += 1
        if self.right != -1:
            degree += 1
        return degree


def get_sibling(T, u):
    if T[u].parent == -1:
        return -1
    elif T[T[u].parent].left != u:
        return T[T[u].parent].left
    else:
        return T[T[u].parent].right

def set_depth(u, p):
    '''
    u: Node ID
    p: Initial depth
    '''
    if u == -1:
        return
    D[u] = p
    set_depth(T[u].right, p + 1)
    set_depth(T[u].left, p + 1)

def set_height(u):
    h1 = h2 = 0
    if T[u].right != -1:
        h1 = set_height(T[u].right) + 1
    if T[u].left != -1:
        h2 = set_height(T[u].left) + 1

    H[u] = max(h1, h2)
    return H[u]


n = int(input())
# initialize tree
T = [Node() for _ in range(n)]
for i in range(n):
    idx, left, right = map(int, input().split())
    T[idx].left = left
    T[idx].right = right

    # set children's parent if Node idx is not leaf
    if left != -1:
        T[left].parent = idx
    if right != -1:
        T[right].parent = idx

D = [0] * n
H = [0] * n
for i in range(n):
    if T[i].parent == -1:
        set_depth(i, 0)
        set_height(i)
        break

for i, node in enumerate(T):
    print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(
        i, node.parent, get_sibling(T, i), node.get_degree(), D[i], H[i], node.get_node_type())
    )
