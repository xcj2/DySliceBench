
class Node:
    id = None
    depth = None
    degree = None
    parent = None
    children = None

    def __init__(self, id):
        self.id = id

    def __str__(self):
        if self.degree == 0:
            children_str = '[]'
        else:
            children_id = []
            for child in self.children:
                children_id.append(child.id)
            children_str = '[' + ', '.join(map(str, children_id)) + ']'

        return 'node {}: parent = {}, depth = {}, {}, {}'.format(self.id, self.parent, self.depth, self.get_type(), children_str)

    def get_type(self):
        if self.depth == 0:
            return 'root'
        elif self.degree == 0:
            return 'leaf'
        else:
            return 'internal node'

    def add_child(self, child):
        if self.children is None:
            self.children = []
            self.children.append(child)
        else:
            self.children.append(child)


def set_children_depth(node):
    if node.degree != 0:
        for child in node.children:
            child.depth = node.depth + 1
            set_children_depth(child)


n = int(input())

nodes = []
for i in range(n):
    nodes.append(Node(i))
# nodes[0].depth = 0
# nodes[0].parent = -1
#
# for i in range(n):
#     _ = list(map(int, input().split()))
#     nodes[i].degree = _[1]
#
#     if _[1] >= 1:
#         nodes[i].children = _[2:]
#         for j in range(_[1]):
#             nodes[_[j+2]].depth = nodes[i].depth + 1
#             nodes[_[j+2]].parent = i
#
# for i in range(n):
#     print(nodes[i])

for i in range(n):
    _ = list(map(int, input().split()))
    # print(_)
    id = _[0]
    nodes[id].degree = _[1]
    if _[1] >= 1:
        for j in range(_[1]):
            nodes[id].add_child(nodes[_[j+2]])
            nodes[_[j+2]].parent = id
    # print(nodes[i])

root_id = -1
for i in range(n):
    if nodes[i].parent is None:
        nodes[i].parent = -1
        nodes[i].depth = 0
        root_id = i
        break

# for i in range(n):
#     print(nodes[i])
#     print(nodes[i].degree)

set_children_depth(nodes[root_id])

for i in range(n):
    print(nodes[i])

