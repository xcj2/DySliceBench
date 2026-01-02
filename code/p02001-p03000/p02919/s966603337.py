N = int(input())
P = [None] + [int(x) for x in input().split()]
id_list = [None] * (N+1)
for i,x in enumerate(P[1:],1):
    id_list[x] = i

# 左隣にあるインデックスを取得できるようにしておく
# Binary Iindex Treeを使うことで、区間[L,R]内での和をとれば[L,R]内のデータ件数を数えられる
class BIT:
    def __init__(self, n):
        # 要素数を与えてインスタンス化
        self.size = n
        self.tree = [0] * (n + 1) # index must be 1-origin

    def add(self, i, x=1):
        # add x(>= 1) to a_i
        while i <= self.size:
            self.tree[i] += x
            i += i&(-i) # i&(-i) = BITでのi番目の区間の長さ

    def sum(self, i):
        # sum of a_1, a_2, ... , a_i
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i) # i&(-i) = BITでのi番目の区間の長さ
        return s

    def search(self, x):
        # 二分探索。a_1 + a_2 + ... + a_i >= xなる最小のインデックスi(>= 1)を返す
        i = 0
        s = 0
        step = 1<<(N.bit_length()-1) # the largest 2^k (= step) <= N
        while step:
            if i+step <= N and s + self.tree[i+step] < x:
                i += step
                s += self.tree[i]
            step >>= 1
        return i+1


def main():
    bit = BIT(N)
    ans = 0
    for x in range(N,0,-1):
        idx = id_list[x]
        L = bit.sum(idx) # 左にある既に書き込んだ数の個数
        bit.add(idx)
        R = N-x-L # 右にある既に書き込んだ数の個数
        ll = bit.search(L-1) if L >= 2 else 0
        l = bit.search(L) if L >= 1 else 0
        r = bit.search(L+2) if R >= 1 else N+1
        rr = bit.search(L+3) if R >= 2 else N+1
        coef = 0
        if l != 0:
            # [b,c]を含むようにする。(a,b) と(c,d)が自由
            coef += (l - ll) * (r - idx)
        if r != 0:
            # [c,d]を含むようにする。
            coef += (rr - r) * (idx - l)
        ans += x * coef
    print(ans)

main()
