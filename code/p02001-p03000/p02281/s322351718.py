def pre(k):
    global nodes

    print(' ' + str(k), end= '')

    if nodes[k][1] != -1:
        pre(nodes[k][1])

    if nodes[k][2] != -1:
        pre(nodes[k][2])

def ino(k):
    global nodes

    if nodes[k][1] != -1:
        ino(nodes[k][1])

    print(' ' + str(k), end= '')

    if nodes[k][2] != -1:
        ino(nodes[k][2])
    


def pos(k):
    global nodes

    if nodes[k][1] != -1:
        pos(nodes[k][1])

    if nodes[k][2] != -1:
        pos(nodes[k][2])


    print(' ' + str(k), end= '')



n = int(input())
nodes = []

for i in range(n):
    nodes.append([-1])


for i in range(n):
    a = list(map(int, input().split()))
    if a[1] != -1:
        nodes[a[1]][0] = a[0]
    if a[2] != -1:
        nodes[a[2]][0] = a[0]
    
    nodes[a[0]] += a[1:]

for i in range(len(nodes)):
    if nodes[i][0] == -1:
        ro = i
        break

print('Preorder')
pre(ro)
print()
print('Inorder')
ino(ro)
print()
print('Postorder')
pos(ro)
print()
