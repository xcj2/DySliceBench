import copy

N, M = [ int(x) for x in input().split() ]

class Node:
    def __init__(self, id):
        self.id = id
        self.path = []
    def __str__(self):
        return "id: " + str(self.id) + " path: " + str(self.path)

nodes = []
for i in range(N):
    nodes.append(Node(i))

paths = []
for i in range(M):
    from_id, to_id = [ int(x) - 1 for x in input().split() ]
    paths.append([from_id, to_id])
    nodes[from_id].path.append(to_id)
    nodes[to_id].path.append(from_id)

def if_all_passed(passed_nodes):
    if len(passed_nodes) == N:
        return True
    else:
        return False

def go_child(id_new, passed_nodes):
    passed_nodes.append(id_new)
    if if_all_passed(passed_nodes):
        return True

    for i in nodes[id_new].path:
        if not i in passed_nodes:
            if go_child(i, passed_nodes):
                return True
    return False

count = 0
for ids in paths:
    nodes[ids[0]].path.remove(ids[1])
    nodes[ids[1]].path.remove(ids[0])
    if not go_child(0, []):
        count += 1
    nodes[ids[0]].path.append(ids[1])
    nodes[ids[1]].path.append(ids[0])

print(count)
