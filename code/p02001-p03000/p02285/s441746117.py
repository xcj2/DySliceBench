
class Node:

    def __init__(self, key: int) -> None:
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def input_line() -> (str, int):
    line = input().split()
    if line[0] == 'print':
        return line[0], None
    else:
        return line[0], int(line[1])


def preorder(tree: Node) -> None:
    """先行順巡回。"""
    print(f' {tree.key}', end='')
    if tree.left is not None:
        preorder(tree.left)
    if tree.right is not None:
        preorder(tree.right)


def inorder(tree: Node) -> None:
    """中間順巡回。"""
    if tree.left is not None:
        inorder(tree.left)
    print(f' {tree.key}', end='')
    if tree.right is not None:
        inorder(tree.right)


def do_inorder(node: Node) -> Node:
    if node.left is not None:
        return do_inorder(node.left)
    return node
    if node.right is not None:
        return inorder(node.right)


def get_next_node(node: Node) -> Node:
    """inorderで次の節点を返す。"""
    next_node = do_inorder(node.right)
    return next_node


def insert(new_node: Node) -> None:
    """二分探索木に挿入する。"""

    # rootはglobalに共有する。
    global root

    # new_nodeを付け加える節(parent)の初期値をNoneに設定する。
    parent = None

    # tmpにrootを設定する。
    tmp = root

    # new_nodeを付け加える節(parent)を探索する。
    while tmp is not None:
        parent = tmp
        if new_node.key < tmp.key:
            tmp = tmp.left
        else:
            tmp = tmp.right

    # new_nodeの親を設定する。
    new_node.parent = parent

    # new_nodeの子供を設定する。
    if parent is None:
        # treeが空だった場合は、rootにnew_nodeを設定する。
        root = new_node
    elif new_node.key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node


def find(key)-> bool:
    if get_node(key) is None:
        return False
    else:
        return True


def get_node(key: int) -> Node:
    """キーが一致するノードを返す。"""
    global root

    # tmpにrootを設定する。
    node = root

    # new_nodeを付け加える節(parent)を探索する。
    while node is not None:
        if key == node.key:
            return node
        elif key < node.key:
            node = node.left
        else:
            node = node.right

    return None


def count_child(node: Node) -> int:
    """ノードの子供の数を取得する。"""
    child_num = 0
    if node.left is not None:
        child_num += 1
    if node.right is not None:
        child_num += 1
    return child_num


def do_delete(node: Node) -> None:
    # delete対象がない場合はメソッドを終了する。
    if node is None:
        return

    child_num = count_child(node)
    parent = node.parent

    if parent is None:
        raise ValueError('親がないケース')

    # keyに一致するノードをzとおく。
    # パターン1: zが子を持たない場合。
    if child_num == 0:
        if parent.left is not None and parent.left.key == node.key:
            parent.left = None
        # if parent.right is not None and parent.right.key == node.key:
        else:
            parent.right = None

    # パターン2: zが子をひとつ持つ場合。
    elif child_num == 1:
        if parent.left is not None and parent.left.key == node.key:
            if node.left is not None:
                parent.left = node.left
                parent.left.parent = parent
            else:
                parent.left = node.right
                parent.left.parent = parent
        else:
            if node.left is not None:
                parent.right = node.left
                parent.right.parent = parent
            else:
                parent.right = node.right
                parent.right.parent = parent

    # パターン3: zが子をふたつ持つ場合。
    elif child_num == 2:
        # inorderでnodeの次に出る節点を取得する。
        next_node = get_next_node(node)
        node.key = next_node.key
        do_delete(next_node)
    else:
        raise ValueError('想定してない事態')


def delete(key: int) -> None:

    node = get_node(key)
    do_delete(node)


root = None  # treeの根を表す。初期値はNone。
N = int(input())
for _i in range(N):
    order, val = input_line()
    if order == 'insert':
        node = Node(val)
        insert(node)
    elif order == 'print':
        inorder(root)
        print()
        preorder(root)
        print()
    elif order == 'find':
        if find(val):
            print('yes')
        else:
            print('no')
    elif order == 'delete':
        delete(val)



