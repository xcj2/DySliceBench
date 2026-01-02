class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

root=None

#前序排序
def PreorderTreeWalk(u):
    if u == None:
        return
    print(" %d"%u.key,end='')
    PreorderTreeWalk(u.left)
    PreorderTreeWalk(u.right)

#中序排序
def InorderTreeWalk(u):
    if (u == None):
        return
    InorderTreeWalk(u.left)
    print(" %d"%u.key,end='')
    InorderTreeWalk(u.right)



def insert(value):
    global root
    
    y = None
    x = root
    z = Node(value)
 
    # 从根结点往下遍历
    while (x != None) :
        y = x
        # z 比 x 小， 则从x的左侧遍历
        # z 比 x 大， 则从x的右侧遍历
        if (z.key < x.key):
            x = x.left
        else:
            x = x.right
    

    z.parent = y

    #没有父结点的是root
    if (y == None): 
        root = z
    else: 
        # z 比 y 小， 则在y的左侧
        # z 比 y 大， 则在y的右侧
        if (z.key < y.key):
            y.left = z
        else:
            y.right = z
            
def find(u,value):
    while (u != None and u.key != value): 
        if (value < u.key):
            u = u.left;
        else:
            u = u.right;
    
    return u


# 树的最小值
def treeMinimum(x):
    while (x.left != None):
        x = x.left;
    return x


# case3如果同时具有左右子树。
#可以将结点x的左子树的最大值（也就是左子树一直往右孩子节点遍历即是最大值）
#或者右子树的最小值（也就是右子树一直往左孩子节点遍历即是最小值）替换x，然后拼接左子树或者右子树
#搜索后一个结点
def treeSuccessor(x) :
    if (x.right != None):
        return treeMinimum(x.right)

    y = x.parent;
    
    if x==y.left:
        return y
    else:
        while (y != None and x == y.right) :
            x = y
            x = y.parent
    
    return y


def treeDelete(z) :
        #x没有子结点，则将x结点删除即可 
        #如果x只有左子树或者只有右子树，则将子树拼接上父结点即可  
        # 确定要删除的结点
    if (z.left == None or z.right == None):
        y = z
    else:
        y = treeSuccessor(z)

    # 确定y的子结点x
    if (y.left != None):
        x = y.left
    else:
        x = y.right

    # 让子结点链接父结点
    if (x != None):
        x.parent = y.parent

    # 让父结点链接子结点
    if (y.parent == None):
        root = x
    else:
        if (y == y.parent.left):
            y.parent.left = x
        else:
            y.parent.right = x
    

    #case 3
    if (y != z):
        z.key = y.key;



n=int(input())
s=[]
for i in range(n):
    s=[x for x in input().split()]
    if s[0][0]=='i':
        insert(int(s[1]))    
    elif s[0][0]=='f':
        f = find(root,int(s[1]));
        if (f != None):
            print("yes")
        else:
            print("no")
    elif s[0][0]=='d':
            treeDelete(find(root, int(s[1])));
    else:
        InorderTreeWalk(root)
        print()
            
        PreorderTreeWalk(root)
        print()
       
