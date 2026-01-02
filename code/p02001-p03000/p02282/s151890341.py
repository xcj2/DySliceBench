n = int(input())
preorderList = [int(i) for i in input().split()]
inorderList = [int(i) for i in input().split()]

class Node:
    def __init__(self, idn):
        self.id = idn
        self.left = -1
        self.right = -1
T = [Node(i+1) for i in range(n)]

def splitTree(P, I):
    b = I.index(P[0])
    if P[0] != I[0]:
        T[P[0]-1].left = P[1]
    if P[0] != I[-1]:
        T[P[0]-1].right = P[b+1]
    if b > 1:
        splitTree(P[1:b+1], I[:b])
    if b < len(I)-2:
        splitTree(P[b+1:], I[b+1:])

splitTree(preorderList, inorderList)
root = preorderList[0]

postorderList = []
def setPostorderList(p):
    if T[p-1].left != -1:
        setPostorderList(T[p-1].left)
    if T[p-1].right != -1:
        setPostorderList(T[p-1].right)
    postorderList.append(T[p-1].id)

setPostorderList(root)
print(*postorderList)

