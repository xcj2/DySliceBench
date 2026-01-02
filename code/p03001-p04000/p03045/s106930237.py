import sys
# input関係の定義
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
# template


# PyPyだと再帰が遅いので注意
# BEGIN CUT HERE
class UnionFind():
    '''
    UnionFind木

    Parameters
    --------
        n (int): UnionFind木のサイズ

    Methods
    --------
        unite(x: int, y: int) -> None
            ノード x とノード y を結合する
        same(x: int, y: int) -> bool
            ノード x とノード y が同じ集合に属するか判定する
        size(x: int) -> int
            ノード x を含む集合の要素数を返す

    '''

    def __init__(self, n):
        self._data = [-1] * n

    def unite(self, x: int, y: int) -> bool:
        '''x と y を結合'''
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False  # 元々結合されている場合はFalseを返し終了する
        elif self._data[x] > self._data[y]:
            x, y = y, x  # swap
        self._data[x] += self._data[y]
        self._data[y] = x
        return True

    def root(self, x: int) -> int:
        '''ノード x の親を返す'''
        while self._data[x] >= 0:
            x = self._data[x]
        return x

    def same(self, x: int, y: int) -> bool:
        '''x と y が同じグループに属するか判定'''
        return self.root(x) == self.root(y)

    def size(self, x: int) -> int:
        '''x を含むグループのノード数を返す'''
        return self._data[self.root(x)]

# END CUT HERE

# BEGIN CUT HERE
class QuickFind():
    def __init__(self, n):
        self.i2g = [i for i in range(n)]  # i2g[i] := アイテム i の所属するグループの番号
        self.g2i = [[i]for i in range(n)]  # g2i[g]: = グループ g に所属するアイテムたち

    def unite(self, ia, ib):
        '''アイテム ia の所属するグループとアイテム ib の所属するグループを 1 つにする'''
        # ia と ib が同じグループに属しているならば return
        if self.same(ia, ib):
            return
        # ia の所属するグループが ib の所属するグループより小さくならないようにする
        if len(self.g2i[self.i2g[ia]]) < len(self.g2i[self.i2g[ib]]):
            ia, ib = ib, ia
        ga, gb = self.i2g[ia], self.i2g[ib]
        # グループ gb に所属する全てのアイテムをグループ ga に移す
        for j in self.g2i[gb]:
            self.i2g[j] = ga
        self.g2i[ga].extend(self.g2i[gb])
        self.g2i[gb] = []


    def same(self, ia, ib):
        '''アイテム ia とアイテム ib は同じグループに所属しているか？'''
        return self.i2g[ia] == self.i2g[ib]

    def size(self, x: int) -> int:
        '''アイテム x の属する集合のサイズを返す'''
        return len(self.g2i[self.i2g[x]])

    def group(self, x: int) -> list:
        '''アイテム x の属する集合を返す'''
        return self.g2i[self.i2g[x]]

    def __str__(self):
        '''デバッグ用出力'''
        return str([self.g2i[i] for i in range(len(self.g2i))if len(self.g2i[i]) != 0])
# END CUT HERE

def benchmark():
    import random
    N = 10**6
    uf = UnionFind(N)
    a = [(random.randint(0, 1), random.randint(0, N - 1), random.randint(0, N - 1)) for i in range(N)]
    for t, x, y in a:
        if t == 0:
            uf.unite(x, y)
        else:
            uf.same(x, y)



def AOJ_DSL_1_A():
    """http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=jp"""
    n, q = mi()
    uf = UnionFind(n)
    for _ in range(q):
        t, x, y = mi()
        if t == 0:
            uf.unite(x, y)
        else:
            if uf.same(x, y):
                print(1)
            else:
                print(0)
# verified on 2019/07/02


def ABC120_D():
    """https://atcoder.jp/contests/abc120/submissions/6094323"""
    n, m = mi()
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = mi()

    uf = UnionFind(n)
    ans = [0] * (m + 1)
    ans[m] = n * (n - 1) // 2

    for i in range(m - 1, -1, -1):
        a[i] -= 1
        b[i] -= 1
        ans[i] = ans[i + 1]
        if uf.same(a[i], b[i]):
            continue

        x = uf.size(a[i])
        y = uf.size(b[i])
        ans[i] -= x * y

        uf.unite(a[i], b[i])

    for i in range(1, m + 1):
        print(ans[i])

# verified on 2019/06/23
# Python3:616ms


def ABC126_E():
    """https://atcoder.jp/contests/abc126/submissions/6094497"""
    N, M = mi()
    uf = UnionFind(N)
    for i in range(M):
        _X, _Y, _Z = mi()
        uf.unite(_X - 1, _Y - 1)
    ans = 0
    for i in range(N):
        if uf.root(i) == i:
            ans += 1
    print(ans)
# verified on 2019/06/23
# Python3:468ms


def ABC131_F():
    """https://atcoder.jp/contests/abc131/submissions/6094709"""
    from collections import defaultdict
    MAX = 100010
    uf = UnionFind(2 * MAX)
    N = ii()
    for i in range(N):
        x, y = mi()
        uf.unite(x, y + MAX)

    mx = defaultdict(int)
    for i in range(MAX):
        mx[uf.root(i)] += 1
    my = defaultdict(int)
    for i in range(MAX, 2 * MAX):
        my[uf.root(i)] += 1
    ans = 0
    for i in range(2 * MAX):
        ans += mx[i] * my[i]
    print(ans - N)
# verified on 2019/06/23
# Python:580ms

def ATC001B():
    N, Q = mi()
    ANS = ["No", "Yes"]
    uf = QuickFind(N)
    for _ in range(Q):
        P, A, B = mi()
        if P == 0:
            uf.unite(A, B)
        elif P == 1:
            print(uf.group(A))
            print(ANS[uf.same(A, B)])

if __name__ == '__main__':
    # AOJ_DSL_1_A()
    # ABC120_D()
    ABC126_E()
    # ABC131_F()
    # ATC001B()
    # import cProfile
    # cProfile.run('benchmark()', sort=0)
