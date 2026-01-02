n = int(input())

class Node:
    def __init__(self):
        self.key = -1
        self.parent_id = -1
        self.left_id = -1
        self.right_id = -1


def insert(nodes,z):
    y = -1
    root_id = -1
    for i in range(len(nodes)):
        if nodes[i].parent_id == -1:
            root_id = i
            break

    x = root_id

    while x != -1:
        y = x
        if z.key < nodes[x].key:
            x = nodes[x].left_id
        else:
            x = nodes[x].right_id

    z.parent_id = y
    nodes.append(z)
    z_id = len(nodes) - 1
    if y == -1: pass
    elif z.key < nodes[y].key:
        nodes[y].left_id = z_id
    else:
        nodes[y].right_id = z_id


def pre(node_id):
    pre_list.append(nodes[node_id].key)
    left = nodes[node_id].left_id
    right = nodes[node_id].right_id

    if left != -1:
        pre(left)
    if right != -1:
        pre(right)


def Ino(node_id):
    if nodes[node_id].left_id != -1 :
        Ino(nodes[node_id].left_id)
    ino_list.append(nodes[node_id].key)
    if nodes[node_id].right_id != -1:
        Ino(nodes[node_id].right_id)

nodes = []
for i in range(n):
    cmd = input()
    op = cmd[0]

    if op == "i":
        z = Node()
        number = int(cmd[7:])
        z.key = number

        insert(nodes,z)

    if op =="p":
        pre_list = []
        ino_list = []
        for i in range(len(nodes)):
            if nodes[i].parent_id == -1:
                Ino(i)
                pre(i)
                break


        pre_list = list(map(str, pre_list))
        ino_list = list(map(str, ino_list))
        print(" ", end="")
        print(' '.join(ino_list))
        print(" ", end="")
        print(' '.join(pre_list))


