"""
根付き木を構成する
"""
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

def getChildren(node_id):
    target = nodes[node_id]
    return target.children

def getType(node_id):
    target = nodes[node_id]
    if target.parent == -1:
        return 'root'
    elif len(target.children) == 0:
        return 'leaf'
    else:
        return 'internal node'


#木の構成
for i in range(n):
    l = list(map(int, input().split()))
    node_id = l[0]
    num = l[1]

    for j in range(num):
        try:
            child = l[2+j] #l[2+j]というのは子供の番号
            nodes[node_id].children.append(child) 
            nodes[child].parent = node_id #子一人当たり親は必ず一人
        except:
            pass
    else:
        pass #子がいないとき


for i in range(n):
    ans = 'node '+str(i)+': parent = '+str(getParent(i))+', ' +\
    'depth = '+str(getDepth(i))+', '+getType(i)+', '+str(getChildren(i))
    print(ans)
    

