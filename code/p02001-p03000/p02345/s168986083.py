class Segment:
    def __init__(self, N, init_val):
        self.N0 = 2**(N-1).bit_length()
        # 0-indexedで管理
        self.dat = [identity_element]*(2*self.N0)
        # 値を代入
        for i in range(N):
            self.dat[i+self.N0-1]=init_val[i]    
        # 構築
        for i in range(self.N0-2,-1,-1) :
            self.dat[i]=segfunc(self.dat[2*i+1],self.dat[2*i+2]) 

    # k番目の要素の値をxに変更
    def update(self, k, x):
        k += self.N0-1
        self.dat[k] = x
        while k >= 0:
            k = (k-1)//2
            self.dat[k] = segfunc(self.dat[2*k+1], self.dat[2*k+2])

    # 区間[l, r)の最小値を求める
    def query(self, l, r):
        L = l + self.N0
        R = r + self.N0
        s = identity_element
        # 区間を列挙しながら最小値を求める
        while L < R:
            if R & 1:
                R -= 1
                s = segfunc(s, self.dat[R-1])
            if L & 1:
                s = segfunc(s, self.dat[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s
def segfunc(x,y):
    return min(x,y)
identity_element = 2**31-1

n,q = map(int,input().split())
seg = Segment(n,[identity_element]*n)

for i in range(q):
    c,x,y=map(int,input().split())
    if c:
        print(seg.query(x,y+1))
    else:
        seg.update(x,y)
