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

def printTree(root):
    inParse(root)
    print()
    preParse(root)
    print()

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

def find(nodes,z,root):
    x = root
    while x != None and z != x:
        if z < x:
            x = nodes[x][1]
        else:
            x = nodes[x][2]
    return x

def getMinimum(nodes,x):
    while nodes[x][1] != None:
        x = nodes[x][1]
    return x

def getSuccessor(nodes,x):
    if nodes[x][2] != None:
        return getMinimum(nodes,nodes[x][2])
    
    y = nodes[x][0]
    while y != None and z == nodes[y][2]:
        x = y
        y = nodes[y][0]
    return y

def deleteNode(nodes,z,root):
    # 削除する対象をyとする
    if nodes[z][1] == None or nodes[z][2] == None:
        y = z
    else:
        y = getSuccessor(nodes,z)

    # yの子xを決める
    if nodes[y][1] != None:
        x = nodes[y][1]
    else:
        x = nodes[y][2]

    # xの親を設定する
    if x != None:
        nodes[x][0] = nodes[y][0]

    # yが根の時、xを木の根とする
    if nodes[y][0] == None:
        root = x
    # yがその親pの左の子なら、pの左の子をxとする
    elif y == nodes[nodes[y][0]][1]:
        nodes[nodes[y][0]][1] = x
    # yがその親pの右の子なら、pの右の子をxとする
    else:
        nodes[nodes[y][0]][2] = x
    
    # zの次節点の連結が解除された場合、yにzのデータをコピーし、
    # zに親子がいた場合はその親子に対してzの部分をyで置き換える
    # これによって、zの部分がまるでyに置き換わったように扱え、zが削除されたことになる
    if y != z:
        nodes[y] = nodes[z]
        if nodes[y][0] != None:
            if nodes[nodes[y][0]][1] == z:
                nodes[nodes[y][0]][1] = y
            else:
                nodes[nodes[y][0]][2] = y
        if nodes[y][1] != None:
            nodes[nodes[y][1]][0] = y
        if nodes[y][2] != None:
            nodes[nodes[y][2]][0] = y

    return root


nodes = {}

# {key:[parent,left,right]}

N = int(input())

root = None

for i in range(N):
    order = input().split()
    if order[0] == 'print':
        printTree(root)
        continue

    z = int(order[1])
    if order[0] == 'insert':
        nodes[z] = [None,None,None]
        root = insert(nodes,z,root)
        continue

    if order[0] == 'find':
        k = find(nodes,z,root)
        if k == z:
            print('yes')
        else:
            print('no')
        continue

    if order[0] == 'delete':
        root = deleteNode(nodes,z,root)
        continue

