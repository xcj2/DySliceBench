class Node:
    def __init__(self, id_num):
        self.id = id_num
        self.parent = None
        self.children = []
    def get_type(self):
        if self.parent is None:
             return 'root'
        if self.children == []:
             return 'leaf'
        else:
             return 'internal node'
             
def get_depth(node, nodes):
    depth = 0
    parent = node.parent
    while parent is not None:
        depth += 1
        parent = nodes[parent].parent
    return depth
 
n = int(input())
nodes = {}
for i in range(n):
    input_line = list(map(int , input().split(' ')))
    id = input_line[0]
    children = input_line[2:]
    if id not in nodes:
        node = Node(id)
        node.children = children
        nodes[id] = node
    else:
        nodes[id].children = children
    for ch in children:
        if ch not in nodes:
            ch_node = Node(ch)
            nodes[ch] = ch_node
            nodes[ch].parent = id
        else:
            nodes[ch].parent = id
for id in sorted(nodes):
    node = nodes[id]
    parent = node.parent
    if node.parent is None:
         parent = -1
    depth = get_depth(node, nodes)
    type = node.get_type()
    print('node {}: parent = {}, depth = {}, {}, {}'.format(id, parent, depth, type, node.children))
