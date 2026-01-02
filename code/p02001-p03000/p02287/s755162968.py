n = int(input())
elements = list(map(int,input().split(" ")))

class Node():
    def __init__(self,value):
        self.value = value
        self.parent = -1
        self.kids = []

    def addParent(self,parent):
        self.parent = parent

    def addKid(self,kids):
        self.kids = kids

nodes = {}
for i in range(len(elements)):
    nodes[i] = Node(int(elements[i]))

parentIndex = 0
def checkKids(index):
    leftKid = index*2+1
    rightKid = index*2+2
    kids = []
    if leftKid in nodes:
        kids.append(leftKid)
        nodes[leftKid].addParent(index)
        checkKids(leftKid)
    if rightKid in nodes:
        kids.append(rightKid)
        nodes[rightKid].addParent(index)
        checkKids(rightKid)
    nodes[index].addKid(kids)

checkKids(parentIndex)

for id in nodes:
    ans = ""
    ans += "node " + str(id+1)
    ans += ": key = " + str(nodes[id].value)
    if not nodes[id].parent == -1:
        ans += ", parent key = " + str(nodes[nodes[id].parent].value)
    if len(nodes[id].kids) == 1:
        ans += ", left key = " + str(nodes[nodes[id].kids[0]].value)
    elif len(nodes[id].kids) == 2:
        ans += ", left key = " + str(nodes[nodes[id].kids[0]].value)
        ans += ", right key = " + str(nodes[nodes[id].kids[1]].value)
    print(ans + ", ")

