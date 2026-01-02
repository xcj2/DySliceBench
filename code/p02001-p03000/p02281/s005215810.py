class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

pre = []
def preorder(t, n):
    pre.append(n)
    if t[n].left is not None:
        preorder(t, t[n].left)
    if t[n].right is not None:
        preorder(t, t[n].right)

ino = []
def inorder(t, n):
    if t[n].left is not None:
        inorder(t, t[n].left)
        ino.append(n)
    else:
        ino.append(n)
    if t[n].right is not None:
        inorder(t, t[n].right)
    if n not in ino:
        ino.append(n)

post = []
def postorder(t, n):
    if t[n].left is not None:
        postorder(t, t[n].left)
    if t[n].right is not None:
        postorder(t, t[n].right)
    post.append(n)

n = int(input())
t = {k: Node(None, None, None) for k in range(n)}
for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] != -1:
        t[tmp[1]].parent = tmp[0] # 親
        t[tmp[0]].left = tmp[1] # 左の子
    if tmp[2] != -1:
        t[tmp[2]].parent = tmp[0] # 親
        t[tmp[0]].right = tmp[2] # 右の子

for node in range(n):
    if t[node].parent is None:
        preorder(t, node)
        inorder(t, node)
        postorder(t, node)

print("Preorder")
print(" " + " ".join([str(k) for k in pre]))
print("Inorder")
print(" " + " ".join([str(k) for k in ino]))
print("Postorder")
print(" " + " ".join([str(k) for k in post]))
