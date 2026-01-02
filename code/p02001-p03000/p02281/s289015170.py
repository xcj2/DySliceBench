class Node:
    def __init__(self, idn):
        self.id = idn
        self.left = -1
        self.right = -1
        self.parent = -1

n = int(input())
T = [Node(i) for i in range(n)]
for ni in range(n):
    idn, left, right = [int(i) for i in input().split()]
    T[idn].left = left
    T[idn].right = right
    if left != -1:
        T[left].parent = idn
    if right != -1:
        T[right].parent = idn

i = 0
while T[i].parent != -1:
    i = T[i].parent
root = i

orderList = []
def setPreorderList(p):
    orderList.append(T[p].id)
    if T[p].left != -1:
        setPreorderList(T[p].left)
    if T[p].right != -1:
        setPreorderList(T[p].right)

setPreorderList(root)
print("Preorder")
print("",*orderList)

orderList = []
def setInorderList(p):
    if T[p].left != -1:
        setInorderList(T[p].left)
    orderList.append(T[p].id)
    if T[p].right != -1:
        setInorderList(T[p].right)

setInorderList(root)
print("Inorder")
print("",*orderList)

orderList = []
def setPostorderList(p):
    if T[p].left != -1:
        setPostorderList(T[p].left)
    if T[p].right != -1:
        setPostorderList(T[p].right)
    orderList.append(T[p].id)

setPostorderList(root)
print("Postorder")
print("",*orderList)
    
