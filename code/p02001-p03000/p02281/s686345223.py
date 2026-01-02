class Node:
    def __init__(self):
        self.parent=-1
        self.left=-1
        self.right=-1


nodeList=[]
preOrderList=[]
inOrderList=[]
postOrderList=[]

def readinput():
    global nodeList

    n=int(input())
    nodeList=[Node() for _ in range(n)]
    for _ in range(n):
        id,l,r=list(map(int,input().split()))
        nodeList[id].left=l
        nodeList[id].right=r
        if(l!=-1):
            nodeList[l].parent=id
        if(r!=-1):
            nodeList[r].parent=id
    
def findRoot():
    global nodeList

    for i,node in enumerate(nodeList):
        if node.parent==-1:
            return i
    return -1

def getPreOrder(id):
    global nodeList
    global preOrderList

    preOrderList.append(id)
    node=nodeList[id]
    if(node.left!=-1):
        getPreOrder(node.left)
    if(node.right!=-1):
        getPreOrder(node.right)

def getInOrder(id):
    global nodeList
    global inOrderList

    node=nodeList[id]
    if(node.left!=-1):
        getInOrder(node.left)
    inOrderList.append(id)
    if(node.right!=-1):
        getInOrder(node.right)
    
def getPostOrder(id):
    global nodeList
    global postOrderList

    node=nodeList[id]
    if(node.left!=-1):
        getPostOrder(node.left)
    if(node.right!=-1):
        getPostOrder(node.right)
    postOrderList.append(id)

def main():
    global nodeList

    root=findRoot()
    getPreOrder(root)
    getInOrder(root)
    getPostOrder(root)
    print('Preorder')
    print(' ',end='');print(' '.join(map(str,preOrderList)))
    print('Inorder')
    print(' ',end='');print(' '.join(map(str,inOrderList)))
    print('Postorder')
    print(' ',end='');print(' '.join(map(str,postOrderList)))

if __name__=='__main__':
    readinput()
    main()

