
class Node:
    key = None
    parent = None
    left = None
    right = None

    def __init__(self, key):
        self.key = key


def insert(key):
    global T
    global root

    new_node = Node(key)
    T.append(new_node)

    if root is None:
        root = new_node

    else:
        y = None  # 親
        x = root  # 子

        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node


def in_order(node, order):
    if node is None:
        return

    in_order(node.left, order)
    order.append(node.key)
    in_order(node.right, order)


def pre_order(node, order):
    if node is None:
        return

    order.append(node.key)
    pre_order(node.left, order)
    pre_order(node.right, order)


m = int(input())
T = []
root = None

for i in range(m):
    order = input()

    if order.startswith('print'):
        output = []
        in_order(root, output)
        # print(output)
        print(' ' + ' '.join(map(str, output)))

        output = []
        pre_order(root, output)
        # print(output)
        print(' ' + ' '.join(map(str, output)))

    else:
        order, value = order.split()
        value = int(value)
        insert(value)

