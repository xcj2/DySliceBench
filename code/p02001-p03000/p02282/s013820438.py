
class Node:
    left = -1
    right = -1


def get_root_index(first: int, end: int) -> int:
    """inorder[first:end]の根のインデックスを取得する。
    根： inorder[first:end]を左部分木と右部分木に分割するノード
    """

    # inorder[first:end]の要素でpreorderの一番手前にあるものが、
    # inorder[first:end]を左部分木と右部分木に分割するノード。
    # そのインデックスを返す。
    for pre in preorder:
        for j in range(first, end):
            if pre == inorder[j]:
                return j


def get_root(first, end) -> int:
    """inorder[first:end]の根のノードを返す。
    """

    root_ix = get_root_index(first, end)
    if root_ix is not None:
        return inorder[root_ix]
    else:
        return -1


def set_nodes(first: int, end: int):
    root_ix = get_root_index(first, end)
    if first + 1 < root_ix:
        set_nodes(first, root_ix)
    if root_ix + 1 < end - 1:
        set_nodes(root_ix + 1, end)
    nodes[inorder[root_ix]].left = get_root(first, root_ix)
    nodes[inorder[root_ix]].right = get_root(root_ix + 1, end)


def set_postorder(node_id: int) -> None:
    """後行順巡回で得られる節の番号を保存する。

    Args:
        node_id (int): [description]
    """

    left = nodes[node_id].left
    if left != -1:
        set_postorder(left)

    right = nodes[node_id].right
    if right != -1:
        set_postorder(right)

    postorder.append(node_id)


N = int(input())
nodes = [Node() for i in range(N + 1)]
preorder = [int(i) for i in input().split()]
inorder = [int(i) for i in input().split()]

set_nodes(0, N)

postorder = []
set_postorder(get_root(0, N))
print(' '.join(map(str, postorder)))
