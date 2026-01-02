class STNode:
    def __init__(self, k, l, r):
        self.key = k
        self.left = l
        self.right = r

def STinsert(h, z):
    p = None
    while True:
        if h.key == -1:
            break
        p = h
        if z.key < h.key:
            h = h.left
        else:
            h = h.right
    if z.key < p.key:
        p.left = z
    else:
        p.right = z

def preorder(head, h, A):
    if h.key == -1:
        return
    A.append(h.key)
    preorder(head, h.left, A)
    preorder(head, h.right, A)
    if head == h:
        print('', *A)

def inorder(head, h, B):
    if h.key == -1:
        return
    inorder(head, h.left, B)
    B.append(h.key)
    inorder(head, h.right, B)
    if head == h:
        print('', *B)

n = int(input())
NULLnode = STNode(-1, None, None)

first = list(input().split())
head = STNode(int(first[1]), NULLnode, NULLnode)
for i in range(n-1):
    temp = list(input().split())
    if temp[0] == "insert":
        z = STNode(int(temp[1]), NULLnode, NULLnode)
        STinsert(head, z)
    else:
        A = []
        B = []
        inorder(head, head, B)
        preorder(head, head, A)
