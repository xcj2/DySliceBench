n = int(input())

class Node():
    def __init__(self,id):
        self.id = id
        self.child = []
        self.parent = -1

    def addChild(self,child):
        self.child = child

    def setParent(self,parent):
        self.parent = parent

nodes = {}
for i in range(n):
    line = list(input().split(" "))
    id = int(line[0])
    if not id in nodes:
        nodes[id] = Node(id)
    child = []
    for j in range(1,3):
        if not int(line[j]) == -1:
            child.append(int(line[j]))
    nodes[id].addChild(child)

    for ele in child:
        if not ele in nodes:
            nodes[ele] = Node(ele)
        nodes[ele].setParent(id)

def culcHeight(nodes,id,counter):
    objNode = nodes[id]
    children = objNode.child
    if children == []:
        return counter
    else:
        counter += 1
        results = []
        for chili in children:
            a = culcHeight(nodes,chili,counter)
            results.append(a)
        return max(results)

for i in sorted(nodes):
    node = nodes[i]
    ans = ''
    ans += 'node ' + str(i) + ': parent = '
    ans += str(node.parent) + ', sibling = '


    if node.parent == -1:
        ans += str(-1)
        children = []
    else:
        children = nodes[node.parent].child
        if children == [node.id]:
            ans += str(-1)
        else:
            for k in children:
                if not k == i:
                    ans += str(k)



    ans += ', degree = ' + str(len(node.child))


    ans += ', depth = '


    startnode = node
    count = 0
    while not startnode.parent == -1:
        startnode = nodes[startnode.parent]
        count += 1
    ans += str(count)


    ans += ', height = '
    ans += str(culcHeight(nodes,i,0))
    ans += ', '
    if node.parent == -1:
        type = 'root'
    else:
        if node.child == []:
            type = 'leaf'
        else:
            type = 'internal node'
    ans += type
    print(ans)

