from math import gcd

class SegmentTree:
    """Segment Tree

    Attributes:
        n (int):       要素数以上の最小の2の累乗
        ide_ele (int): 単位元
            - RmQ (Range Minimum Query): inf
            - RMQ (Range Maximum Query): -1
            - RSQ (Range Sum Query):     0
            - RPQ (Range Product Query): 1
            - RGQ (Range GCD Query):     0
        seg (list):    要素の格納先
    """
    def __init__(self, a):
        """初期化 O(N)
        
        Args:
            a (list): 対象の配列
        """
        self.n = 2 ** (len(a) - 1).bit_length()
        self.ide_ele = 0
        self.seg = [self.ide_ele] * (2*self.n)

        for i, v in enumerate(a, self.n):
            self.seg[i] = v
        for i in range(self.n-1, 0, -1):
            self.seg[i] = self.st_func(self.seg[2*i], self.seg[2*i+1])

    def query(self, l, r):
        """区間クエリの計算 O(logN)

        Args:
            l (int): 区間の左端
            r (int): 区間の右端
        
        Returns:
            int: [l, r)についての区間クエリ
        """
        l += self.n
        r += self.n
        res_l = self.ide_ele
        res_r = self.ide_ele

        while l < r:
            if l % 2 == 1:
                res_l = self.st_func(res_l, self.seg[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res_r = self.st_func(self.seg[r], res_r)
            l //= 2
            r //= 2

        return self.st_func(res_l, res_r)

    def update(self, i, v):
        """値の更新 O(logN)

        Args:
            i (int): 更新対象のindex
            v (int): 更新値
        """
        i += self.n
        self.seg[i] = v
        while i > 1:
            i //= 2
            self.seg[i] = self.st_func(self.seg[i*2], self.seg[i*2+1])
    
    def st_func(self, x, y):
        """問題に応じた処理

        Returns:
            int: 問題に応じた値
                - RmQ(Range Minimum Query): min(x, y)
                - RMQ(Range Maximum Query): max(x, y)
                - RSQ(Range Sum Query):     x + y
                - RPQ(Range Product Query): x * y
                - RGQ(Range GCD Query):     gcd(x, y)
        """
        return gcd(x, y)
 
n = int(input())
a = list(map(int, input().split()))

st = SegmentTree(a)

res = 0
for i in range(n):
	res = max(res, gcd(st.query(0, i), st.query(i+1, n)))

print(res)