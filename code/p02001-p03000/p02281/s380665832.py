n=int(input())
data=[list(map(int,input().split())) for i in range(n)]
data.sort(key=lambda tup:tup[0])
parent=[-1]*n

for i in range(n):
    if data[i][1]!=-1:
        parent[data[i][1]]=i
    if data[i][2]!=-1:
        parent[data[i][2]]=i

for i in range(n):
    if parent[i]==-1:
        root=i

def preorder(node):
    if node==-1:return
    print(' '+str(node),end='')
    preorder(data[node][1])
    preorder(data[node][2])

def inorder(node):
    if node==-1:return
    inorder(data[node][1])
    print(' '+str(node),end='')
    inorder(data[node][2])

def postorder(node):
    if node==-1:return
    postorder(data[node][1])
    postorder(data[node][2])    
    print(' '+str(node),end='')

print('Preorder')
preorder(root)
print()
print('Inorder')
inorder(root)
print()
print('Postorder')
postorder(root)
print()




        
