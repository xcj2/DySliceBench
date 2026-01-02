# coding: utf-8
n = int(input())
prt = [-1 for i in range(n)]
chd = [[] for i in range(n)]
root = -1

def preOrder(num):
    if num == -1:
        return
    print(f' {num}', end = '')
    preOrder(chd[num][0])
    preOrder(chd[num][1])

def inOrder(num):
    if num == -1:
        return
    inOrder(chd[num][0])
    print(f' {num}', end = '')
    inOrder(chd[num][1])

def postOrder(num):
    if num == -1:
        return
    postOrder(chd[num][0])
    postOrder(chd[num][1])
    print(f' {num}', end = '')
    
for i in range(n):
    idx, left, right = map(int, input().split())
    chd[idx].append(left)
    chd[idx].append(right)
    if left >= 0:
        prt[left] = idx
    if right >= 0:
        prt[right] = idx

for i in range(n):
    if prt[i] == -1:
        root = i
        break

print('Preorder')
preOrder(root)
print('\nInorder')
inOrder(root)
print('\nPostorder')
postOrder(root)
print('')
