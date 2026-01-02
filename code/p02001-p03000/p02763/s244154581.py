class SegmentTree():
    def segfunc(self, x, y):
        return x|y #関数
    
    def __init__(self, a): #a:リスト
        n = len(a)
        self.ide_ele = 0 #単位元
        self.num = 2**((n-1).bit_length()) #num:n以上の最小の2のべき乗
        self.seg = [self.ide_ele]*2*self.num
        
        #set_val
        for i in range(n):
            self.seg[i+self.num-1] = a[i]
        #built
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.segfunc(self.seg[2*i+1], self.seg[2*i+2])
        
        
    def update(self, k, s):
        x = 1<<(ord(s)-97)
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1], self.seg[k*2+2])
            
    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res = self.ide_ele
        while q - p > 1:
            if p&1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f
    

N = int(input())
S = list(input())
for i in range(N):
    S[i] = 1<<(ord(S[i])-97)
Seg = SegmentTree(S)
Q = int(input())
for i in range(Q):
    x, y, z = input().split()
    if int(x) == 1:
        Seg.update(int(y)-1, z)
    else:
        print(popcount(Seg.query(int(y)-1, int(z))))