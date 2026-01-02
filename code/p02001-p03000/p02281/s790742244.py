from typing import List


class Node:
    left = -1
    right = -1
    parent = -1


def get_root(nodes: List[int]) -> int:
    for i, node in enumerate(nodes):
        if node.parent == -1:
            return i


def show_preorder(node_id: int)-> None:
    print(f' {node_id}', end='')
    if nodes[node_id].left != -1:
        show_preorder(nodes[node_id].left)
    if nodes[node_id].right != -1:
        show_preorder(nodes[node_id].right)


def show_inorder(node_id: int)-> None:
    left = nodes[node_id].left
    if left != -1:
        show_inorder(left)

    print(f' {node_id}', end='')

    right = nodes[node_id].right
    if right != -1:
        show_inorder(right)


def show_postorder(node_id: int) -> None:
    left = nodes[node_id].left
    if left != -1:
        show_postorder(left)

    right = nodes[node_id].right
    if right != -1:
        show_postorder(right)

    print(f' {node_id}', end='')


N = int(input())
nodes = [Node() for i in range(N)]
for _i in range(N):
    node_id, left, right = map(int, input().split())
    nodes[node_id].left = left
    nodes[node_id].right = right
    if left != -1:
        nodes[left].parent = node_id
    if right != -1:
        nodes[right].parent = node_id
root = get_root(nodes)

print('Preorder')
show_preorder(root)
print()

print('Inorder')
show_inorder(root)
print()

print('Postorder')
show_postorder(root)
print()

