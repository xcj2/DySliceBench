if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    NIL = -1

    m = int(input())

    root = NIL

    def insert(k):
        global root
        y = NIL
        x = root
        z = {'key':k, 'left':NIL, 'right':NIL}
        while x != NIL:
            y = x
            if z['key'] < x['key']:
                x = x['left']
            else:
                x = x['right']
        z['parent'] = y

        if y == NIL:
            root = z
        elif z['key'] < y['key']:
            y['left'] = z
        else:
            y['right'] = z

    def find(u, k):
        while u != NIL and k != u['key']:
            if k < u['key']:
                u = u['left']
            else:
                u = u['right']
        return u

    def tree_minimum(x):
        while x['left'] != NIL:
            x = x['left']
        return x

    def tree_successor(x):
        if x['right'] != NIL:
            return tree_minimum(x['right'])
        y = x['parent']
        while y != NIL and x == y['right']:
            x = y
            y = y['parent']
        return y

    def tree_delete(z):
        global root
        if z['left'] == NIL or z['right'] == NIL:
            y = z
        else:
            y = tree_successor(z)
        # yの子xを決める
        if y['left'] != NIL:
            x = y['left']
        else:
            x = y['right']

        if x != NIL:
            x['parent'] = y['parent']

        if y['parent'] == NIL:
            root = x
        elif y == y['parent']['left']:
            y['parent']['left'] = x
        else:
            y['parent']['right'] = x

        if y != z:
            z['key'] = y['key']

    def inorder(u):
        if u == NIL:
            return
        inorder(u['left'])
        print(' ' + str(u['key']), end='')
        inorder(u['right'])

    def preorder(u):
        if u == NIL:
            return
        print(' ' + str(u['key']), end='')
        preorder(u['left'])
        preorder(u['right'])

    for _ in range(m):
        command = input()
        if command[0] == 'f':
            _, x = command.split()
            x = int(x)
            t = find(root, x)
            if t != NIL:
                print('yes')
            else:
                print('no')
        elif command[:6] == 'insert':
            _, x = command.split()
            x = int(x)
            insert(x)
        elif command[:5] == 'print':
            inorder(root)
            print('')
            # pythonのprintは最後に改行記号をつけてくれるので、これで改行できる
            preorder(root)
            print('')
        else:
            _, x = command.split()
            x = int(x)
            tree_delete(find(root, x))

