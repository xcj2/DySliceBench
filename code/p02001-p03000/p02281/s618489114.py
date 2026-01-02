class node:
    parent = None
    depth = 0
    degree = 0
    height = 0

    def __init__(self, no, l, r,sib):
        self.no = no
        self.left = l
        self.right = r
        self.sibling = sib
    
    def setsibdepth(self, nodes, d):
        if self.left is None:
            return
        self.depth = d
        self.left.sibling = self.right
        self.right.sibling = self.left
        self.left.setsibdepth(nodes, d+1)
        self.right.setsibdepth(nodes, d+1)

    def setheight(self, nodes, h):
        if self.left is None:
            return h-1
        return max(self.left.setheight(nodes, h+1), self.right.setheight(nodes, h+1))


def preorder(head, h, A):
    if h.left is None:
        return
    A.append(h.no)
    preorder(head, h.left, A)
    preorder(head, h.right, A)
    if head == h:
        print('', *A)

def inorder(head, h, B):
    if h.left is None:
        return
    inorder(head, h.left, B)
    B.append(h.no)
    inorder(head, h.right, B)
    if head == h:
        print('', *B)

def postorder(head, h, C):
    if h.left is None:
        return
    postorder(head, h.left, C)
    postorder(head, h.right, C)
    C.append(h.no)
    if head == h:
        print('', *C)

#葉はNULL, 根の親はNone

NULL = node(-1, None, None, None)
head = None
nodes = []
n = int(input())
for i in range(n):
    temp = node(i, None, None, NULL)
    nodes.append(temp)

for i in range(n):
    temp = list(map(int,input().split()))
    if temp[1] == -1:
        nodes[temp[0]].left = NULL
    else:
        nodes[temp[0]].left = nodes[temp[1]]
        nodes[nodes[temp[0]].left.no].parent = nodes[temp[0]]

    if temp[2] == -1:
        nodes[temp[0]].right = NULL
    else:
        nodes[temp[0]].right = nodes[temp[2]]
        nodes[nodes[temp[0]].right.no].parent = nodes[temp[0]]

    if temp[1] == -1 and temp[2] == -1:
        nodes[temp[0]].degree = 0
    elif temp[1] != -1 and temp[2] != -1:
        nodes[temp[0]].degree = 2
    else:
        nodes[temp[0]].degree = 1

for i in range(n):
    if nodes[i].parent is None:
        head = nodes[i]
        break

head.setsibdepth(nodes, 0)

for i in range(n):
    nodes[i].height = nodes[i].setheight(nodes, 0)

A = []
B = []
C = []
print("Preorder")
preorder(head, head, A)
print("Inorder")
inorder(head, head, B)
print("Postorder")
postorder(head, head, C)
