import sys

m = int(input())

l, r = {}, {}

def insert(num):
    y = None
    x = root
    while True:
        y = x
        if num < x:
            try:
                x = l[x]
            except KeyError:
                break
        else:
            try:
                x = r[x]
            except KeyError:
                break
    if num < y:
        l[y] = num
    else:
        r[y] = num

def find(num):
    x = root
    while True:
        if num == x:
            print('yes')
            return
        elif num < x:
            try:
                x = l[x]
            except KeyError:
                print('no')
                return
        else:
            try:
                x = r[x]
            except KeyError:
                print('no')
                return

def inorder(num):
    try:
        inorder(l[num])
    except KeyError:
        pass
    print(' ' + str(num), end='')
    try:
        inorder(r[num])
    except KeyError:
        pass

def preorder(num):
    print(' ' + str(num), end='')
    try:
        preorder(l[num])
    except KeyError:
        pass
    try:
        preorder(r[num])
    except KeyError:
        pass

for i in range(m):
    order = sys.stdin.readline()
    if i == 0:
        global root
        root = int(order[7:])
        continue
    if order[0] == 'i':
        insert(int(order[7:]))
    elif order[0] == 'p':
        inorder(root)
        print()
        preorder(root)
        print()
    else:
        find(int(order[5:]))
