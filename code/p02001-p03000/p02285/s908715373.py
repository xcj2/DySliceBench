import collections
sent = None

def insert(hoge, new_node, root):
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
    
def searchNode(hoge, num, node_id):
    if node_id == sent:
        return 'no'
    
    if num == node_id:
        return 'yes'
    elif num < node_id:
        return searchNode(hoge, num, hoge[node_id]['left'])
    elif num > node_id:
        return searchNode(hoge, num, hoge[node_id]['right'])

def deleteNode(hoge, node_id):
    left_child = hoge[node_id]['left']
    right_child = hoge[node_id]['right']
    parent = hoge[node_id]['parent']
    if left_child == sent and right_child == sent:
        if hoge[parent]['left'] == node_id:
            hoge[parent]['left'] = sent
        else:
            hoge[parent]['right'] = sent
    elif left_child == sent and right_child != sent:
        if hoge[parent]['left'] == node_id:
            hoge[parent]['left'] = right_child
        else:
            hoge[parent]['right'] = right_child 
        hoge[right_child]['parent'] = parent
    elif right_child == sent and left_child != sent:
        if hoge[parent]['left'] == node_id:
            hoge[parent]['left'] = left_child
        else:
            hoge[parent]['right'] = left_child
        hoge[left_child]['parent'] = parent
    else:
        min_node = getMin(hoge, hoge[node_id]['right'])
        min_parent = hoge[min_node]['parent']
        if hoge[min_node]['right'] == sent:
            flag = True
        else:
            flag = False
        hoge[left_child]['parent'] = min_node
        hoge[right_child]['parent'] = min_node
        hoge[min_node]['left'] = left_child
        if min_node != right_child:
            hoge[min_node]['right'] = right_child
        hoge[min_node]['parent'] = parent
        if hoge[parent]['left'] == node_id:
            hoge[parent]['left'] = min_node
        else:
            hoge[parent]['right'] = min_node
            
        if flag:
            hoge[min_parent]['left'] = sent
        else:
            min_node_rchild = hoge[min_node]['right']
            hoge[min_parent]['left'] = min_node_rchild
            hoge[min_node_rchild]['parent'] = min_parent
    del hoge[node_id]
        
def getMin(hoge, node_id):
    while hoge[node_id]['left'] != sent:
        node_id = hoge[node_id]['left']
    return node_id

if __name__ == '__main__':
    num = int(input())
    hoge = collections.defaultdict(dict)
    root = sent
    for _ in range(num):
        command = input()
        if command.split()[0] == 'insert':
            root = insert(hoge, int(command.split()[1]), root)
        elif command.split()[0] == 'find':
            print(searchNode(hoge, int(command.split()[1]), root))
        elif command.split()[0] == 'delete':
            deleteNode(hoge, int(command.split()[1]))
        else:
            getTree(root)

