def insert(z):
    global root
    y = NIL
    x = root
    #print(x)
    while x != NIL:
        y = x
        if z < x:
            x = TL[x]
        else:
            x = TR[x]
    TP[z] = y

    if y == NIL:
        root = z
    elif z < y:
        TL[y] = z
    else:
        TR[y] = z


def inorder(u):
    if u == NIL:
        return
    inorder(TL[u])
    print(' ', end='')
    print(u, end='')
    inorder(TR[u])


def preorder(v):
    if v == NIL:
        return
    print(' ', end='')
    print(v, end='')
    preorder(TL[v])
    preorder(TR[v])


TR = {}
TL = {}
TP = {}
NIL = None
root = NIL
m = int(input())
data = [input().split() for _ in range(m)]
#print(data)
for i in data:
    if i[0][0] == 'i':
        TR[int(i[1])] = TL[int(i[1])] = NIL
        insert(int(i[1]))
    elif i[0][0] == 'f':
        if int(i[1]) in TR:
            print('yes')
        else:
            print('no')
    else:
        inorder(root)
        print()
        preorder(root)
        print()
