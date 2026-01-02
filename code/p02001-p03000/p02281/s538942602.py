n = int(input())

"""親情報を入れる'p'、左の子を入れる'l'、右の子を入れる'r'の辞書を作成"""
p, l, r = {}, {}, {}

for i in range(n):
    num, left, right = input().split()
    l[num] = left
    r[num] = right
    if left != '-1':
        p[left] = num
    if right != '-1':
        p[right] = num

root = (set(l) - set(p)).pop()

def preorder(num):
    if num == '-1':
        return
    print(' ' + num, end='')
    preorder(l[num])
    preorder(r[num])

def inorder(num):
    if num == '-1':
        return
    inorder(l[num])
    print(' ' + num, end='')
    inorder(r[num])

def postorder(num):
    if num == '-1':
        return
    postorder(l[num])
    postorder(r[num])
    print(' ' + num, end='')

print('Preorder')
preorder(root)
print()
print('Inorder')
inorder(root)
print()
print('Postorder')
postorder(root)
print()
