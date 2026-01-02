if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    from collections import defaultdict

    NIL = -1

    n = int(input())

    # pythonは構造体を用意するのに手間取るので、辞書型を使う
    T = defaultdict(lambda: {'l':NIL, 'r':NIL, 'p':NIL})

    for _ in range(n):
        u, l, r = map(int, input().split())
        T[u]['l'] = l
        T[u]['r'] = r
        if l != NIL:
            T[l]['p'] = u
        if r != NIL:
            T[r]['p'] = u

    for u, info in T.items():
        if info['p'] == NIL:
            root = u
            break

    # 先行順巡回
    def pre_parse(u):
        if u == NIL:
            return
        print(' ' + str(u), end='')
        pre_parse(T[u]['l'])
        pre_parse(T[u]['r'])

    # 中間順巡回
    def in_parse(u):
        if u == NIL:
            return
        in_parse(T[u]['l'])
        print(' ' + str(u), end='')
        in_parse(T[u]['r'])

    # 後行順巡回
    def post_parse(u):
        if u == NIL:
            return
        post_parse(T[u]['l'])
        post_parse(T[u]['r'])
        print(' ' + str(u), end='')

    print('Preorder')
    pre_parse(root)
    print('')

    print('Inorder')
    in_parse(root)
    print('')

    print('Postorder')
    post_parse(root)
    print('')
