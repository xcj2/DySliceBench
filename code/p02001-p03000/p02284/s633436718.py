class NullNode():
    def __init__(self):
        self.id = None

null_node = NullNode()
class Node():
    def __init__(self, id):
        global null_node
        self.id = id
        self.parent = null_node
        self.left = null_node
        self.right =  null_node

def preorder(node, out_list=[]):
    if node.id is not None:
        out_list.append(str(node.id))
        out_list = preorder(node.left, out_list)
        out_list = preorder(node.right, out_list)
    return out_list

def inorder(node, out_list=[]):
    if node.id is not None:
        out_list = inorder(node.left, out_list)
        out_list.append(str(node.id))
        out_list = inorder(node.right, out_list)
    return out_list

def insert(node, root_node):
    temp_node_parent = root_node.parent
    temp_node = root_node

    while temp_node.id is not None:
        temp_node_parent = temp_node
        if node.id < temp_node.id:
            temp_node = temp_node.left
        else:
            temp_node = temp_node.right

    node.parent = temp_node_parent
    if node.id < temp_node_parent.id:
        temp_node_parent.left = node
    else:
        temp_node_parent.right = node

def find(id,root_node):
    node = root_node
    while node.id is not None:
        if id < node.id:
            node = node.left
        elif id > node.id:
            node = node.right
        else:
            print('yes')
            break
    else:
        print('no')

import sys


n = int(sys.stdin.readline())
input_lines = sys.stdin.readlines()
root_node = NullNode()
for i in range(n):
    input_line = input_lines[i].split()
    command = input_line[0]
    if command == 'insert':
        id = int(input_line[1])
        id_node = Node(id)
        if root_node.id is None:
            root_node = id_node
        else:
            insert(id_node, root_node)

    elif command == 'find':
        id = int(input_line[1])
        find(id, root_node)

    else:
        inorder_list = inorder(root_node, [])
        preorder_list = preorder(root_node, [])
        out = ' ' + ' '.join(inorder_list)
        print(out)
        out = ' ' + ' '.join(preorder_list)
        print(out)


