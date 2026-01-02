class Node:
    def __init__(self):
        self.parent=-1
        self.left=-1
        self.right=-1

nodeList=[]
depthList=[]
heightList=[]

def readinput():
    global nodeList

    n=int(input())
    nodeList = [Node() for _ in range(n)]
    for _ in range(n):
        id,left,right = list(map(int,input().split()))
        nodeList[id].left=left
        if(left!=-1):
            nodeList[left].parent=id
        nodeList[id].right=right
        if(right!=-1):
            nodeList[right].parent=id
        #print('[id,l,r]: ',end=''); print(id,left,right)
        #printNodeList()
    return

def printNodeList():
    global nodeList
    print('\n[printNodeList]')
    for i,node in enumerate(nodeList):
        print(i, node.parent, node.left, node.right)
    print('')

def findRoot():
    global nodeList

    for i, node in enumerate(nodeList):
        if node.parent==-1:
            return i

def getDepth(p,d):
    global depthList
    global nodeList

    depthList[p]=d
    l=nodeList[p].left
    if(l!=-1):
        getDepth(l,d+1)
    r=nodeList[p].right
    if(r!=-1):
        getDepth(r,d+1)

def getHeight(p):
    global heightList
    global nodeList

    pnode=nodeList[p]
    if(pnode.left==-1 and pnode.right==-1):
        heightList[p]=0
    elif(pnode.left==-1):
        heightList[p]=getHeight(pnode.right)+1
    elif(pnode.right==-1):
        heightList[p]=getHeight(pnode.left)+1
    else:
        heightList[p]=max(getHeight(pnode.left),getHeight(pnode.right))+1
    return heightList[p]

def nodeType(id):
    global nodeList

    node=nodeList[id]
    if(node.parent==-1):
        return 'root'
    elif(node.left==-1 and node.right==-1):
        return 'leaf'
    else:
        return 'internal node'

def getSibling(id):
    global nodeList

    node=nodeList[id]
    if(node.parent==-1):
        return -1
    parent=nodeList[node.parent]
    if(parent.left==id):
        return parent.right
    else:
        return parent.left

def getChild(id):
    global nodeList

    node=nodeList[id]
    if (node.left==-1 and node.right==-1):
        return 0
    elif (node.left==-1 or node.right==-1):
        return 1
    else:
        return 2

def main():
    global nodeList
    global depthList
    global heightList
    depthList = [0]*len(nodeList)
    heightList = [0]*len(nodeList)

    root=findRoot()
    getDepth(root,0)
    getHeight(root)

    for i,node in enumerate(nodeList):
        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'\
            .format(i, node.parent, getSibling(i), getChild(i), depthList[i], heightList[i], nodeType(i) ))


    return

if __name__=='__main__':
    readinput()
    main()
