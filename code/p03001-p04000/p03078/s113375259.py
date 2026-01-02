import heapq


#root.search(x): ◯.data == x のものが存在するある場合それを出力、ない場合Noneを出力
#root.insert(x): ◯.data == xが存在する場合Falseを出力、ない場合◯.data == x なる頂点を作る
#y.to_s(): 頂点yのdataを出力
#y.left_s(): 頂点yのleftを出力(ない場合はNone)

################################################################################
class Avltree:
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None 
        self.balance = "Even"
    def search(self,key):
        if self.key == None:
            return None
        if self.key > key:
            if self.left == None:
                return None
            else:
                return self.left.search(key)
        if self.key < key:
            if self.right == None:
                return None
            else:
                return self.right.search(key)
        return self # self.key == keyの場合
    def DoubleRightRotation(self):
        tl = self.left
        self.left = tl.right.right
        tl.right.right = self # selfはそのノード
        tlr = tl.right
        tl.right = tlr.left
        tlr.left = tl
        if tlr.balance == "Left":
            tlr.right.balance = "Right"
            tlr.left.balance = "Even"
        elif tlr.balance == "Right":
            tlr.right.balance = "Even"
            tlr.left.balance = "Left"
        elif tlr.balance == "Even":
            tlr.right.balance = "Even"
            tlr.left.balance = "Even"
        tlr.balance = "Even"
        return tlr
    def DoubleLeftRotation(self):
        tr = self.right
        self.right = tr.left.left
        tr.left.left = self
        trl = tr.left
        tr.left = trl.right
        trl.right = tr
        if trl.balance == "Right":
            trl.left.balance = "Left"
            trl.right.balance = "Even"
        elif trl.balance == "Left":
            trl.left.balance = "Even"
            trl.right.balance = "Right"
        elif trl.balance == "Even":
            trl.left.balance = "Even"
            trl.right.balance = "Even"
        trl.balance = "Even"
        return trl
    def SingleLeftRotation(self):
        tr = self.right
        tr.balance = "Even"
        self.balance = "Even"
        self.right = tr.left
        tr.left = self
        return tr
    def SingleRightRotation(self):
        tl = self.left
        tl.balance = "Even"
        self.balance = "Even"
        self.left = tl.right
        tl.right = self
        return tl
    def replace(self,p,v): # 親ノードpの下にある自分(self)をvに置き換える。
        if p.left == self:
            p.left = v
        else :
            p.right = v 
    def insert(self,key): # rootでのみ呼ばれる挿入
        if self.key == None: # rootを含むrotationはしないことにする。
            self.key = key
            return self
        if key < self.key:
            if self.left == None:
                self.left = Avltree(key)
            else:
                self.left.insertx(self,key)
        elif key > self.key:
            if self.right == None:
                self.right = Avltree(key)
            else:
                self.right.insertx(self,key)
        else: # key == self.key:
            pass # do not overwrite
    def insertx(self,p,key): # replaceを呼ぶために一つ上の親を持っているinsert
        if self.key > key:
            if self.left == None:
                self.left = Avltree(key)
            else:
                if not self.left.insertx(self, key): # 左の木が生長しなければ、
                    return False # 成長しない
            if self.balance == "Right":
                self.balance = "Even"
                return False
            elif self.balance == "Even":
                self.balance = "Left"
                return True # 成長した
            elif self.balance == "Left":
                if self.left.balance == "Right":
                    self.replace(p,self.DoubleRightRotation())
                elif self.left.balance == "Left":
                    self.replace(p,self.SingleRightRotation())
                return False # rotationを行うと成長しない
        if self.key < key:
            if self.right == None:
                self.right = Avltree(key)
            else:
                if not self.right.insertx(self, key):
                    return False 
            if self.balance == "Left":
                self.balance = "Even"
                return False
            elif self.balance == "Even":
                self.balance = "Right"
                return True
            elif self.balance == "Right":
                if self.right.balance == "Left": 
                    self.replace(p,self.DoubleLeftRotation())
                elif self.right.balance == "Right":
                    self.replace(p,self.SingleLeftRotation())
                return False
        return False # self.key == keyの時は何もしないので成長もしない 

    def to_s(self):
        return self.key
    def left_s(self):
        if self.left == None:
            return None
        return (self.left).key
    def right_s(self):
        if self.right == None:
            return None
        return (self.right).key


def Search(x,y,z):
    global dict
    global root
    global q
    p = a[x] + b[y] + c[z]
    u = ((1001)**2) * x + ((1001)**1) * y + z
    s = root.search(u)
    if s == None:
        root.insert(u)
        heapq.heappush(q, -p)
        if p not in dict:
            dict[p] = [(x, y, z)]
        else:
            dict[p].append((x, y, z))


x,y,z,k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
c = [int(_) for _ in input().split()]
a = sorted(a)
b = sorted(b)
c = sorted(c)

t = k
root = Avltree()
q = []
heapq.heapify(q)
dict = {}
count = 0
while t != 0:
    if t == k:
        p = a[x-1]+b[y-1]+c[z-1]
        print(p)
        x -= 1
        y -= 1
        z -= 1
        u = ((1001)**2) * x + ((1001)**1) * y + z
        root.insert(u)
        
        if x != 0:
            Search(x-1,y,z)
        if y != 0:
            Search(x,y-1,z)
        if z != 0:
            Search(x,y,z-1)

        if x == 0 and y == 0 and z == 0:
            break
        
        t -= 1
    else:
        p = heapq.heappop(q)*(-1)
        print(p)
        x, y, z = dict[p].pop()

        if x != 0:
            Search(x-1,y,z)
        if y != 0:
            Search(x,y-1,z)
        if z != 0:
            Search(x,y,z-1)

        if x == 0 and y == 0 and z == 0:
            break

        t -= 1

