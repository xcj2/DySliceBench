def preParse(u):
    if u == None:
        return
    print(' {}'.format(u), end='')
    preParse(nodes[u][1])
    preParse(nodes[u][2])

def inParse(u):
    if u == None:
        return
    inParse(nodes[u][1])
    print(' {}'.format(u), end='')
    inParse(nodes[u][2])

nodes = {}

# {key:[parent,left,right]}

N = int(input())

root = None

def insert(nodes,z,root):
    x = root
    y = None
    while x != None:
        y = x
        if z < x:
            x = nodes[x][1]
        else:
            x = nodes[x][2]
    nodes[z][0] = y

    if y == None:
        root = z
    elif z < y:
        nodes[y][1] = z
    else:
        nodes[y][2] = z
    return root

for i in range(N):
    order = input().split()
    if order[0] == 'print':
        inParse(root)
        print()
        preParse(root)
        print()
        continue

    z = int(order[1])
    nodes[z] = [None,None,None]
    root = insert(nodes,z,root)

