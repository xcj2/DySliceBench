'''
def delete(z):
    global root
    if TL[z] == NIL or TR[z] == NIL:
        y = z
    else:
        y = get_next(z)
    if TL[y] != NIL:
        x = TL[y]
    else:
        x = TR[y]
    if x != NIL:
        TP[x] = TP[y]
    if TP[y] == NIL:
        root = x
    elif y == TL[TP[y]]:
        TL[TP[y]] = x
    else:
        TR[TP[y]] = x
    if y != z:
        TP[z], TR[z], TL[z] = TP[y], TR[y], TL[y]
    del TP[y]
    del TR[y]
    del TL[y]
    print(z)
    hyouzi()

    #print(TR)
    #print(TL)
    #print(x)
    if TR[x] == NIL and TL[x] == NIL:
        if TR[TP[x]] == x:
            TR[TP[x]] = NIL
        else:
            TL[TP[x]] = NIL
    elif TR[x] == NIL:
        if TR[TP[x]] == x:
            TR[TP[x]] = TL[x]
            TP[TL[x]] = TP[x]
        else:
            TL[TP[x]] = TL[x]
            TP[TL[x]] = TP[x]
    elif TL[x] == NIL:
        if TR[TP[x]] == x:
            TR[TP[x]] = TR[x]
            TP[TR[x]] = TP[x]
        else:
            TL[TP[x]] = TR[x]
            TP[TR[x]] = TP[x]
    else:
        y = get_next(x)
        TP[x], TR[x], TL[x] = TP[y], TR[y], TL[y]
        delete(y)
'''


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


def get_next(x):
    if TR[x] != NIL:
        return get_minimum(TR[x])
    y = TP[x]
    while y != NIL and x == TR[y]:
        x = y
        y = TP[y]
    return y


def get_minimum(x):
    while TL[x] != NIL:
        x = TL[x]
    return x


def treedelete(z):
    if z in TL:
        if TL[z] != NIL and TR[z] != NIL:
            y = get_next(z)
            '''
            print(y, z)
            print(TR)
            print(TL)
            print(TP)
            '''
        else:
            y = z
        if TL[y] == NIL and TR[y] == NIL:
            if TR[TP[y]] == y:
                TR[TP[y]] = NIL
            else:
                TL[TP[y]] = NIL
        elif TL[y] == NIL and TR[y] != NIL:
            if TR[TP[y]] == y:
                TR[TP[y]] = TR[y]
                TP[TR[y]] = TP[y]
            else:
                TL[TP[y]] = TR[y]
                TP[TR[y]] = TP[y]
        elif TL[y] != NIL and TR[y] == NIL:
            if TR[TP[y]] == y:
                TR[TP[y]] = TL[y]
                TP[TL[y]] = TP[y]
            else:
                TL[TP[y]] = TL[y]
                TP[TL[y]] = TP[y]
        if y != z:
            if TR[TP[z]] == z:
                TR[TP[z]] = y
            else:
                TL[TP[z]] = y
            TP[TL[z]] = y
            TP[TR[z]] = y
            TL[y], TR[y], TP[y] = TL[z], TR[z], TP[z]
            del TL[z], TR[z], TP[z]
            #print(TL[z], TR[z], TP[z], TL[y], TR[y], TP[y])
            #TL[z], TR[z], TP[z] = TL[y], TR[y], TP[y]
        else:
            del TL[y], TR[y], TP[y]



def hyouzi():
    inorder(root)
    print()
    preorder(root)
    print()


TR = {}
TL = {}
TP = {}
NIL = 10000000000000000000000
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
    elif i[0][0] == 'd':
        #print(i[1])
        treedelete(int(i[1]))
    elif i[0][0] == 'p':
        hyouzi()
    '''
    print(i)
    print(TR)
    print(TL)
    print(TP)
    '''

