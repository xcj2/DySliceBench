if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    from collections import defaultdict

    NIL = -1

    n = int(input())

    T = defaultdict(lambda: {'left':NIL, 'right':NIL, 'parent':NIL})
    D = {}
    H = {}

    for _ in range(n):
        u, left, right = map(int, input().split())
        T[u]['left'] = left
        T[u]['right'] = right
        if left != NIL:
            T[left]['parent'] = u
        if right != NIL:
            T[right]['parent'] = u

    def set_depth(u, d):
        if u == NIL:
            return
        D[u] = d
        set_depth(T[u]['left'], d+1)
        set_depth(T[u]['right'], d+1)

    def set_height(u):
        h1 = 0
        h2 = 0
        if T[u]['left'] != NIL:
            h1 = set_height(T[u]['left'])+1
        if T[u]['right'] != NIL:
            h2 = set_height(T[u]['right'])+1
        height = max(h1, h2)
        H[u] = height
        return height

    for u, value in T.items():
        if value['parent'] == NIL:
            root = u
            break

    set_depth(root, 0)
    set_height(root)

    # 節点uの兄弟を返す
    def get_sibling(u):
        if T[u]['parent'] == NIL:
            return NIL
        if T[T[u]['parent']]['left'] != u:  # and 以降なくても問題ない
            return T[T[u]['parent']]['left']
        if T[T[u]['parent']]['right'] != u:  # and 以降なくても問題ない
            return T[T[u]['parent']]['right']
        return NIL

    for u in range(n):
        value = T[u]
        parent = value['parent']
        sibling = get_sibling(u)
        deg = 0
        if T[u]['left'] != NIL:
            deg += 1
        if T[u]['right'] != NIL:
            deg += 1
        if value['parent'] == NIL:
            type = 'root'
        elif value['left'] == NIL and value['right'] == NIL:
            type = 'leaf'
        else:
            type = 'internal node'
        depth = D[u]
        height = H[u]
        print('node ' + str(u) + ': ', end='')
        print('parent = ' + str(parent) +', ', end='')
        print('sibling = ' + str(sibling) + ', ', end='')
        print('degree = ' + str(deg) + ', ', end='')
        print('depth = ' + str(depth) + ', ', end='')
        print('height = ' + str(height) + ', ', end='')
        print(type)
