def main():
    import sys
    def MI():
        return map(int, sys.stdin.readline().rstrip().split())
    def LI():
        return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり

    N,Q = MI()
    c = [0] + LI()
    lr = []
    for i in range(Q):
        l,r = MI()
        lr.append(i+l*(10**6)+r*(10**12))

    lr.sort()  # 右端rでソート
    d = {}  # d[i] = 玉iが現れた最も右の位置
    ANS = [0]*Q


    class BIT():
        def __init__(self, init_value):
            self.n = len(init_value)
            self.tree = [0] * (self.n + 1)
            for i in range(1, self.n + 1):
                x = init_value[i - 1]
                while i <= self.n:
                    self.tree[i] += x
                    i += i & (-i)

        def update(self, i, x):  # i(1-index)番目の値を+x
            while i <= self.n:
                self.tree[i] += x
                i += i & (-i)
            return

        def query(self, i):  # 1番目からi(1-index)番目までの和を返す
            res = 0
            while i > 0:
                res += self.tree[i]
                i -= i & (-i)
            return res


    bit = BIT([0]*N)  # 最も右に現れた玉の位置を管理
    a = 0  # lr のどこまで見たか
    for i in range(1,N+1):
        if not c[i] in d.keys():
            d[c[i]] = i
            bit.update(i,1)
        else:
            bit.update(d[c[i]],-1)
            d[c[i]] = i
            bit.update(i, 1)
        while a <= Q-1:
            x = lr[a]
            r = x//(10**12)
            x %= 10**12
            l = x//(10**6)
            j = x % (10**6)
            if r == i:
                ANS[j] = bit.query(r)-bit.query(l-1)
                a += 1
            else:
                break

    print(*ANS,sep='\n')


if __name__ == '__main__':
    main()
