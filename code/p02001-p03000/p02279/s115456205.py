from typing import List

# id
# k 子の数
# 子のID


class Node:
    node_id = -999
    child = []
    parent = -1
    depth = -999
    node_type = 'Not set'

    def __init__(self, id: int, child: List[int]):
        self.node_id = id
        self.child = child

    def show(self):
        out = f'node {self.node_id}: '
        out += f'parent = {self.parent}, depth = {self.depth}, '
        out += f'{self.node_type}, '
        tmp = ', '.join(map(str, self.child))
        out += f'[{tmp}]'
        print(out)

    def get_value(self):
        return self.node_id


def show(node_list: List[Node]):
    for n in node_list:
        n.show()


def get_parent(node_id: int) -> int:
    return node_list[node_id].parent


def set_depth(node_id: int, depth: int):
    node_list[node_id].depth = depth
    for ch in node_list[node_id].child:
        set_depth(ch, depth + 1)


def set_node_info(node_list: List[Node]):

    # depthを設定する。
    for target in node_list:
        if target.parent == -1:
            set_depth(target.node_id, 0)
            break

    # typeを設定する。
    for target in node_list:
        if target.depth == 0:
            target.node_type = 'root'
        elif target.depth > 0:
            target.node_type = \
                'leaf' if len(target.child) == 0 else 'internal node'
        else:
            raise ValueError()


n = int(input())
node_list = []
for _i in range(n):
    node_list.append(Node(_i, []))

for _i in range(n):
    line = [int(i) for i in input().split()]
    node_id = line[0]
    num = line[1]

    # 親子関係を設定する。
    for i in range(num):
        child_id = line[2 + i]
        node_list[node_id].child.append(child_id)
        node_list[child_id].parent = node_id

set_node_info(node_list)
show(node_list)


