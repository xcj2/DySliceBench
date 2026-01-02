def preorder(tree, now):
    if now == -1:
        return []
    else:
        left = tree[now][0]
        right = tree[now][1]
        return [now] + preorder(tree, left) + preorder(tree, right)


def inorder(tree, now):
    if now == -1:
        return []
    else:
        left = tree[now][0]
        right = tree[now][1]
        return inorder(tree, left) + [now] + inorder(tree, right)


def postorder(tree, now):
    if now == -1:
        return []
    else:
        left = tree[now][0]
        right = tree[now][1]
        return postorder(tree, left) + postorder(tree, right) + [now]


def print_list_split_whitespace(a):
    print(" ", end="")
    for x in a[:-1]:
        print(x, end=" ")
    print(a[-1])


n = int(input())
tree = [[] for _ in range(n)]
ps = [-1 for _ in range(n)]
ss = [-1 for _ in range(n)]
for _ in range(n):
    s = input().split()
    id = int(s[0])
    left = int(s[1])
    right = int(s[2])
    tree[id] = [left, right]
    if left >= 0:
        ps[left] = id
        ss[left] = right
    if right >= 0:
        ps[right] = id
        ss[right] = left

root = ps.index(-1)

print("Preorder")
pre_list = preorder(tree, root)
print_list_split_whitespace(pre_list)

print("Inorder")
in_list = inorder(tree, root)
print_list_split_whitespace(in_list)

print("Postorder")
post_list = postorder(tree, root)
print_list_split_whitespace(post_list)
