
import sys

YES = "yes"
NO = "no"

class Node:
    def __init__(self, value, p = None, l = None, r = None):
        self.key = value
        self.p = p
        self.left = l
        self.right = r

def chgchild(parent, old, new = None):
    if parent == None:
        return
    else:
#        print("\tparent:{}".format(parent.key))
        if parent.left == old:
            parent.left = new
        else:
            parent.right = new
        if new != None:
            new.p = parent

def delete(node):
    if node == None:
        return
#    print("\tdel key:{}".format(node.key))
    if node.left == None:
        chgchild(node.p, node, node.right)
    elif node.right == None:
        chgchild(node.p, node, node.left)
    else:
        ino = []
        inorder(node,ino)
        next = 0
        for i in range(len(ino)):
            if ino[i].key == node.key:
                next = i + 1
                break
        node.key = ino[next].key
        delete(ino[next])

def getroot(x):
    if x.p != None:
        return getroot(x.p)
    return x

def keylist(A):
    B = []
    for i in A:
        B.append(i.key)
    return B

def preorder(x, A):
    if x == None:
        return
    A.append(x)
    preorder(x.left, A)
    preorder(x.right, A)

def inorder(x, A):
    if x == None:
        return
    inorder(x.left, A)
    A.append(x)
    inorder(x.right, A)

def postorder(x, A):
    if x == None:
        return
    postorder(x.left, A)
    postorder(x.right, A)
    A.append(x)

def ptree(root):
    pre = []
    ino = []
    preorder(root, pre)
    inorder(root, ino)
    ap = keylist(pre)
    ip = keylist(ino)
    print(" {}".format(" ".join(map(str,ip))))
    print(" {}".format(" ".join(map(str,ap))))

def find(value, root):
    if root == None:
        return None
    elif value < root.key:
        return find(value,root.left)
    elif value > root.key:
        return find(value,root.right)
    return root

def insert(root, z):
    y = None # x ??????
    x = root  # 'T ??????'
    while x != None:
        y = x # ???????¨????
        if z.key < x.key:
            x = x.left # ?????????????§????
        else:
            x = x.right # ?????????????§????
    z.p = y

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
    root = None
    for i in range(num):
        cmd = cmds[i][0]
        if cmd == "i":
            n = Node(int(cmds[i][7:]))
            root = insert(root, n)
        elif cmd == "f":
            if find(int(cmds[i][5:]),root) == None:
                print(NO)
            else:
                print(YES)
        elif cmd == "p":
            ptree(root)
        elif cmd == "d":
            node = find(int(cmds[i][7:]),root)
            delete(node)

 

if __name__ == '__main__':
    main()