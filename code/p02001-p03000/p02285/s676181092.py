import sys
sys.setrecursionlimit(2**20)  


class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

ROOT = None

def pre_parse(u, pre_ls):
    if u == None:
        return
    pre_ls.append(u.key)
    pre_parse(u.left, pre_ls) 
    pre_parse(u.right, pre_ls)


def in_parse(u, in_ls):
    if u == None:
        return
    in_parse(u.left, in_ls)
    in_ls.append(u.key)
    in_parse(u.right, in_ls)


def insert(value):
    global ROOT
    y = None
    x = ROOT
    z = Node(value)  
    while x != None:
        y = x  
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
            
    z.parent = y

    if y == None:
        ROOT = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z


def find(u, value):
    while u != None and u.key != value:
        if value < u.key:
            u = u.left
        else:
            u = u.right
    return u


def deleteNode(z):
    
    if (z.left == None or z.right == None):
        y = z
    else:
        y = getSucessor(z)

    if y.left is not None:
        x = y.left
    else:
        x = y.right

    if x is not None:
        x.parent = y.parent

    if y.parent is None:
        ROOT = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    if y != z:
        z.key = y.key

def getSucessor(x):
    if x.right is not None:
        return getMinimum(x.right)

    y = x.parent
    
    while y and x == y.right:
        x = y
        y = y.parent
    return y


def getMinimum(x):
    while x.left != None:
        x = x.left
    return x
    
    
def print_result():
    pre_ls, in_ls = [], []
    in_parse(ROOT, in_ls)
    pre_parse(ROOT, pre_ls)
    print('', *in_ls)
    print('', *pre_ls)

n = int(input())

for i in range(n):
    tmp = input()
    if tmp[0] == "p":
        print_result()
    elif tmp[0] == "f":
        if find(ROOT, int(tmp[5:])):
            print("yes")
        else:
            print("no")
    elif tmp[0] == "i":
        insert(int(tmp[7:]))
    else:
        deleteNode(find(ROOT, int(tmp[7:])))

