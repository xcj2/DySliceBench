N = int(input())
left  =  [-1 for i in range(N)]
right =  [-1 for i in range(N)]
root = sum(range(N)) - N - 1
 
for i in range(N):
    i, l, r = map(int, input().split())
    left[i] = l
    right[i] = r
    root -= (l + r)
 
def preorder(i):
    if i == -1:
        return
    print(' ', i, sep = '', end = '')
    preorder(left[i])
    preorder(right[i])
     
def inorder(i):
    if i == -1:
        return
    inorder(left[i])
    print(' ', i, sep = '', end = '')
    inorder(right[i])
     
def postorder(i):
    if i == -1:
        return
    postorder(left[i])
    postorder(right[i])
    print(' ', i, sep = '', end = '')
     
print('Preorder')
preorder(root)
print()
 
print('Inorder')
inorder(root)
print()
 
print('Postorder')
postorder(root)
print()