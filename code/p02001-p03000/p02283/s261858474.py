class Node():
    right = None
    left = None
    def __init__(self, key, parent):
        self.parent = parent
        self.key = key

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, v):
        y = None
        x = self.root
        while x != None:
            y = x
            if v < x.key:
                x = x.left
            else :
                x = x.right
        z = Node(v, y)

        if y == None: # Tが空の時
            self.root = z
        elif v < y.key:
            y.left = z
        else :
            y.right = z

    # 先行
    def printPreorder(self, parent): # 最初はRootを与え再帰的に。
        print( " " + str(parent.key), end="" )
        if parent.left != None:
            self.printPreorder(parent.left)
        if parent.right != None:
            self.printPreorder(parent.right)

    # 中間
    def printInorder(self, parent): # 最初はRootを与え再帰的に。
        if parent.left != None:
            self.printInorder(parent.left)
        print( " " + str(parent.key), end="" )
        if parent.right != None:
            self.printInorder(parent.right)

def main():
    T = Tree()
    Orders =[]
    tmp =[]
    N = int( input() )
    for i in range(N):
        tmp = [input().split()]
        Orders.extend( tmp )

    for order in Orders:
        if order[0] == "insert":
            T.insert( int( order[1] ) )
        elif order[0] == "print":
            T.printInorder( T.root )
            print("")
            T.printPreorder( T.root )
            print("")

if __name__ == '__main__':
    main()

