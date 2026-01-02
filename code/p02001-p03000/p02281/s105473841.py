from sys import stdin
input = stdin.readline

def preorder(idx, nodelist):
    nodelist.append(idx)
    left, right = leftlist[idx], rightlist[idx]
    if left != -1:
        preorder(left, nodelist)
    if right != -1:
        preorder(right, nodelist)
    return nodelist

def inorder(idx, nodelist):
    left, right = leftlist[idx], rightlist[idx]
    if left != -1:
        inorder(left, nodelist)
    if right != -1:
        nodelist.append(idx)
        inorder(right, nodelist)
    else:
        nodelist.append(idx)
    return nodelist
    
def postorder(idx, nodelist):
    left, right = leftlist[idx], rightlist[idx]
    if left != -1:
        postorder(left, nodelist)
    if right != -1:
        postorder(right, nodelist)
        nodelist.append(idx)
    else:
        nodelist.append(idx)
    return nodelist

n = int(input())
parentlist = [-1]*n
leftlist = [-1]*n
rightlist = [-1]*n
for i in range(n):
    idx, left, right = map(int, input().split())
    leftlist[idx], rightlist[idx] = left, right
    if left != -1:
        parentlist[left] = idx
    if right != -1:
        parentlist[right] = idx
root = parentlist.index(-1)

print('Preorder\n', *preorder(root, []))
print('Inorder\n', *inorder(root, []))
print('Postorder\n', *postorder(root, []))
