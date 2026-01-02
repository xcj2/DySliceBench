"""
二分探索木を構成する
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
        global root_node #途中でインスタンス化すると水の泡なんですよ
        root_node = Node(new_id)

    def insert_node(self, root_id, new_id): #new_idは追加するノード
        compare_node = root_node #はじめはrootから比較スタート
        new_node = Node(new_id) #インスタンス化
        while compare_node is not None: #compare_nodeが存在するとき
            #この下の一行は最重要アイディア
            #親の可能性がある時，とりあえず代入して情報を記録しておく
            new_node.parent = compare_node 
            #右か左か
            if compare_node.node_id < new_id:
                compare_node = compare_node.right
            else:
                compare_node = compare_node.left

        #compare_node == Noneの時，上の２つの分岐のどっちからきたかわからない
        #そのため，親と比較し直す必要がある
        if new_node.parent.node_id < new_id:
            new_node.parent.right = Node(new_id)
        else:
            new_node.parent.left = Node(new_id)

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

def find(search_id):
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
        tree.insert_node(root_id, new_id)
    elif order[0][0] == 'p':
        node = copy.copy(root_node)
        inParse(node)
        print()
        node = copy.copy(root_node)
        preParse(node)
        print()
    elif order[0][0] == 'f':
        find(int(order[1]))



