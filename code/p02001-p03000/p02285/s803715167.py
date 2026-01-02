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

def bisearch(p,op):
    '''再帰を使わないバージョン
    '''
    global T

    x=p
    while(x != -1 and T[x].key != op):
        if (op < T[x].key):
            x=T[x].left
        else:
            x=T[x].right
    return x


def find(op):
    ans=bisearch(root,op)
    if(ans!=-1):
        print('yes')
    else:
        print('no')

def delete1(target):
    '''子を持たないノードの削除
    '''
    global T

    node=T[target]
    parent=T[node.parent]
    if (T[parent.left].key==node.key):
        parent.left=-1
    else:
        parent.right=-1
    node.parent=-1

def delete2(target):
    '''子を1個持つノードの削除
    '''
    global T

    node=T[target]
    parent=T[node.parent]
    if(node.left!=-1):
        childIdx=node.left
        node.left=-1
    else:
        childIdx=node.right
        node.right=-1
    if(T[parent.left].key==node.key):
        parent.left=childIdx
    else:
        parent.right=childIdx
    T[childIdx].parent=node.parent
    node.parent=-1

def delete3(target):
    '''子を2子持つノード
    '''
    global T
    global inorderList

    #print('[delete3]:{}'.format(T[target].key))
    node=T[target]
    inorderList=[]
    getInorderList(node.right) # ; printInorderList()
    nextIdx=inorderList[0]
    node.key=T[nextIdx].key
    nextType=getType(nextIdx)
    if(nextType==1):
        delete1(nextIdx)
    else:
        delete2(nextIdx)


def getType(target):
    global T

    node=T[target]
    if(node.left==-1 and node.right==-1):
        return 1
    elif(node.left==-1 or node.right==-1):
        return 2
    else:
        return 3

def delete(op):
    target=bisearch(root,op)
    type=getType(target)
    if(type==1):
        delete1(target)
    elif(type==2):
        delete2(target)
    else:
        delete3(target)
    
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
        elif(command=='find'):
            find(op)
        elif(command=='delete'):
            delete(op)
        elif(command=='print'):
            printT()

if __name__=='__main__':
    readinput()
    main()
