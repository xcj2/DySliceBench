n= int(input())
a = [list(map(int, input().split())) for _ in range(n)]

p = [-1]*n
r = [-1]*n
l = [-1]*n

for i in range(n):
    ind = a[i][0]
    r[ind] = a[i][2]
    l[ind] = a[i][1]
    if r[ind]>=0:
        p[r[ind]] = ind
    if l[ind]>=0:
        p[l[ind]] = ind

root = -1
for i in range(n):
    if p[i]==-1:
        root = i
        break

def preorder(ind):
    print(' %i'%ind, end='')
    if l[ind]!=-1:
        preorder(l[ind])
    if r[ind]!=-1:
        preorder(r[ind])
        
def inorder(ind):
    if l[ind]!=-1:
        inorder(l[ind])
    print(' %i'%ind, end='')
    if r[ind]!=-1:
        inorder(r[ind])
        
def postorder(ind):
    if l[ind]!=-1:
        postorder(l[ind])
    if r[ind]!=-1:
        postorder(r[ind])
    print(' %i'%ind, end='')
    
print('Preorder')
preorder(root)
print()
print('Inorder')
inorder(root)
print()
print('Postorder')
postorder(root)
print()
