# -*- coding:utf-8 -*-
import sys


def tree_walk(tree, root):
    preorder_walk(tree, root)
    inorder_walk(tree, root)
    postoder_walk(tree, root)


def preorder_walk(tree, root):
    print("Preorder")
    result = []

    def preorder_walk_rec(node):
        if node == -1:
            pass
        else:
            result.append(str(node))
            preorder_walk_rec(tree[node][1])
            preorder_walk_rec(tree[node][2])

    preorder_walk_rec(root)
    print(" " + " ".join(result))


def inorder_walk(tree, root):
    print("Inorder")
    result = []

    def inorder_walk_rec(node):
        if node == -1:
            pass
        else:
            inorder_walk_rec(tree[node][1])
            result.append(str(node))
            inorder_walk_rec(tree[node][2])

    inorder_walk_rec(root)
    print(" " + " ".join(result))


def postoder_walk(tree, root):
    print("Postorder")
    result = []

    def postoder_work_rec(node):
        if node == -1:
            pass
        else:
            postoder_work_rec(tree[node][1])
            postoder_work_rec(tree[node][2])
            result.append(str(node))

    postoder_work_rec(root)
    print(" " + " ".join(result))


def get_tree():
    n = int(input())
    tree = [[-1, -1, -1] for x in range(0, n)]
    for node in sys.stdin.readlines():
        _id, left, right = [int(x) for x in node.split()]
        if left >= 0:
            tree[left][0] = _id
            tree[_id][1] = left
        if right >= 0:
            tree[right][0] = _id
            tree[_id][2] = right
    return tree


def get_root(tree):
    for i, node in enumerate(tree):
        if node[0] == -1:
            return i
    raise ValueError


if __name__ == "__main__":
    tree = get_tree()
    tree_walk(tree, get_root(tree))