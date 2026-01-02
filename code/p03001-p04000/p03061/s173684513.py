# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class SegmentTree():
    '''
    非再帰
    segment tree
    '''

    def __init__(self, _n, func, inf=float('inf')):
        '''
        _n->配列の長さ
        func:func(a,b)->val,　func=minだとRMQになる
        木の高さhとすると,
        n:h-1までのノード数。h段目のノードにアクセスするために使う。
        data:ノード。
        parent:k->child k*2+1とk*2+2
        '''
        self.n = 2**(_n-1).bit_length()
        self.inf = inf
        self.data = [inf]*(2*self.n)
        self.func = func

    def set(self, k, v):
        '''
        あたいの初期化
        '''
        self.data[k+self.n-1] = v

    def build(self):
        '''
        setの後に一斉更新
        '''
        for k in reversed(range(self.n-1)):
            self.data[k] = self.func(self.data[k*2+1], self.data[k*2+2])

    def update(self, k, a):
        '''
        list[k]=aに更新する。
        更新ぶんをrootまで更新
        '''
        k += self.n-1
        self.data[k] = a

        while k > 0:
            k = (k-1)//2
            self.data[k] = self.func(self.data[k*2+1], self.data[k*2+2])

    def query(self, l, r):
        '''
        [l,r)のminを求める
        '''
        L = l+self.n
        R = r+self.n
        ret = self.inf
        while L < R:
            if R & 1:
                R -= 1
                ret = self.func(ret, self.data[R-1])
            if L & 1:
                ret = self.func(ret, self.data[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return ret


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = int(input())
L = list(map(int, input().split()))
T = SegmentTree(N, gcd, 0)
for i, l in enumerate(L):
    T.set(i, l)
T.build()

ans = 0
for i in range(N):
    l = i
    r = i+1
    ans = max(ans, gcd(T.query(0, l), T.query(r, N)))
print(ans)
