import sys

sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, p, l, r):
        self.p = p
        self.l = l
        self.r = r


N = int(input())
T = [Node(-1, -1, -1) for _ in range(N)]


def preorder_parse(u):
    if u == -1:
        return
    print(' ' + str(u), end='')
    preorder_parse(T[u].l)
    preorder_parse(T[u].r)


def inorder_parse(u):
    if u == -1:
        return
    inorder_parse(T[u].l)
    print(' ' + str(u), end='')
    inorder_parse(T[u].r)


def postorder_parse(u):
    if u == -1:
        return
    postorder_parse(T[u].l)
    postorder_parse(T[u].r)
    print(' ' + str(u), end='')


def main():
    for _ in range(N):
        v, l, r = map(int, input().split())
        T[v].l = l
        T[v].r = r
        if l != -1:
            T[l].p = v
        if r != -1:
            T[r].p = v

    root = 0
    for i, t in enumerate(T):
        if t.p == -1:
            root = i

    print('Preorder')
    preorder_parse(root)
    print('')
    print('Inorder')
    inorder_parse(root)
    print('')
    print('Postorder')
    postorder_parse(root)
    print('')


if __name__ == '__main__':
    main()

