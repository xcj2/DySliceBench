#ALDS1_8_B
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.list = []
    
    def insert(self, node_tobe_added):
            y = None #「xの親」って書いてあるけど、「zの親」では？
            x = self.root
            while x != None:
                #ここで親を設定する。xを一つずつ葉に進めて、yに代入する。yがｚの親になる。
                y = x
                if node_tobe_added.key < x.key:
                    x = x.left
                else:
                    x = x.right
            #ここでyがzの親に設定される。
            node_tobe_added.parent = y 
            
            #yがNoneなら何もないということなのでzがrootになる。
            if y == None:
                self.root = node_tobe_added
            elif node_tobe_added.key < y.key:
                #node_tobe_addedをyの左の子にする
                y.left = node_tobe_added
            else:
                #node_tobe_addedをyの右の子にする
                y.right = node_tobe_added
                
    def find(self, key):
        x = self.root
        while x != None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x
                
    def preParse(self, node):
        if node == None:
            return
        self.list.append(node.key)
        self.preParse(node.left)
        self.preParse(node.right)
    
    def inParse(self, node):
        if node == None:
            return
        self.inParse(node.left)
        self.list.append(node.key)
        self.inParse(node.right)

T = Tree()

N = int(input())
for i in range(N):
        order, *key = input().split() #printの場合はkeyがないので、*をつけて配列として扱う。
        if order == "print":
            T.list = []
            T.inParse(T.root)
            print(" " + " ".join(map(str, T.list)))
            T.list = []
            T.preParse(T.root)
            print(" " + " ".join(map(str, T.list)))
        elif order == "insert":#insertの場合
            T.insert(Node(int(key[0]))) #なぜかわからないがintにしないとWAになる。
        else:
            if T.find(int(key[0])):
                print("yes")
            else:
                print("no")
