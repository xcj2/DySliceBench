if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    from collections import defaultdict

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
        if command[:5] == 'print':
            inorder(root)
            print('')
            preorder(root)
            print('')
        else:

            _, k = command.split()
            k = int(k)
            insert(k)

