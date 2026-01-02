class Node:
    '''
    p: parent node
    l: child node
    r: sibling node
    '''
    def __init__(self, p=-1, l=-1, r=-1):
        self._p = p
        self._l = l
        self._r = r

Depth = []
T = []

def rec(node, depth):
    global Depth
    global T
    Depth[node] = depth

    child = T[node]._l
    while child != -1:
        rec(child, depth + 1)
        child = T[child]._r


    # if T[node]._r != -1:
    #     rec(T[node]._r, depth)

    # if T[node]._l != -1:
    #     rec(T[node]._l, depth + 1)

def print_node(index):
    global Depth
    global T
    print('node %d: parent = %d, depth = %d, '%(index, T[index]._p, Depth[index]), end='')

    if T[index]._p == -1:
        print('root, [', end='')
    elif T[index]._l == -1:
        print('leaf, [', end='')
    else:
        print('internal node, [', end='')

    i = 0
    node = T[index]._l
    while node != -1:
        if i:
            print(', ', end='')
        print(node, end='')

        i += 1
        node = T[node]._r
    print(']')
    


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        T.append(Node())
    Depth = [-1]*n
    for i in range(n):
        parent_node, child_cnt, *child_node = map(int, input().split())
        for j in range(child_cnt):
            if j == 0:
                T[parent_node]._l = child_node[j]
            else:
                T[child_node[j - 1]]._r = child_node[j]
            T[child_node[j]]._p = parent_node

    root = 0
    for i in range(n):
        if T[i]._p == -1:
            root = i
            break
    
    rec(root, 0)

    for i in range(n):
        print_node(i)

