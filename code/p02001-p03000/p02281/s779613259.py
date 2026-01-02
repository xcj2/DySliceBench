def preorder(tree, index):
    print(" " + str(index), end="")
    if tree[index][1] != -1:
        preorder(tree, tree[index][1])
    if tree[index][2] != -1:
        preorder(tree, tree[index][2])


def inorder(tree, index):
    if tree[index][1] != -1:
        inorder(tree, tree[index][1])
    print(" " + str(index), end="")
    if tree[index][2] != -1:
        inorder(tree, tree[index][2])


def postorder(tree, index):
    if tree[index][1] != -1:
        postorder(tree, tree[index][1])
    if tree[index][2] != -1:
        postorder(tree, tree[index][2])
    print(" " + str(index), end="")



n = int(input())
a = [[-1 for i in range(3)] for j in range(n)]
for _ in range(n):
    i, l, r = [int(x) for x in input().split()]
    a[i][1] = l
    a[i][2] = r
    a[l][0] = i
    a[r][0] = i

root = 0
for i, v in enumerate(a):
    if v[0] == -1:
        root = i
        break

print("Preorder")
preorder(a, root)
print("")
print("Inorder")
inorder(a, root)
print("")
print("Postorder")
postorder(a, root)
print("")

