
class Node:

    def __init__(self, key: int) -> None:
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def input_line() -> (str, int):
    line = input().split()
    if line[0] == 'insert':
        return 'insert', int(line[1])
    else:
        return line[0], None


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


def insert(new_node: Node) -> None:
    """二分探索木に挿入する。"""
    global root  # rootはglobalに共有する。
    parent = None
    x = root

    # new_nodeを付け加える節(parent)を探索。
    while x is not None:
        parent = x
        if new_node.key < x.key:
            x = x.left
        else:
            x = x.right
    new_node.parent = parent

    # new_nodeの子供を設定。
    if parent is None:  # treeが空だった場合は、rootにnew_nodeを設定。
        # print(f'key: {new_node.key} op: new node')
        root = new_node
    elif new_node.key < parent.key:
        # print(f'key: {new_node.key} op: left')
        parent.left = new_node
    else:
        # print(f'key: {new_node.key} op: right')
        parent.right = new_node


root = None  # treeの根を表す。初期値はNone。
N = int(input())
for _i in range(N):
    order, val = input_line()
    if order == 'insert':
        node = Node(val)
        insert(node)
    else:
        inorder(root)
        print()
        preorder(root)
        print()



