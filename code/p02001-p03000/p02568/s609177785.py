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
a = list(map(int, input().split()))
# ninf = -10**9
# op = max
# mapping = lambda f,x: f(x)
# composition = lambda f1, f2: f1 if f1 is not None else f2
M = 998244353
ninf = 0
f0 = 1<<32
def op(x,y):
    x0,x1 = x>>32, x%(1<<32)
    y0,y1 = y>>32, y%(1<<32)
    return (((x0+y0)%M)<<32) + x1+y1
def mapping(f,x):
    x0,x1 = x>>32, x%(1<<32)
    f0,f1 = f>>32, f%(1<<32)
    return (((f0*x0 + f1*x1)%M)<<32) + x1
def composition(f,g):
    g0,g1 = g>>32, g%(1<<32)
    f0,f1 = f>>32, f%(1<<32)
    return (((f0*g0)%M)<<32) + (g1*f0 + f1)%M
# op = lambda x,y: ((x[0]+y[0])%M, (x[1]+y[1]))
# mapping = lambda f,x: ((f[0]*x[0] + f[1]*x[1])%M, x[1])
# composition = lambda f1, f2: ((f1[0]*f2[0])%M, (f2[1]*f1[0]+f1[1])%M)
# f0 = (1,0)
sg = LazySegmentTree(n, [((item<<32)+1) for item in a])
ans = []
for _ in range(q):
    t = tuple(map(int, input().split()))
    if t[0]==0:
        _, l,r,b,c = t
        sg.update(l,r,f=((b<<32)+c))
    else:
        _,s,t = t
        ans.append(sg.query(s,t)>>32)
        
write("\n".join(map(str, ans)))