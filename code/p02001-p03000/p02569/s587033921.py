import sys

sys.setrecursionlimit(10**7)
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


class LazySegTree():  # モノイドに対して適用可能、Nが2冪でなくても良い
    def __init__(self,N,X_func,A_func,operate,X_unit,A_unit):
        self.N = N
        self.X_func = X_func
        self.A_func = A_func
        self.operate = operate
        self.X_unit = X_unit
        self.A_unit = A_unit
        self.X = [self.X_unit]*(2*self.N)
        self.A = [self.A_unit]*(2*self.N)
        self.size = [0]*(2*self.N)

    def build(self,init_value):  # 初期値を[N,2N)に格納
        for i in range(self.N):
            self.X[self.N+i] = init_value[i]
            self.size[self.N+i] = 1
        for i in range(self.N-1,0,-1):
            self.X[i] = self.X_func(self.X[i << 1],self.X[i << 1 | 1])
            self.size[i] = self.size[i << 1] + self.size[i << 1 | 1]

    def update(self,i,x):  # i番目(0-index)の値をxに変更
        i += self.N
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.X_func(self.X[i << 1],self.X[i << 1 | 1])
            i >>= 1

    def eval_at(self,i):  # i番目で作用を施した値を返す
        return self.operate(self.X[i],self.A[i],self.size[i])

    def eval_above(self,i):  # i番目より上の値を再計算する
        i >>= 1
        while i:
            self.X[i] = self.X_func(self.eval_at(i << 1),self.eval_at(i << 1 | 1))
            i >>= 1

    def propagate_at(self,i):  # i番目で作用を施し、1つ下に作用の情報を伝える
        self.X[i] = self.eval_at(i)
        self.A[i << 1] = self.A_func(self.A[i << 1],self.A[i])
        self.A[i << 1 | 1] = self.A_func(self.A[i << 1 | 1], self.A[i])
        self.A[i] = self.A_unit

    def propagate_above(self,i):  # i番目より上で作用を施す
        H = i.bit_length()
        for h in range(H,0,-1):
            self.propagate_at(i >> h)

    def fold(self,L,R):  # [L,R)の区間取得
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self.propagate_above(L0)
        self.propagate_above(R0)
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_func(vL,self.eval_at(L))
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_func(self.eval_at(R),vR)
            L >>= 1
            R >>= 1
        return self.X_func(vL,vR)

    def operate_range(self,L,R,x):  # [L,R)にxを作用
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self.propagate_above(L0)
        self.propagate_above(R0)
        while L < R:
            if L & 1:
                self.A[L] = self.A_func(self.A[L],x)
                L += 1
            if R & 1:
                R -= 1
                self.A[R] = self.A_func(self.A[R],x)
            L >>= 1
            R >>= 1
        self.eval_above(L0)
        self.eval_above(R0)


N,Q = MI()
A = LI()
B = []
for i in range(N):
    if A[i] == 0:
        B.append((0,1,0))
    else:
        B.append((0,0,1))
# (その区間の転倒数,0の個数,1の個数)


def X_func(x,y):
    x0,x1,x2 = x
    y0,y1,y2 = y
    return (x0+y0+x2*y1,x1+y1,x2+y2)


def A_func(a,b):
    return a ^ b


def operate(x,a,r):  # 右作用
    if a == 0:
        return x
    x0,x1,x2 = x
    return (x1*x2-x0,x2,x1)


X_unit = (0,0,0)
A_unit = 0


LST = LazySegTree(N,X_func,A_func,operate,X_unit,A_unit)
LST.build(B)

for i in range(Q):
    T,L,R = MI()
    if T == 1:
        LST.operate_range(L-1,R,1)
    else:
        print(LST.fold(L-1,R)[0])
