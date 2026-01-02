class segment_tree:
    def __init__(self, N, operator_M, e_M):
        self.op_M = operator_M
        self.e_M = e_M
        
        self.N0 = 1<<(N-1).bit_length()
        self.dat = [self.e_M]*(2*self.N0)
    
    # 長さNの配列 initial で初期化
    def build(self, initial):
        self.dat[self.N0:self.N0+len(initial)] = initial[:]
        for k in range(self.N0-1,0,-1):
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])

    # a_k の値を x に更新
    def update(self,k,x):
        k += self.N0
        self.dat[k] = x
        k //= 2
        while k:
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])
            k //= 2

    # 区間[L,R]をopでまとめる
    def query(self,L,R):
        L += self.N0; R += self.N0 + 1 
        sl = sr = self.e_M
        while L < R:
            if R & 1:
                R -= 1
                sr = self.op_M(self.dat[R],sr)
            if L & 1:
                sl = self.op_M(sl,self.dat[L])
                L += 1
            L >>= 1; R >>= 1
        return self.op_M(sl,sr)

    def get(self, k): #k番目の値を取得。query[k,k]と同じ
        return self.dat[k+self.N0]

class BIT: #0-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [i&-i for i in range((n+1))]
        self.depth = n.bit_length()
        self.n0 = 1<<self.depth
#        self.element = [0]*(n+1)
    def get_sum(self, i): #a_0 + ... + a_{i} #閉区間
        s = 0; i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def query(self,l,r): #a_l + ... + a_r 閉区間
        return self.get_sum(r) - self.get_sum(l-1) 
    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
        # self.element[i] += x
    #def get(self,i): return element[i]        
    def bisect_left(self,w):
        #和が w 以上になる最小の index
        #w が存在しない場合 self.size を返す
        if w <= 0: return 0
        x,k = 0,self.n0
        for _ in range(self.depth):
            k >>= 1
            if x+k <= self.size and self.tree[x+k] < w:
                w -= self.tree[x+k]
                x += k
        return x
    
class stdmap:
    def __init__(self, n):
        self.size = n+1
        self.keys = set()
        self.B = BIT(n+1) #存在すれば 1、しないなら 0
        self.dic = [0]*(n+1) # 値域
    
    def __contains__(self, k):
        return k in self.keys

    def insert(self,a,b): # 値 a に b を上書き
        if a not in self.keys:
            self.B.add(a,1)
            self.keys.add(a)
        self.dic[a] = b

    def remove(self,a): # a を取り除く
        self.keys.remove(a)
        self.B.add(a,-1)

    def lower_bound(self,k): # k 以上の最小のkeyを求める
        return self.B.bisect_left(self.B.get_sum(k))
        
    def kth_key(self,k): # k 番目に小さい元のkeyを求める
        return self.B.bisect_left(k)

    def kth_value(self,k): # k 番目に小さい元のmap先を求める
        return self.dic[self.B.bisect_left(k)]

    def prev_key(self,k): #一個前の元のkeyを求める
        idx = self.B.get_sum(k)
        assert idx != 0
        return self.B.bisect_left(idx-1)

    def next_key(self,k):
        idx = self.B.get_sum(k)
        assert idx != self.size
        return self.B.bisect_left(idx+1)

    def __getitem__(self,item):
        return self.dic[item]


# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

h,w = map(int,readline().split())

b = stdmap(w+2)
b.dic = [0]*(w+3) # 値域
b.keys = set(range(w+2))

INF = 1<<31
seg = segment_tree(w+2, min, INF)
seg.build([INF]+[0]*w+[INF])


for i in range(1,h+1):
    p,q = map(int,readline().split())

    idx = b.B.get_sum(p-1)+1
    x = b.kth_key(idx)
    val = INF
    while x <= q:
        #print(x,b.dic[x]-x,"x,val")
        val = min(val,b.dic[x]-x)
        seg.update(x,INF)
        b.remove(x)
        x = b.kth_key(idx)
    
    if q < w:
        if q+1 not in b.keys or b.dic[q+1] > val+q+1:
            b.insert(q+1,val+q+1)
            seg.update(q+1,val+q+1)
    
    #print(b.keys)
    #print(seg.dat)
    #print(q,val,"q,val")    

    v = seg.dat[1]
    #print(v,i)
    if v>=INF:
        print(-1)
    else:
        print(v+i)
    
    #print()


