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
    elif com[0] == 'print':
        print_node()
