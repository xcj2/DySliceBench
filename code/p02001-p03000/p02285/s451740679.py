NIL = -1

class Node():
    def __init__(self, key):
        self.key = key
        self.right = NIL
        self.left = NIL
        self.parent = NIL

def getAncestor(t, n):
    for i in range(n):
        if t[i].parent == -1:
            return i

def preOrderWolk(t, u, load=[]):
    load.append(u.key)
    if u.left != -1:
        load = preOrderWolk(t, u.left, load)
    if u.right != -1:
        load = preOrderWolk(t, u.right, load)
    return load

def preorder(u):
    if u == NIL:
        return
    print(' ' + str(u['key']), end='')
    preorder(u['left'])
    preorder(u['right'])

def inorder(u):
    if u == NIL:
        return
    inorder(u['left'])
    print(' ' + str(u['key']), end='')
    inorder(u['right'])

def inOrderTreeWalk(t, u, load=[]):
    if u.left != -1:
        load = inOrderTreeWalk(t, u.left, load)
    load.append(u.key)
    if u.right != -1:
        load = inOrderTreeWalk(t, u.right, load)
    return load

def find(x, k):
    """[finding Node which has key k]

    Args:
        x ([root Node]): [description]
        k ([int]): [description]
    """    
    while x != -1 and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def insert(T, z):
    """[insert z to tree T]

    Args:
        T ([list]): [description]
        z ([Node class]): [Node ]
        r ([int]): [root intger]
    """
    y = NIL # x no parent
    x = T[0]
    while x != NIL and x.key != None:
        y = x
        if z.key < x.key:
            x = x.left
        elif z.key > x.key:
            x = x.right
    z.parent = y

    if y == NIL: ## T が空の場合
        T[0] = z
    elif z.key < y.key:
        T.append(z)
        y.left = z
    else:
        T.append(z)
        y.right = z

def getSuccessor(x):
    """[finding node that succes the Node]

    Args:
        x ([node]): [description]
    """
    if x.right != -1:
        return getMinimum(x.right)
    
    print('arienai')
    y = x.parent
    while y != -1 and x == y.right:
        x = y
        y = y.parent
    return y

def getMinimum(x):
    while x.left != -1:
        x = x.left
    return x

def delete(T, z):
    """[delete Node z]

    Args:
        T ([list]): [description]
        z ([node]): [node with key]
    """    
    # 削除する対象の節点をyとする
    if z.left == -1 or z.right == -1:
        y = z
    else:
        y = getSuccessor(z)

    # yの子xを決める
    if y.left != -1:
        x = y.left
    else:
        x = y.right

    if x != -1:
        x.parent = y.parent
    if y.parent == -1:
        T[0] = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    if y != z:
        z.key = y.key

import sys
T = [Node(None)]
n = int(input())
r = 0
for _ in range(n):
    in_ = sys.stdin.readline().split()
    if in_[0][0] == 'i':
        z = Node(int(in_[1]))
        insert(T, z)
    elif in_[0][0] == 'd':
        key = int(in_[1])
        x = find(T[0], key)
        delete(T, x)

    elif in_[0][0] == 'f':
        key = int(in_[1])
        x = find(T[0], key)
        if x !=  -1:
            print('yes')
        else:
            print('no')
    else:
        pre = preOrderWolk(T, T[0], [])
        in_ = inOrderTreeWalk(T, T[0], [])
        print('',*in_) #inOrder
        print('',*pre) #preOrder


