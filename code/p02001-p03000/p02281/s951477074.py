class Node:
    def __init__(self, p=-1, l=-1, r=-1):
        self._p = p
        self._l = l
        self._r = r

T = []

def pre_parse(index):
    if index == -1:
        return
    print(' %d'%index, end='')
    pre_parse(T[index]._l)
    pre_parse(T[index]._r)

def in_parse(index):
    if index == -1:
        return
    in_parse(T[index]._l)
    print(' %d'%index, end='')
    in_parse(T[index]._r)

def post_parse(index):
    if index == -1:
        return
    post_parse(T[index]._l)
    post_parse(T[index]._r)
    print(' %d'%index, end='')

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        T.append(Node(-1, -1, -1))

    for i in range(n):
        index, l_child, r_child = map(int, input().split())
        T[index]._l = l_child
        T[index]._r = r_child
        if l_child != -1:
            T[l_child]._p = index
        if r_child != -1:
            T[r_child]._p = index

    root = -1
    for i in range(n):
        if T[i]._p == -1:
            root = i
            break

    print('Preorder')
    pre_parse(root)
    print('\nInorder')
    in_parse(root)
    print('\nPostorder')
    post_parse(root)
    print()

