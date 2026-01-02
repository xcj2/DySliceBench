#! /usr/bin/env python3
# # -*- coding: utf-8 -*-


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __iter__(self):
        yield from self.postorder()

    def postorder(self):
        yield from self.left
        yield from self.right
        yield self


def reconstruct(preorder, inorder):
    if len(preorder) == 0:
        return []

    root_val = preorder[0]
    root_index = inorder.index(root_val)
    inorder_left = inorder[:root_index]
    inorder_right = inorder[root_index + 1 :]
    preorder_left = [x for x in preorder if x in inorder_left]
    preorder_right = [x for x in preorder if x in inorder_right]

    return Node(
        root_val,
        reconstruct(preorder_left, inorder_left),
        reconstruct(preorder_right, inorder_right),
    )


def main():
    n = int(input())
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]

    print(*[node.val for node in reconstruct(preorder, inorder).postorder()])


main()

