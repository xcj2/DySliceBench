
nil = -1

class Node:
    def __init__(self):
        self.parent = nil
        self.left = nil
        self.right = nil

def pre_tw(node):
    print(' ' + str(node), end = '')

    if tree[node].left != nil:
        pre_tw(tree[node].left)

    if tree[node].right != nil:
        pre_tw(tree[node].right)

def in_tw(node):
    if tree[node].left != nil:
        in_tw(tree[node].left)

    print(' ' + str(node), end = '')

    if tree[node].right != nil:
        in_tw(tree[node].right)

def post_tw(node):
    if tree[node].left != nil:
        post_tw(tree[node].left)

    if tree[node].right != nil:
        post_tw(tree[node].right)

    print(' ' + str(node), end = '')


n = int(input())

tree = [Node() for i in range(n)]

for i in range(n):
    line = [int(j) for j in input().split()]
    id_t = line[0]
    left = line[1]
    right = line[2]

    if left != nil:
        tree[id_t].left = left
        tree[left].parent = id_t
    if right != nil:
        tree[id_t].right = right
        tree[right].parent = id_t

for i in range(n):
    if tree[i].parent == nil:
        root = i
        break

print('Preorder')
pre_tw(root)
print('')

print('Inorder')
in_tw(root)
print('')

print('Postorder')
post_tw(root)
print('')