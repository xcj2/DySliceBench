import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



### 遅延評価セグメント木
class LazySegmentTree:
    def __init__(self, n, a=None):
        """初期化
        num : n以上の最小の2のべき乗
        """
        num = 1
        while num<=n:
            num *= 2
        self.num = num
        self.seg = [ninf] * (2*self.num-1)
        self.lazy = [f0] * (2*self.num-1)
        self.ls = [0]*(2*self.num-1)
        self.rs = [0]*(2*self.num-1)
        self.ls[0] = 0
        self.rs[0] = self.num
        for i in range(self.num-1):
            self.ls[2*i+1] = self.ls[i]
            self.rs[2*i+1] = (self.ls[i] + self.rs[i])//2
            self.ls[2*i+2] = (self.ls[i] + self.rs[i])//2
            self.rs[2*i+2] = self.rs[i]
        if a is not None:
            # O(n)で初期化
            assert len(a)==n
            for i in range(n):
                self.seg[num-1+i] = a[i]
            for k in range(num-2, -1, -1):
                self.seg[k] = op(self.seg[2*k+1], self.seg[2*k+2])
    def eval(self, k):
        if self.lazy[k]==f0:
            return 
        if k<self.num-1:
            self.lazy[k*2+1] = composition(self.lazy[k], self.lazy[k*2+1])
            self.lazy[k*2+2] = composition(self.lazy[k], self.lazy[k*2+2])
        self.seg[k] = mapping(self.lazy[k], self.seg[k])
        self.lazy[k] = f0
    def eval_all(self):
        for i in range(2*self.num-1):
            self.eval(i)
    def update(self,a,b,x=None,f=None):
        """A[a]...A[b-1]をxに更新する
        """
        if f is None:
            # 更新クエリ
            f = lambda y: x
        k = 0
        q = [k] # k>=0なら行きがけ順
        # 重なる区間を深さ優先探索
        while q:
            k = q.pop()
            l,r = self.ls[k], self.rs[k]
            if k>=0:
                self.eval(k)
                if r<=a or b<=l:
                    continue
                elif a<=l and r<=b:
                    self.lazy[k] = composition(f, self.lazy[k])
                    self.eval(k)
                else:
                    q.append(~k)
                    q.append(2*k+1)
                    q.append(2*k+2)
            else:
                k = ~k
                self.seg[k] = op(self.seg[2*k+1], self.seg[2*k+2])
    def query(self,a,b):
        k = 0
        l = 0
        r = self.num
        q = [k]
        ans = ninf
        # 重なる区間を深さ優先探索
        while q:
            k = q.pop()
            l,r = self.ls[k], self.rs[k]
            self.eval(k)
            if r<=a or b<=l:
                continue
            elif a<=l and r<=b:
                ans = op(ans, self.seg[k])
            else:
                q.append(2*k+2)
                q.append(2*k+1)
#             print(q, ans, l,r,a,b, self.seg[k])
        return ans

n,q = list(map(int, input().split()))
M = 998244353
vals = [1]
vals2 = [1]
v = 1
for i in range(n):
    v *= 10
    v %= M
    vals.append(v)
    vals2.append((1+vals2[-1]*10)%M)
    
ninf = 0 # (転倒数, #0, #1)
V = (1<<32)
def op(x,y):
#     print(x,bin(y))
    return ((x%V)*vals[y//V] + y%V)%M + (x//V + y//V)*V
# op = lambda x,y: ((x[0]*vals[y[1]] + y[0])%M, x[1]+y[1])
# op = lambda x,y: ((x[0]*vals[y[1]] + y[0])%M, x[1]+y[1])

mapping = lambda f,x: x if f is None else ((f%10)*vals2[(x//V)-1])%M + (x//V)*V
def composition(f1,f2):
    if f1 is None:
        return f2
    elif f2 is None:
        return f1
    else:
        if f1//10<f2//10:
            return f2
        else:
            return f1
# composition = lambda f1, f2: f1 if f2 is None else 
f0 = None
sg = LazySegmentTree(n, [1+(1<<32)]*n)
ans = [None]*q
for i in range(q):
    l,r,d = map(int, input().split())
    l -= 1
    r -= 1
#     print(l,r,d)
    sg.update(l,r+1,f=10*i+d)
    ans[i] = sg.query(0,n+1)%V
write("\n".join(map(str, ans)))