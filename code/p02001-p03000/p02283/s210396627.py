treeRoot = {'left': None, 'right': None, 'p': None, 'val': None}

root = None


def insert(val):
    global root
    z = {'left': None, 'right': None, 'p': None, 'val': val}
    x = root
    y = None
    while x:
        y = x
        if z['val'] < x['val']:
            x = x['left']
        else:
            x = x['right']
    z['p'] = y
    if y is None:
        root = z
    else:
        if z['val'] < y['val']:
            y['left'] = z
        else:
            y['right'] = z


def inorder(root):
    if root is None:
        return
    inorder(root['left'])
    print(' ', end='')
    print(root['val'], end='')
    inorder(root['right'])


def preorder(root):
    if root is None:
        return
    print(' ', end='')
    print(root['val'], end='')
    preorder(root['left'])
    preorder(root['right'])


M = int(input())
for _ in range(M):
    line = input().strip()
    if line == 'print':
        inorder(root)
        print('')
        preorder(root)
        print('')
    else:
        inst, k = line.split()
        k = int(k)
        if inst == 'insert':
            insert(k)
        elif inst == 'find':
            pass
        elif inst == 'delete':
            pass