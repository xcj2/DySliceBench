import sys
input = sys.stdin.readline

class Node: # ノードの型
    def __init__(self, height, key, x):
        self.height = height # そのノードを根とする部分木の高さ
        self.key    = key    # そのノードのキー
        self.value  = x      # そのノードの値
        self.lst    = None   # 左部分木
        self.rst    = None   # 右部分木 

def height(t): return 0 if t is None else t.height

def bias(t): return height(t.lst) - height(t.rst)

def modHeight(t): t.height = 1 + max(height(t.lst), height(t.rst))

def rotateL(v):
    u = v.rst; t2 = u.lst
    u.lst = v; v.rst = t2
    modHeight(u.lst)
    modHeight(u)
    return u

def rotateR(u):
    v = u.lst; t2 = v.rst
    v.rst = u; u.lst = t2
    modHeight(v.rst)
    modHeight(v)
    return v

def rotateLR(t):
    t.lst = rotateL(t.lst)
    return rotateR(t)

def rotateRL(t):
    t.rst = rotateR(t.rst)
    return rotateL(t)

def keys_sub(t):
    if t is None: return []
    return keys_sub(t.lst) + [t.key] + keys_sub(t.rst)

def values_sub(t):
    if t is None: return []
    return values_sub(t.lst) + [t.value] + values_sub(t.rst)

def items_sub(t):
    if t is None: return []
    return items_sub(t.lst) + [(t.key, t.value)] + items_sub(t.rst)



class AVLMap:
    def __init__(self):
        self.root   = None  # AVL木の根。Node 型
        self.change = False # 修正が必要かを示すフラグ(True:必要, False:不要)
        self.lmax   = None  # 左部分木のキーの最大値
        self.value  = None  # lmax に対応する値
    
    def balanceLi(self, t): return self.balanceL(t)
    def balanceRi(self, t): return self.balanceR(t)

    def balanceLd(self, t): return self.balanceR(t)
    def balanceRd(self, t): return self.balanceL(t)

    def balanceL(self, t):
        if not self.change: return t
        h = height(t)
        if bias(t) == 2:
            if bias(t.lst) >= 0:
                t = rotateR(t)
            else:
                t = rotateLR(t)
        else: modHeight(t)
        self.change = (h != height(t))
        return t

    def balanceR(self, t):
        if not self.change: return t
        h = height(t)
        if bias(t) == -2:
            if bias(t.rst) <= 0:
                t = rotateL(t)
            else:
                t = rotateRL(t)
        else: modHeight(t)
        self.change = (h != height(t))
        return t

     # insert(挿入)    

    def insert(self, key, x): self.root = self.insert_sub(self.root, key, x)

    def insert_sub(self, t, key, x):
        if t is None:
            self.change = True
            return Node(1, key, x)
        elif key < t.key:
            t.lst = self.insert_sub(t.lst, key, x)
            return self.balanceLi(t)
        elif key > t.key:
            t.rst = self.insert_sub(t.rst, key, x)
            return self.balanceRi(t)
        else:
            self.change = False
            t.value = x
            return t

    #重複を許すか許さないかをkeyベースで考える
    def set_append(self, key, x):
        if self.member(key):
            pass
        else:
            self.insert(key, x)
    
    def list_append(self, key, x):
        self.insert(key, x)
        
    # delete(削除)

    def delete(self, key): self.root = self.delete_sub(self.root, key)

    def delete_sub(self, t, key):
        if t is None:
            self.change = False
            return None
        elif key < t.key:
            t.lst = self.delete_sub(t.lst, key)
            return self.balanceLd(t)
        elif key > t.key:
            t.rst = self.delete_sub(t.rst, key)
            return self.balanceRd(t)
        else:
            if t.lst is None:
                self.change = True
                return t.rst # 右部分木を昇格させる
            else:
                t.lst = self.delete_max(t.lst) # 左部分木の最大値を削除する
                t.key = self.lmax # 左部分木の削除した最大値で置き換える
                t.value = self.value
                return self.balanceLd(t)

    def delete_max(self, t):
        if t.rst is not None:
            t.rst = self.delete_max(t.rst)
            return self.balanceRd(t)
        else:
            self.change = True
            self.lmax = t.key # 部分木のキーの最大値を保存
            self.value = t.value
            return t.lst # 左部分木を昇格させる

    # member(検索)等
    def member(self, key):
        t = self.root
        while t is not None:
            if key < t.key:
                t = t.lst
            elif key > t.key:
                t = t.rst
            else:
                return True
        return False

    # キーから値を得る。キーがヒットしない場合は None を返す
    def lookup(self, key):
        t = self.root
        while t is not None:
            if key < t.key:
                t = t.lst
            elif key > t.key:
                t = t.rst
            else:
                return t.value
        return None       

    # x以上の最小のキー
    def upper_bound(self, x):
        t = self.root
        res = 0
        ans = None
        while t is not None:
            if x < t.key:
                ans = t.key
                t = t.lst
            elif x > t.key:
                t = t.rst
            else:
                return t.key
        return ans
    
    # x以下の最大のキー
    def lower_bound(self, x):
        t = self.root
        res = 0
        ans = None
        while t is not None:
            if x < t.key:
                t = t.lst
            elif x > t.key:
                ans = t.key
                t = t.rst
            else:
                return int(t.key)
        return ans
            

    def isEmpty(self): return self.root is None

    def clear(self): self.root = None

    def keys(self): return keys_sub(self.root)

    def values(self): return values_sub(self.root)

    def items(self): return items_sub(self.root)

    def size(self): return len(self.keys())




def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    index = [0]*n
    for i in range(n):
        index[a[i]-1] = i
    
    avl = AVLMap()
    
    ans = 0
    avl.insert(index[n-1], n-1)
    for i in range(n-2, -1, -1):
        ind = index[i]
        
        p, q, r, s = 0, 0, 0, 0
        key_upper = avl.upper_bound(ind)
        if key_upper != None:
            p = key_upper
            key_upper = avl.upper_bound(key_upper+1)
            if key_upper == None:
                q = n
            else:
                q = key_upper
        else:
            p = n
            q = n
        
        
        
        
        
        key_lower = avl.lower_bound(ind)
        if key_lower != None:
            r = key_lower
            key_lower = avl.lower_bound(key_lower-1)
            if key_lower == None:
                s = -1
            else:
                s = key_lower
        else:
            r = -1
            s = -1
        

        ans += (i+1)*((p-ind)*(r-s)+(ind-r)*(q-p))
        
        
        avl.insert(ind, i)
    
    print(ans)
    
    
    
    
if __name__ == "__main__":
    main()
