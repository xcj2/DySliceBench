from collections import deque
import sys

sys.setrecursionlimit(200000)

N, ko, oni = map(int, input().split())


class Node:
    def __init__(self):
        self.parent = -1
        self.child = []
        self.depth = -1

    def add_child(self, num):
        self.child.append(num)

    def set_parent(self, num):
        self.parent = num

    def set_depth(self, num):
        self.depth = num

    def children(self):
        for i in self.child:
            if i != self.parent:
                yield i


node_list = [Node() for _ in range(N + 1)]


def get_most_deep(parent_node):
    ret = -1

    if len(node_list[parent_node].child) == 1:
        return node_list[parent_node].depth

    for child_node in node_list[parent_node].children():
        ret = max(ret, get_most_deep(child_node))

    return ret


for _ in range(N - 1):
    A, B = map(int, input().split())
    node_list[A].add_child(B)
    node_list[B].add_child(A)

q = deque()
q.append([oni, 0])

while len(q) > 0:
    val = q.pop()
    parent = val[0]
    gen = val[1]
    node_list[parent].set_depth(gen)
    for child in node_list[parent].children():
        q.append([child, gen + 1])
        node_list[child].set_parent(parent)

ko_gen = node_list[ko].depth
up_count = (ko_gen - 1) // 2

point = ko

for _ in range(up_count):
    point = node_list[point].parent

ans = 0
ans += get_most_deep(point) - ko_gen
ans += ko_gen - 1

print(ans)