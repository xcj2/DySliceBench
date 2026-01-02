class Node:
    def __init__(self,key,left,right,parent):
        self.key = key
        self.left = left
        self.right = right
        self.p = parent

    def __repr__(self):
        return str(self.key)

def insert(T, z):
    y = None
    x = T 
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    #print(x,y,z)
    if y == None:
        #print("Y==None")
        T = z
        print(T)
    elif z.key<y.key:
        #print("z.key<y.key")
        y.left = z
    else:
        #print("z.key<y.key")
        y.right = z

def printPreorder(x):
    if x == None:
        return
    printPreorder(x.left)
    print(end=' ')
    print(x,end='')
    printPreorder(x.right)

def printMidorder(x):
    if x == None:
        return
    print(end=' ')
    print(x,end='')
    printMidorder(x.left)
    printMidorder(x.right)

def printal(x):
    printPreorder(x)
    print()
    printMidorder(x)
    print()


N = int(input())
Q = input().split()
T = Node(int(Q[1]),None,None,None)
for i in range(N-1):
    Q = input().split()
    if Q[0] == "print":
        printal(T)
        continue
    insert(T,Node(int(Q[1]),None,None,None))

