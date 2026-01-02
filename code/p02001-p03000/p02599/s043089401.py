
class BinaryIndexedTree:
    def __init__(self, n):
        # 0-indexed
        n += 1
        nv = 1
        while nv < n:
            nv *= 2
        self.size = nv
        self.tree = [0] * nv

    def sum(self, i):
        """ [0, i]を合計する """
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i - 1]
            i -= i & -i
        return s

    def add(self, i, x):
        """ 値の追加：添字i, 値x """
        i += 1
        while i <= self.size:
            self.tree[i - 1] += x
            i += i & -i

    def get(self, l, r=None):
        """ 区間和の取得 [l, r) """
        # 引数が1つなら一点の値を取得
        if r is None: r = l + 1
        res = 0
        if r: res += self.sum(r - 1)
        if l: res -= self.sum(l - 1)
        return res

    def update(self, i, x):
        """ 値の更新：添字i, 値x """
        self.add(i, x - self.get(i))

    def bisearch_fore(self, l, r, x):
        """ 区間[l, r]を左から右に向かってx番目の値がある位置 """
        l_sm = self.sum(l - 1)
        ok = r + 1
        ng = l - 1
        while ng + 1 < ok:
            mid = (ok + ng) // 2
            if self.sum(mid) - l_sm >= x:
                ok = mid
            else:
                ng = mid
        if ok != r + 1:
            return ok
        else:
            return 1<<60

def resolve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))


    pi = [-1] * (N + 1)  # 各数について最後に出てきた場所
    ps = [[] for i in range(N)]

    for i in range(N):
        l = pi[A[i]]
        if l != -1:
            ps[l].append(i)
        pi[A[i]] = i

    qs = [[] for i in range(N)]
    for i in range(Q):
        l, r = map(lambda x:int(x)-1, input().split())
        qs[l].append((r, i))

    BIT = BinaryIndexedTree(N + 1)
    ans = [0] * Q

    for x in range(N - 1, -1, -1):
        for y in ps[x]:
            BIT.add(y, 1)

        for r, i in qs[x]:
            ans[i] = (r - x + 1) - BIT.sum(r)

    print(*ans, sep="\n")



if __name__ == "__main__":
    resolve()
