def preorder(idx):
    if idx == -1:
        return 
    left,right = tree[idx]
    print(' {}'.format(idx), end='')
    preorder(left)
    preorder(right)

def inorder(idx):
    if idx == -1:
        return 
    left,right = tree[idx]
    inorder(left)
    print(' {}'.format(idx),end='')
    inorder(right)

def postorder(idx):
    if idx == -1:
        return
    left,right = tree[idx]
    postorder(left)
    postorder(right)
    print(' {}'.format(idx),end='')

n = int(input())
tree = [None]*n
root = set(range(n))

for _ in range(n):
    idx,left,right = map(int,input().split())
    tree[idx] = (left,right)
    root -= set([left,right])
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
