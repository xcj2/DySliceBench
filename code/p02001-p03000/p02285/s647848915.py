#ALDS1_8_C
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
    
    def delete(self, node):
        if node.left == None or node.right == None:
            y = node
        else:
            y = self.get_successor(node)
        
        if y.left != None:
            x = y.left
        else:
            x = y.right
        
        if x != None:#nodeの子がいた場合は、子をnodeの親とつなげる。
            x.parent = y.parent
        
        if y.parent == None:#yがrootのときは、xをrootにする。
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        
        if y != node:
            node.key = y.key
        
    def get_successor(self, node):
        if node.right != None:
            return self.get_minimum(node.right)
        
        y = node.parent
        while y != None and node == y.right:
            node = y
            y = y.parent
        return y
    
    def get_minimum(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def pre_parse(self, node):
        if node == None:
            return
        self.list.append(node.key)
        self.pre_parse(node.left)
        self.pre_parse(node.right)
    
    def in_parse(self, node):
        if node == None:
            return
        self.in_parse(node.left)
        self.list.append(node.key)
        self.in_parse(node.right)

T = Tree()

N = int(input())
for i in range(N):
        order, *key = input().split() #printの場合はkeyがないので、*をつけて配列として扱う。
        if order == "print":
            T.list = []
            T.in_parse(T.root)
            print(" " + " ".join(map(str, T.list)))
            T.list = []
            T.pre_parse(T.root)
            print(" " + " ".join(map(str, T.list)))
        elif order == "insert":
            T.insert(Node(int(key[0]))) #なぜかわからないがintにしないとWAになる。
        elif order == "find":
            if T.find(int(key[0])):
                print("yes")
            else:
                print("no")
        else:
            node = T.find(int(key[0]))
            T.delete(node)
