"""
ALDS1_8_C
螺旋本を参考にしています
"""
import copy

class Node:
    def __init__(self, node_id, parent=None, left=None, right=None):
        self.node_id = node_id
        self.parent = parent
        self.left = left
        self.right = right

class Tree:
    def insert_root_node(self, new_id):
        global root_node 
        root_node = Node(new_id)

    def insert_node(self, new_id): 
        compare_node = root_node 
        new_node = Node(new_id)
        while compare_node is not None: 
            new_node.parent = compare_node 
            if compare_node.node_id < new_id:
                compare_node = compare_node.right
            else:
                compare_node = compare_node.left

        if new_node.parent.node_id < new_id:
            new_node.parent.right = new_node
        else:
            new_node.parent.left = new_node


    def find(self, search_id):
        tmp_node = root_node
        while tmp_node:
            if tmp_node.node_id == search_id:
                print('yes')
                return
            elif tmp_node.node_id < search_id:
                tmp_node = tmp_node.right
            else:
                tmp_node = tmp_node.left
        print('no')

    #search_nodeを根とする右部分技の最も小さいノードを取得する
    def getTheLeft(self, search_node): 
        while search_node.left:
            search_node = search_node.left
        return search_node

    def delete(self, search_id):
        tmp_node = root_node
        while tmp_node:
            if tmp_node.node_id == search_id:
                if tmp_node.left is None and tmp_node.right is None:
                    if tmp_node.parent.node_id < search_id:
                        tmp_node.parent.right = None
                    else:
                        tmp_node.parent.left = None
                    return
                elif tmp_node.left is None and tmp_node.right is not None:
                    tmp_node.right.parent = tmp_node.parent
                    if tmp_node.parent.node_id < search_id:
                        tmp_node.parent.right = tmp_node.right
                    else:
                        tmp_node.parent.left = tmp_node.right
                    return
                elif tmp_node.left is not None and tmp_node.right is None:
                    tmp_node.left.parent = tmp_node.parent
                    if tmp_node.parent.node_id < search_id:
                        tmp_node.parent.right = tmp_node.left
                    else:
                        tmp_node.parent.left = tmp_node.left
                    return
                else:
                    left_node = tmp_node.right
                    left_node = self.getTheLeft(left_node) 
                    if left_node.parent.node_id < left_node.node_id: 
                        left_node.parent.right = None
                        left_node.parent = None
                    else:
                        left_node.parent.left = None
                        left_node.parent = None
                    tmp_node.node_id = left_node.node_id
                    return

            elif tmp_node.node_id < search_id:
                tmp_node = tmp_node.right
            else:
                tmp_node = tmp_node.left
#------------------------------------------------

def inParse(tmp_node):
    if not tmp_node:
        return
    inParse(tmp_node.left)
    print(' '+str(tmp_node.node_id), end='')
    inParse(tmp_node.right)
        
def preParse(tmp_node):
    if not tmp_node:
        return
    print(' '+str(tmp_node.node_id), end='')
    preParse(tmp_node.left)
    preParse(tmp_node.right)

#------------------------------------------------


tree = Tree()

n = int(input())
root_id = 0
root_node = None
for i in range(n):
    order = input().split()
    if not root_node: #何も入ってない時
        root_id = int(order[1])
        tree.insert_root_node(int(order[1]))
    elif order[0][0] == 'i':
        new_id = int(order[1])
        tree.insert_node(new_id)
    elif order[0][0] == 'p':
        node = copy.copy(root_node)
        inParse(node)
        print()
        node = copy.copy(root_node)
        preParse(node)
        print()
    elif order[0][0] == 'f':
        tree.find(int(order[1]))
    elif order[0][0] == 'd':
        tree.delete(int(order[1]))



