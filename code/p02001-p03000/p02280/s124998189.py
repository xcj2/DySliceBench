class Node:
    def __init__(self, p=-1, l=-1, r=-1):
        self._p = p
        self._l = l
        self._r = r

T = []
Depth = []
Height = []

def get_sibling(index):
    global T
    if T[index]._p == -1:
        return -1
    if T[T[index]._p]._l != index:
        return T[T[index]._p]._l
    if T[T[index]._p]._r != index:
        return T[T[index]._p]._r
    return -1

def print_node(index):
    global Depth
    global Height
    global T
    
    deg = 0
    if T[index]._l != -1:
        deg += 1
    if T[index]._r != -1:
        deg += 1
    
    print('node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, '%(index, T[index]._p, get_sibling(index), deg, Depth[index], Height[index]), end='')

    if T[index]._p == -1:
        print('root')
    elif T[index]._l == -1 and T[index]._r == -1:
        print('leaf')
    else:
        print('internal node')

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        T.append(Node(-1, -1, -1))
        Depth.append(-1)
        Height.append(-1)

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

    def rec(node, dep):
        Depth[node] = dep

        lh = rh = 0
        if T[node]._l != -1:
            lh = rec(T[node]._l, dep + 1) + 1
        if T[node]._r != -1:
            rh = rec(T[node]._r, dep + 1) + 1

        Height[node] = max(lh, rh)
        return Height[node]

    rec(root, 0)

    for i in range(n):
        print_node(i)

