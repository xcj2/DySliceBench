import sys
sys.setrecursionlimit(10000000)
rd = sys.stdin.buffer.read
rl = sys.stdin.buffer.readline
NIL = -1

class Node:
    def __init__(self, left, right, p):
        self.left = left
        self.right = right 
        self.p = p

n = int(input())
T = [Node(NIL, NIL, NIL) for _ in range(n)]
for _ in range(n):
    x, y, z = map(int ,input().split())
    T[x].left = y
    T[x].right = z
    if y != NIL:
        T[y].p = x
    if z != NIL:
        T[z].p = x

#rootを見つける
def searchRoot():
    for node_i in range(n):
        if T[node_i].p == NIL:
            return node_i

preorder_res = []
def preorder(node_i):
    if node_i == NIL:
        return
    preorder_res.append(node_i)
    preorder(T[node_i].left)
    preorder(T[node_i].right)

inorder_res = []
def inorder(node_i):
    if node_i == NIL:
        return
    inorder(T[node_i].left)
    inorder_res.append(node_i)
    inorder(T[node_i].right)

postorder_res = []
def postorder(node_i):
    if node_i == NIL:
        return
    postorder(T[node_i].left)
    postorder(T[node_i].right)
    postorder_res.append(node_i)

def outPut(s, array):
    n = len(array)
    print(s)
    res =' '
    for i in range(len(array)):
        if i==n-1:
            res += str(array[i])
        else:
            res += str(array[i])+' ' 
    print(res)


def main():
    s = ['Preorder', 'Inorder', 'Postorder']
    l = [preorder_res, inorder_res, postorder_res]
    root = searchRoot()
    preorder(root)
    inorder(root)
    postorder(root)

    for i, j in zip(s, l):
        outPut(i, j)
if __name__ == '__main__':
    main()
