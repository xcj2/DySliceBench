INFTY=2000000000+1

class Node:
    def __init__(self,key=INFTY):
        self.key=key
        self.parent=-1
        self.left=-1
        self.right=-1

root=-1
T=[]
commands=[]
preorderList=[]
inorderList=[]

def readinput():
    global commands

    n=int(input())
    for _ in range(n):
        s=input().split()
        command=s[0]
        if(len(s)>1):
            op=s[1]
        commands.append((command,int(op)))

def insert(op):
    global T
    global root

    #print('[{}]'.format(op))
    zidx=len(T)
    z=Node(op)
    T.append(z)

    yidx=-1
    xidx=root
    while(xidx != -1):
        x=T[xidx]
        yidx=xidx
        if(z.key<x.key):
            xidx=x.left
            #print('left: {} < {}'.format(z.key, x.key))
        else:
            xidx=x.right
            #print('right')
    z.parent=yidx

    if yidx==-1:
        root=zidx
        #print('root changed')
    elif z.key<T[yidx].key:
        T[yidx].left=zidx
    else:
        T[yidx].right=zidx

def getPreorderList(id):
    global preorderList

    preorderList.append(id)
    node=T[id]
    if(node.left!=-1):
        getPreorderList(node.left)
    if(node.right!=-1):
        getPreorderList(node.right)

def getInorderList(id):
    global inorderList

    node=T[id]
    if(node.left!=-1):
        getInorderList(node.left)
    inorderList.append(id)
    if(node.right!=-1):
        getInorderList(node.right)

def printPreorderList():
    for i in preorderList:
        print(' '+str(T[i].key),end='')
    print('')

def printInorderList():
    for i in inorderList:
        print(' '+str(T[i].key),end='')
    print('')

def printT():
    global inorderList
    global preorderList

    inorderList=[]
    preorderList=[]
    
    getInorderList(root)
    printInorderList()
    getPreorderList(root)
    printPreorderList()
    #for node in T:
    #    print(node.key, node.parent, node.left, node.right)    

def main():
    global commands

    for command,op in commands:
        if(command=='insert'):
            insert(op)
        elif(command=='print'):
            printT()

if __name__=='__main__':
    readinput()
    main()
