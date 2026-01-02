from sys import stdin

class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res
def bc(x):
    return bin(x).count("1")

n = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()
q = int(stdin.readline().rstrip())

lamb_or = lambda x,y : x|y
seg = SegmentTree(n,lamb_or,0)

for i,x in enumerate(s):
    seg.update(i,1 << ord(x)-97)

for _ in range(q):
    c,x,y = [x for x in stdin.readline().rstrip().split()]
    if c == '1':
        x = int(x)
        seg.update(x-1,1 << ord(y)-97)
    elif c == '2':
        x = int(x)
        y = int(y)
        print(bc(seg.query(x-1,y)))
