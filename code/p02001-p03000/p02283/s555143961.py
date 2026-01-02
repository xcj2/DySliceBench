import collections
sent = -1

def insert(hoge, new_node, root):
    #print(hoge)
    parent_maybe = sent
    now_looking = root
    hoge[new_node]['node_id'] = new_node
    while now_looking != sent:
        parent_maybe = now_looking
        if new_node < hoge[now_looking]['node_id']:
            now_looking = hoge[now_looking]['left']
        else:
            now_looking = hoge[now_looking]['right']
    hoge[new_node]['parent'] = parent_maybe
    
    if parent_maybe == sent:
        root = new_node
        hoge[new_node]['parent'] = sent
        hoge[new_node]['left'] = sent
        hoge[new_node]['right'] = sent
    elif new_node < hoge[parent_maybe]['node_id']:
        hoge[parent_maybe]['left'] = new_node
        hoge[new_node]['left'] = sent
        hoge[new_node]['right'] = sent
    else:
        hoge[parent_maybe]['right'] = new_node
        hoge[new_node]['left'] = sent
        hoge[new_node]['right'] =sent
    
    return root
    
def inorder(node_id):
    if node_id == sent:
        return None
    inorder(hoge[node_id]['left'])
    print(' {}'.format(node_id), end='')
    inorder(hoge[node_id]['right'])

def preorder(node_id):
    if node_id == sent:
        return None
    print(' {}'.format(node_id), end='')
    preorder(hoge[node_id]['left'])
    preorder(hoge[node_id]['right'])
    
    
def getTree(root):
    inorder(root)
    print()
    preorder(root)
    print()

if __name__ == '__main__':
    num = int(input())
    hoge = collections.defaultdict(dict)
    root = -1
    for _ in range(num):
        command = input()
        if command.split()[0] == 'insert':
            root = insert(hoge, int(command.split()[1]), root)
        else:
            getTree(root)
