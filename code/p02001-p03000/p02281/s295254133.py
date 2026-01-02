class Node:
    def __init__(self, parent, left, right):
        self.parent, self.left, self.right = parent, left, right

N = int(input())
T = [Node(None, None, None) for _ in range(N)]
for t in T:
    i, left, right = map(int, input().split())
    if left != -1:
        T[i].left = left
        T[left].parent = i
    if right != -1:
        T[i].right = right
        T[right].parent = i

def preorder(i):
    if i == None:
        return
    print(' {}'.format(i), end='')
    preorder(T[i].left)
    preorder(T[i].right)

def inorder(i):
    if i == None:
        return
    inorder(T[i].left)
    print(' {}'.format(i), end='')
    inorder(T[i].right)

def postorder(i):
    if i == None:
        return
    postorder(T[i].left)
    postorder(T[i].right)
    print(' {}'.format(i), end='')

root = 0
for i, t in enumerate(T):
    if t.parent == None:
        root = i

print('Preorder')
preorder(root)
print()
print('Inorder')
inorder(root)
print()
print('Postorder')
postorder(root)
print()
