"""
与えられた二分木の全ての節点を体系的に訪問する
"""
import copy

class Node:
    def __init__(self):
        self.parent = -1
        self.depth = 0
        self.children = []

#空の木の構成
#node_idをインデックスに持たせる
n = int(input())
nodes = []
for _ in range(n):
    node = Node()
    nodes.append(node)

#木の構成
for i in range(n):
    l = list(map(int, input().split()))
    node_id = l[0]

    for j in range(2):
        try:
            child = l[1+j] #l[1+j]というのは子供の番号
            nodes[node_id].children.append(child) 
            if not child == -1:
                nodes[child].parent = node_id #子一人当たり親は必ず一人
        except:
            pass #エラー回避
    else:
        pass #子がいないとき

def getRoot(node_id):
    target = nodes[node_id]
    if target.parent == -1:
        return node_id

def preParse(node_id):
    if node_id == -1:
        return
    print(' '+str(node_id), end='')
    preParse(nodes[node_id].children[0])
    preParse(nodes[node_id].children[1])

def inParse(node_id):
    if node_id == -1:
        return
    inParse(nodes[node_id].children[0])
    print(' '+str(node_id), end='')
    inParse(nodes[node_id].children[1])

def postParse(node_id):
    if node_id == -1:
        return
    postParse(nodes[node_id].children[0])
    postParse(nodes[node_id].children[1])
    print(' '+str(node_id), end='')

root_id = 0
for i in range(n):
    target = nodes[i]
    if target.parent == -1:
        root_id = i
        break

print('Preorder')
preParse(root_id)
print('\nInorder')
inParse(root_id)
print('\nPostorder')
postParse(root_id)
print()



