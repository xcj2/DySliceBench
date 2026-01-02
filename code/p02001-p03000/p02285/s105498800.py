import sys
sys.setrecursionlimit(2 ** 20)

class Node:
    def __init__(self, parent, left, right):
        self.parent, self.left, self.right = parent, left, right

T = {}
root = None

def insert_node(key):
    global root
    x = root
    y = None
    z = Node(None, None, None)
    while x != None:
        y = x
        if key < x:
            x = T[x].left
        else:
            x = T[x].right
    z.parent = y
    if y == None:
        root = key
    else:
        if key < y:
            T[y].left = key
        else:
            T[y].right = key
    T[key] = z

def find_node(key):
    x = root
    while x != None and key != x:
        if key < x:
            x = T[x].left
        else:
            x = T[x].right
    if x != None:
        print('yes')
    else:
        print('no')

def get_minimum(key):
    while T[key].left != None:
        key = T[key].left
    return key

def delete_node(key):
    global root
    parent = T[key].parent

    if T[key].left == None and T[key].right == None:
        if T[parent].left == key:
            T[parent].left = None
        elif T[parent].right == key:
            T[parent].right = None
        del T[key]

    elif T[key].right == None:
        key_is_left = True if T[parent].left == key else False
        child = T[key].left
        if key_is_left:
            T[parent].left = child
        else:
            T[parent].right = child
        T[child].parent = parent
        del T[key]

    elif T[key].left == None:
        key_is_left = True if T[parent].left == key else False
        child = T[key].right
        if key_is_left:
            T[parent].left = child
        else:
            T[parent].right = child
        T[child].parent = parent
        del T[key]

    elif T[key].left != None and T[key].right != None:
        left, right = T[key].left, T[key].right
        node_next_more = get_minimum(T[key].right)
        next_more_right = T[node_next_more].right
        next_more_parent = T[node_next_more].parent
        if parent == None:
            if node_next_more == right:
                T[right].parent = None
                T[right].left = left
                root = right
                del T[key]
                return
            else:
                T[node_next_more].left = left
                T[node_next_more].right = right
                T[node_next_more].parent = None
                T[left].parent = node_next_more
                T[right].parent = node_next_more
                if next_more_right != None:
                    T[next_more_right].parent = next_more_parent
                root = node_next_more
                del T[key]
                return
        else:
            key_is_left = True if T[parent].left == key else False
            if node_next_more == right:
                if key_is_left:
                    T[parent].left = right
                else:
                    T[parent].right = right
                T[right].parent = parent
                T[right].left = left
                del T[key]
                return
            else:
                if key_is_left:
                    T[parent].left = node_next_more
                else:
                    T[parent].right = node_next_more
                T[node_next_more].left = T[key].left
                T[node_next_more].right = T[key].right
                T[node_next_more].parent = parent
                T[left].parent = node_next_more
                T[right].parent = node_next_more
                T[next_more_parent].left = next_more_right
                if next_more_right is not None:
                    T[next_more_right].parent = next_more_parent
                del T[key]
                return

def in_print(key, ls):
    if key == None:
        return
    in_print(T[key].left, ls)
    ls.append(key)
    in_print(T[key].right, ls)

def pre_print(key, ls):
    if key == None:
        return
    ls.append(key)
    pre_print(T[key].left, ls)
    pre_print(T[key].right, ls)

def print_node():
    in_ls, pre_ls = [], []
    in_print(root, in_ls)
    pre_print(root, pre_ls)
    print('', *in_ls)
    print('', *pre_ls)

N = int(input())
for i in range(N):
    com = input().split()
    if com[0] == 'insert':
        insert_node(int(com[1]))
    elif com[0] == 'find':
        find_node(int(com[1]))
    elif com[0] == 'delete':
        delete_node(int(com[1]))
    elif com[0] == 'print':
        print_node()
