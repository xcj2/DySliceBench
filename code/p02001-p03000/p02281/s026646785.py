N = int(input())
nodes = [[-1,-1,-1] for i in range(N)]

for k in range(N):
    i,l,r = map(int,input().split())
    nodes[i][1] = l
    nodes[i][2] = r
    if l != -1:
        nodes[l][0] = i
    if r != -1:
        nodes[r][0] = i

#print(nodes)

def preParse(u):
    if u == -1:
        return
    print(' {}'.format(u), end='')
    preParse(nodes[u][1])
    preParse(nodes[u][2])

def inParse(u):
    if u == -1:
        return
    inParse(nodes[u][1])
    print(' {}'.format(u), end='')
    inParse(nodes[u][2])

def postParse(u):
    if u == -1:
        return
    postParse(nodes[u][1])
    postParse(nodes[u][2])
    print(' {}'.format(u), end='')

root = 0
while nodes[root][0] != -1:
    root = nodes[root][0]

print('Preorder')
preParse(root)
print()

print('Inorder')
inParse(root)
print()

print('Postorder')
postParse(root)
print()

