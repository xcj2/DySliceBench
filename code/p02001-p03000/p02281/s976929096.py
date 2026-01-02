import sys

def walk_preorder(n):
    c = children[n]
    print(' {}'.format(n), end='')
    if c[0]>=0: walk_preorder(c[0])
    if c[1]>=0: walk_preorder(c[1])

def walk_inorder(n):
    c = children[n]
    if c[0]>=0: walk_inorder(c[0])
    print(' {}'.format(n), end='')
    if c[1]>=0: walk_inorder(c[1])

def walk_postorder(n):
    c = children[n]
    if c[0]>=0: walk_postorder(c[0])
    if c[1]>=0: walk_postorder(c[1])
    print(' {}'.format(n), end='')
    

n = int(sys.stdin.readline())
parent = [-1 for _ in range(n)]
children = [[] for _ in range(n)]
for _ in range(n):
    id, left, right = list(map(int, sys.stdin.readline().split()))
    children[id] = [left, right]
    if left>=0:  parent[left] = id
    if right>=0: parent[right] = id

root=parent.index(-1)
order=[]
print('Preorder')
walk_preorder(root)
print()
print('Inorder')
walk_inorder(root)
print()
print('Postorder')
walk_postorder(root)
print()
