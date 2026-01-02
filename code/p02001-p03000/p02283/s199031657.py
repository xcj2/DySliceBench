
import sys

class Node:
    def __init__(self, value, p = None, l = None, r = None):
        self.key = value
        self.p = p
        self.left = l
        self.right = r

def getroot(x):
    if x.p != None:
        return getroot(x.p)
    return x

def preorder(x, A):
    if x == None:
        return
    A.append(x.key)
    preorder(x.left, A)
    preorder(x.right, A)

def inorder(x, A):
    if x == None:
        return
    inorder(x.left, A)
    A.append(x.key)
    inorder(x.right, A)

def postorder(x, A):
    if x == None:
        return
    postorder(x.left, A)
    postorder(x.right, A)
    A.append(x.key)

def ptree(root):
    pre = [""]
    ino = [""]
    preorder(root, pre)
    inorder(root, ino)
    print(" ".join(map(str,ino)))
    print(" ".join(map(str,pre)))

def insert(Tree, root, z):
    y = None # x ??????
    x = root  # 'T ??????'
    while x != None:
        y = x # ???????¨????
        if z.key < x.key:
            x = x.left # ?????????????§????
        else:
            x = x.right # ?????????????§????
    z.p = y

    Tree.append(z)
    if y == None: # T ???????????´???
        return z
    elif z.key < y.key:
        y.left = z # z ??? y ?????????????????????
    else:
        y.right = z # z ??? y ?????????????????????
    return root

def main():

    """ ????????? """
    num = int(input().strip())
    istr = sys.stdin.read()
    cmds = list(istr.splitlines())
    Tree = []
    root = None
    for i in range(num):
        cmd = cmds[i][0]
        if cmd == "i":
            n = Node(int(cmds[i][7:]))
            root = insert(Tree, root, n)
        elif cmd == "p":
            ptree(root)
    

if __name__ == '__main__':
    main()