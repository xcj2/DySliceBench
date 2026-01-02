
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


def find(key):
    global T
    global root

    x = root

    while x is not None and key != x.key:
        # print(key, x.key)

        if key < x.key:
            x = x.left
        else:
            x = x.right
    return x  # マッチしなければNONEが戻る。


def delete(key):
    global T
    global root

    z = find(key)


    # まず、削除するノードを決める。
    if z.left is None or z.right is None:
        y = z
    else:
        y = tree_successor(z)

    # yの子xを決める。
    if y.left is not None:
        x = y.left  # 親がいなくなる子ノード
    else:
        x = y.right

    if x is not None:
        x.parent = y.parent  # yの親が新しいxの親になる

    if y.parent is None:
        root = x  # yに親がいない場合は、つまりyがルートなので、xが新しいルートになる。
    else:
        if y == y.parent.left:
            y.parent.left = x  # yの親の方の子供をxに更新する。
        else:
            y.parent.right = x

    if y != z:
        z.key = y.key


def tree_minimum(x):
    """ xを根とした場合に、一番小さなノードを見つける（＝左下に行き続ける） """
    while x.left is not None:
        x = x.left
    return x


def tree_successor(x):
    """ 中間巡回でxの次に来るものを見つける。
        中間巡回は昇順ソートと同じなので、つまり、
        xの次に大きいノードを探すということ。

        もしxに右の子がいれば、x以下の木のなかで、
        xの次に大きいノードを見つけることができる。

        しかし、もしxが右の子を持たなければ、
        全体の木の中で次に大きいのは、
        xより上の木まで探しに行く必要がある。
    """

    """ xに右の子がいる場合 """
    if x.right is not None:
        return tree_minimum(x.right)

    """ xに右の子がいない場合 """
    y = x.parent  # xが親の左側の子の場合は、これで完了。

    # 右側の子だった場合は、弟の立場になるまで遡る。
    while y is not None and x == y.right:
        x = y
        y = y.parent

    return y


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

    elif order.startswith('find'):
        order, value = order.split()
        value = int(value)
        _ = find(value)
        if _ is None:
            print('no')
        else:
            print('yes')

    elif order.startswith('delete'):
        order, value = order.split()
        value = int(value)
        delete(value)

    else:
        order, value = order.split()
        value = int(value)
        insert(value)

