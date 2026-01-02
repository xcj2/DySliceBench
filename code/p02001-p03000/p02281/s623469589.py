n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

class Node():
    def __init__(self):
        self.left = -1
        self.right = -1
        self.parent = -1
        
T = [Node() for i in range(25)]

for (idx, left, right) in A:
    T[idx].left = left
    T[idx].right = right
    if left != -1:
        T[left].parent = idx
    if right != -1:
        T[right].parent = idx

for idx in range(n):
    if T[idx].parent == -1:
        root = idx
        break
        
preorder_list = []
def preorder(u):
    preorder_list.append(str(u))
    if T[u].left != -1:
        preorder(T[u].left)
    if T[u].right != -1:
        preorder(T[u].right)
        
inorder_list = []
def inorder(u):    
    if T[u].left != -1:
        inorder(T[u].left)
    inorder_list.append(str(u))
    if T[u].right != -1:
        inorder(T[u].right)

postorder_list = []
def postorder(u):    
    if T[u].left != -1:
        postorder(T[u].left)
    if T[u].right != -1:
        postorder(T[u].right)
    postorder_list.append(str(u))
    
preorder(root)
inorder(root)
postorder(root)

print('Preorder')
print(' '+' '.join(preorder_list))
print('Inorder')
print(' '+' '.join(inorder_list))
print('Postorder')
print(' '+' '.join(postorder_list))
