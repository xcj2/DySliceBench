import sys

class Node:
    def __init__(self):
        self.parent=-1
        self.left=-1
        self.right=-1

depthList = []
nodeList = []

def readinput():
    global nodeList
    n=int(input())
    nodeList=[Node() for _ in range(n)]
    for _ in range(n):
        s=list(map(int,input().split()))
        id=s[0]
        deg=s[1]
        child=s[2:]
        if (deg>0):
            nodeList[id].left=child[0]
            for i in range(deg-1):
                nodeList[child[i]].parent=id
                nodeList[child[i]].right=child[i+1]
            nodeList[child[deg-1]].parent=id
    return

def findRoot(nodeList):
    for i, node in enumerate(nodeList):
        if(node.parent==-1):
            return i
    return -1

def setDepth(id,depth):
    #sys.setrecursionlimit(3700)
    global depthList
    global nodeList

    depthList[id]=depth
    r=nodeList[id].right
    #if(r!=-1):
    #    setDepth(r,depth)
    while(r!=-1):
        depthList[r]=depth
        if(nodeList[r].left!=-1):
            setDepth(nodeList[r].left,depth+1)
        r=nodeList[r].right
    l=nodeList[id].left
    if(l!=-1):
        setDepth(l,depth+1)

def nodeType(node):
    if node.parent==-1:
        return 'root'
    elif node.left==-1:
        return 'leaf'
    else:
        return 'internal node'

def childList(p, nodeList):
    child=[]
    c=nodeList[p].left
    while(c!=-1):
        child.append(c)
        c=nodeList[c].right
    return child

def printNodeList(nodeList, depthList):
    for i,node in enumerate(nodeList):
        print('node {}: parent = {}, depth = {}, {}, {}'.format(i,node.parent, depthList[i], nodeType(node), childList(i,nodeList)))

def main():
    global depthList
    global nodeList

    depthList=[0]*len(nodeList)
    root=findRoot(nodeList)
    setDepth(root,0)
    printNodeList(nodeList, depthList)

if __name__=='__main__':
    sys.setrecursionlimit(10000)
    readinput()
    main()

