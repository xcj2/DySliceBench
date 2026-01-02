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


def preParse(u):
    if u == -1:
        return
    print(f' {u}', end='')
    preParse(T[u].left)
    preParse(T[u].right)

def inParse(u):
    if u == -1:
        return
    inParse(T[u].left)
    print(f' {u}', end='')
    inParse(T[u].right)

def postParse(u):
    if u == -1:
        return
    postParse(T[u].left)
    postParse(T[u].right)
    print(f' {u}', end='')


for i in range(n):
    if T[i].parent == -1:
        print('Preorder')
        preParse(i)
        print()
        print('Inorder')
        inParse(i)
        print()
        print('Postorder')
        postParse(i)
        print()
        break
