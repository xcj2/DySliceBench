# coding=utf-8
class Node():
    # About Type
    # parent = -1 ==> Root ==> 0
    # child = [] ==> Leaf ==> 1
    # others ==> Internal ==> 2
    def __init__(self, id, parent, child):
        self.id = id
        self.parent = parent
        self.child = child

    def update(self):
        self.depth = 0
        back = -1
        if self.parent == -1:
            self.Type = "root"
            back = self.id
        elif self.child == []:
            self.Type = "leaf"
        else :
            self.Type = "internal node"
        return back

    def printInfo(self):
        print("node " + str( self.id ), end = ": " )
        print("parent = " + str( self.parent ), end = ", " )
        print("depth = " + str( self.depth ), end = ", " )
        print( self.Type, end = ", " )
        print("[", end="")
        length = len( self.child )
        for i in self.child[0: length - 1]:
            print(str(i), end=", ")
        if length > 0:
            print( str(self.child[length-1]) , end="")
        print("]")


    def calcDepth(self, Tree):
        if self.parent == -1:
            self.depth = 0
        else :
            self.depth = Tree[self.parent].depth + 1
        for i in self.child:
            Tree[i].calcDepth(Tree)


def main():
    # データ入力
    n = int( input() )
    InputData = []
    Tree = {} # Nodeクラスのディクショナリ

    tmp = []
    for i in range(n):
        tmp = [int(x) for x in input().split()] # [Node, num, 子1, 子2, ...]
        InputData.append(tmp)
        # Treeの初期化
        Tree[tmp[0]] = Node(tmp[0], -1, tmp[2: 2+tmp[1]])

    for val in Tree.values():
        for i in val.child:
            Tree[i].parent = val.id

    for key in Tree.keys():
        tmp = Tree[key].update()
        if tmp != -1:
            root = tmp

    Tree[root].calcDepth(Tree)

    keys = list(Tree.keys())
    keys.sort()

    for key in keys:
        Tree[key].printInfo()

if __name__ == '__main__':
    main()

