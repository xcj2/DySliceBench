class Node():
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None


def preorder(id):
    print(f" {id}", end="")
    if tree[id].left is not None:
        preorder(tree[id].left)
    if tree[id].right is not None:
        preorder(tree[id].right)

def inorder(id):
    if tree[id].left is not None:
        inorder(tree[id].left)
    print(f" {id}", end="")
    if tree[id].right is not None:
        inorder(tree[id].right)


def postorder(id):
    if tree[id].left is not None:
        postorder(tree[id].left)
    if tree[id].right is not None:
        postorder(tree[id].right)
    print(f" {id}", end="")
    
n = int(input())
tree = []
for _ in range(n):
    tree.append(Node())
for _ in range(n):
    id, left, right = map(int, input().split())
    if left != -1:
        tree[id].left = left
        tree[left].parent = id
    if right != -1:
        tree[id].right = right
        tree[right].parent = id
        
for id in range(n):
    if tree[id].parent is None:
        root_id = id
        break
    
print("Preorder")
preorder(root_id)
print("")
print("Inorder")
inorder(root_id)
print("")
print("Postorder")
postorder(root_id)
print("")
