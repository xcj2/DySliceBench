"""
根付き木を構成する
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

def getDepth(node_id):
    d = 0
    target = nodes[node_id]
    while target.parent != -1:
        d += 1
        tmp_num = target.parent
        target = nodes[tmp_num]
    return d

def getParent(node_id):
    target = nodes[node_id]
    return target.parent

def getDegree(node_id):
    target = nodes[node_id]
    count = 0
    if target.children[0] != -1:
        count += 1
    if target.children[1] != -1:
        count += 1
    return count

def getType(node_id):
    target = nodes[node_id]
    if target.parent == -1:
        return 'root'
    elif target.children[0] == -1 and target.children[1] == -1:
        return 'leaf'
    else:
        return 'internal node'

def getSibling(node_id):
    target = nodes[node_id]
    if not target.parent == -1:
        brother_list = copy.copy(nodes[target.parent].children)
        brother_list.remove(node_id)
        return brother_list[0]
    else:
        return -1

def getChildren(node_id):
    target= nodes[node_id]
    return target.children

def getHeight(node_id, h): #このhに結果を保持してく
    target = nodes[node_id]
    h1 = 0
    h2 = 0
    if target.children[0] != -1:
        h1 = getHeight(target.children[0], h)+1
    if target.children[1] != -1:
        h2 = getHeight(target.children[1], h)+1
    h = max(h1, h2)
    return h



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


for i in range(n):
    ans = 'node '+str(i)+': ' +\
          'parent = '+str(getParent(i))+', ' +\
          'sibling = '+str(getSibling(i))+', ' +\
          'degree = '+str(getDegree(i))+', ' +\
          'depth = '+str(getDepth(i))+', '+\
          'height = '+str(getHeight(i, h=0))+', ' +\
           getType(i)
    print(ans)


    

