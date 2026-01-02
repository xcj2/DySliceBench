N = int(input())

class Node():
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right

T = [Node() for _ in range(N)]

for _ in range(N):
    id, left, right = map(int, input().split())

    T[id].left = left
    T[id].right = right

    if left != -1:
        T[left].parent = id
    if right != -1:
        T[right].parent = id


def preorder(id):
    if id == -1:
        return

    preorder_list.append(id)

    preorder(T[id].left)
    preorder(T[id].right)

def inorder(id):
    if id == -1:
        return

    inorder(T[id].left)
    inorder_list.append(id)
    inorder(T[id].right)

def postorder(id):
    if id == -1:
        return

    postorder(T[id].left)
    postorder(T[id].right)
    postorder_list.append(id)

preorder_list = []
inorder_list = []
postorder_list = []
for id in range(N):
    if T[id].parent == -1:
        preorder(id)
        inorder(id)
        postorder(id)
        break


print("Preorder")
print(" "+" ".join(map(str, preorder_list)))
print("Inorder")
print(" "+" ".join(map(str, inorder_list)))
print("Postorder")
print(" "+" ".join(map(str, postorder_list)))
