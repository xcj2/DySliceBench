#coding:utf-8
#1_7_C
def preorder(i):
    if i == -1:
        return
    (l, r) = tree[i]
    print(" {}".format(i), end = "")
    preorder(l)
    preorder(r)

def inorder(i):
    if i == -1:
        return
    (l, r) = tree[i]
    inorder(l)
    print(" {}".format(i), end = "")
    inorder(r)

def postorder(i):
    if i == -1:
        return
    (l, r) = tree[i]
    postorder(l)
    postorder(r)
    print(" {}".format(i), end = "")

n = int(input())
tree = [None for i in range(n)]
root = set(range(n))
for i in range(n):
    i, l, r = map(int, input().split())
    tree[i] = (l, r)
    root -= set([l, r])

root_node = root.pop()

print("Preorder")
preorder(root_node)
print()

print("Inorder")
inorder(root_node)
print()

print("Postorder")
postorder(root_node)
print()