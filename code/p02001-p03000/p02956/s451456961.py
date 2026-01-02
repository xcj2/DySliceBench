N = int(input())

XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
    
# BITの定義
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    # index 1からiの値の和を返す
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    # index iの値にxを加算する
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

#######################
# 開始
from operator import itemgetter
def solve():
    p_list = XY[:]

    # y座標の圧縮
    p_list = sorted(p_list, key=itemgetter(1))
    p_list = [ (x, y, i+1) for i, (x, y) in enumerate(p_list)]

    # xでソート
    p_list= sorted(p_list)

    # ある点が四角に含まれる場合の総数を求めるメソッド
    power = [1] * N
    for i in range(1, N):
        power[i] = power[i-1] * 2 % 998244353

    # a,bを求める
    bit = Bit(N)
    ans = 0
    for i, (x, y, r) in enumerate(p_list):
        tmp = bit.sum(r)
        a = tmp
        b = i-tmp
        c = r-tmp-1
        d = (N-r+1)-(i-tmp)-1
        bit.add(r, 1)
        _a = power[a] - 1
        _b = power[b] - 1
        _c = power[c] - 1
        _d = power[d] - 1

        ret = (_a+1) * (_d+1) * _c * _b
        ret += (_b+1) * (_c+1) * _a * _d
        ret -= _a*_b*_c*_d
        ret += power[N-1]
        ans += ret % 998244353

    print(ans % 998244353)
    
solve()
