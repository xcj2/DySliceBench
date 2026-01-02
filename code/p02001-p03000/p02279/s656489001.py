class tree:
    def __init__(self, node, children):
        self.node = node
        self.children = children
        self.feature = None
        self.parent = None
        self.depth = 0


def set_feature(info_list):
    for info in info_list:
        if info.depth == 0:
            info.feature = 'root'
        else:
            if len(info.children) == 0:
                info.feature = 'leaf'
            else:
                info.feature = 'internal node'

def get_root_node(info_list):
    cand_nodes = []
    remove_node = []
    for info in info_list:
        if len(info.children) != 0:
            cand_nodes.append(info.node)
            remove_node.extend(info.children)
    if len(cand_nodes) == 1:
        return cand_nodes[0]
    elif len(cand_nodes) == 0:
        return info_list[0].node
    else:
        co_value = (set(cand_nodes) ^ set(remove_node)) & set(cand_nodes)
    return co_value.pop()
    
def set_parent(info_list):
    for info in info_list:
        if info.feature == 'root':
            info.parent = -1
        children = info.children
        for child in children:
            info_list[child].parent = info.node

def set_depth(child, depth, node_infos):
    if len(node_infos[child].children) == 0:
        node_infos[child].depth = depth
    else:
        depth += 1
        children = node_infos[child].children
        for child in children:
            info_list[child].depth = depth
            set_depth(child, depth, node_infos)
        

N = int(input())
info_list = [0] * N
for i in range(N):
    info = [int(i) for i in input().split()] 
    node_num = info.pop(0)
    nchild = info.pop(0)
    info_list[node_num] = tree(node_num, info)

root_node = get_root_node(info_list)
set_depth(root_node, 0, info_list)

for info in info_list:
    if info.depth == 0:
        info.feature = 'root'
    else:
        if len(info.children) == 0:
            info.feature = 'leaf'
        else:
            info.feature = 'internal node'

for info in info_list:
    if info.feature == 'root':
        info.parent = -1
    children = info.children
    for child in children:
        info_list[child].parent = info.node

for info in info_list:
    print('node {}: parent = {}, depth = {}, {}, {}'.format(
        info.node, info.parent, info.depth, info.feature, info.children
    )
)




