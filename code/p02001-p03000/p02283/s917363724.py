import copy
class Node():
    def __init__(self, parent = -1, left = -1, right = -1):
        self.parent = parent
        self.left = left
        self.right = right
        
    def __eq__(self, other):
        if self.num == other.num:
            return True
        else:
            return False

def insert(node, z):
    global root
    p = -1
    x = root
    while x != -1:
        p = x
        if z < x:
            x = node[x].left
        else:
            x = node[x].right
    
    if p == -1:
        root = z
        node[z] = Node()
    elif z < p:
        node[p].left = z
        node[z] = Node(p)
    else:
        node[p].right = z
        node[z] = Node(p)
        
def preorder(node, i):
    print(" " + str(i), end ="")
    if node[i].left != -1:
        preorder(node, node[i].left)
    if node[i].right != -1:
        preorder(node, node[i].right)

def inorder(node, i):
    if node[i].left != -1:
        inorder(node, node[i].left)
    print(" " + str(i), end ="")
    if node[i].right != -1:
        inorder(node, node[i].right)
        
n = int(input())
node = {}
root = -1
for i in range(n):
    s = input()
    if s == "print":
        inorder(node, root)
        print()
        preorder(node, root)
        print()
    else:
        s = s.split()
        insert(node, int(s[1]))

