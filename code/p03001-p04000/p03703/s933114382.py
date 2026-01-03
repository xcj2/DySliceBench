"""
方針
(1) 累積和s_i = a_0 + a_1 + ... + a_{i-1}をとる
(2) 部分和s_i_j = a_i + ... + a_{j-1} = s_j - s_iについて、平均がk以上であるとき、
        s_j - s_i >= k * (j-i) = k*j - k*i
    ->  s_j - k*j >= s_i - k*iとなる(i, j), i < jのペアを数えればよいので
    b_i = s_i - k*iを計算する
(3) b_iを座標圧縮して0~nの範囲に変換する (b_i -> c_iになるとする) (大小関係のみ重要なので)
(4) 0~nの変換においてBITを用いて、順次c_iの値をカウントしていく
"""

class BIT:
    def __init__(self, n):
        self.size = n + 1
        self.tree = [0] * (n + 2)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def submit():
    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]

    # 累積和を求める
    s = [0]
    for ai in a:
        s.append(s[-1] + ai)

    # biを求める
    b = [s[i] - k * i for i in range(n + 1)]

    # ciを求める
    b_dict = {}
    cnt = 0
    for be in sorted(b):
        if be not in b_dict:
            b_dict[be] = cnt
            cnt += 1
    c = [b_dict[be] for be in b]

    # BITでciの出現個数を逐次カウント
    bit = BIT(n)
    ans = 0
    for ce in c:
        ans += bit.sum(ce + 1)
        bit.add(ce + 1, 1)
    print(ans)

    
if __name__ == "__main__":
    submit()