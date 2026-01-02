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


# BEGIN CUT HERE
class BIT:
    '''
    BinaryIndexedTreeのクラス。0-indexed に統一してあるので0からn-1までの配列と思って使える。

    Parameters
    ----------
        n (Union(int, list)): int なら使う BIT のサイズ。list ならそのlistで BIT を初期化する
    '''

    def __init__(self, x, d=0):
        if isinstance(x, int):
            self.size = x
            self.tree = [d for _ in range(self.size + 1)]
        elif isinstance(x, list):
            self.size = len(x)
            self.tree = [d for _ in range(self.size + 1)]
            self.build(x)
        else:
            raise TypeError

    def build(self, arr):
        """
        初期化されたあとのBITをリストの値に設定する

        Parameters
        ----------
            arr (list): 元のlsit

        Raises
        ------
            TypeError: 入力はlistでないといけないことに注意してください。
        """
        if not isinstance(arr, list):
            raise TypeError
        for num, x in enumerate(arr):
            self.add(num, x)

    def sum(self, i):
        '''[0,i] の和'''
        s = self.tree[0]
        while i > 0:
            s += self.tree[i]
            i -= (i & -i)
        return s

    def add(self, i, a):
        i += 1
        '''i番目の要素にaを足す'''
        if(i == 0):
            return
        while (i <= self.size):
            self.tree[i] += a
            i += (i & -i)

    def lower_bound(self, w):
        '''[0,i]の和 >= w をみたす最小の index
        Examples
        ----------
        >>> bit = BIT([1,0,0,1,0,1,0])
        >>> bit.lower_bound(1)
        0
        >>> bit.lower_bound(2)
        3
        >>> bit.lower_bound(3)
        5
        '''
        if w <= 0:
            return -1
        x = 0
        k = 1 << (self.size.bit_length() - 1)
        while k:
            if x + k <= self.size and self.tree[x + k] < w:
                w -= self.tree[x + k]
                x += k
            k //= 2
        return x

    def getKthNum(self, w):
        '''k番目(k = 0, 1, ...)に小さい数を返す'''
        w += 1
        return self.lower_bound(w)


    def upper_bound(self, w):
        w += 0.00000000001
        return self.lower_bound(w)

    def query(self, l, r):
        '''[l, r)の和を求める'''
        return self.sum(r) - self.sum(l)

    # 出力関係（デバッグのみに用いる）
    def __getitem__(self, item):
        if not isinstance(item, int):
            _tmp = item.indices(self.size + 1)
            return [self.sum(i + 1) - self.sum(i) for i in range(_tmp[0], _tmp[1], _tmp[2])]
        else:
            return self.sum(item + 1) - self.sum(item)
    def __str__(self):
        return str(self[0:self.size])

# END CUT HERE

# BEGIN CUT HERE
def compress(v):
    sort_v = list(set(v))
    sort_v.sort()
    return sort_v
def dictionary(v):
    res = dict()
    for i in range(len(v)):
        res[v[i]] = i
    return res
# END CUT HERE


def AOJ_ALDS_1_5_D():
    """https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_D"""
    n = ii()
    a = lmi()
    bit = BIT(n)
    ans = 0
    mp = dictionary(compress(a))
    for j in range(n):
        ans += j - bit.sum0(mp[a[j]])
        bit.add0(a[j], 1)
    print(ans)
# verified on 2019/06/13


def AOJ_DSL2B():
    """https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B"""
    n, q = mi()
    bit = BIT(n, 0)
    for _ in range(q):
        c, x, y = mi()
        if c == 0:
            bit.add(x, y)
        elif c == 1:
            print(bit.query(x, y + 1))
# verified on 2019/06/13


def ARC033_C():
    q = ii()
    bit = BIT(200000, 0)
    for _ in range(q):
        t, x = mi()
        if t == 1:
            bit.add(x, 1)
        elif t == 2:
            k = bit.lower_bound(x)
            bit.add(k, -1)
            print(k)
# verified on 2019/06/13
# https://atcoder.jp/contests/arc033/tasks/arc033_3
# pypy3:558ms https://atcoder.jp/contests/arc033/submissions/5896367
# Python3:1966ms https://atcoder.jp/contests/arc033/submissions/5896359

def ABC140_E():
    '''https://atcoder.jp/contests/abc140/tasks/abc140_e'''
    N = ii()
    P = lmi()
    L = [0 for i in range(N)]
    for i in range(N):
        L[P[i] - 1] = i
    L.reverse()
    ans = 0
    bit = BIT(N)
    for num, i in enumerate(L):
        bit.add(i, 1)
        # print(bit)
        x = bit.sum(i)
        l2 = bit.getKthNum(x - 2)
        l1 = bit.getKthNum(x - 1)
        r1 = bit.getKthNum(x + 1)
        r2 = bit.getKthNum(x + 2)
        debug(x, l2, l1, r1, r2)
        ans += (abs(r2 - r1) * abs(i - l1) + abs(l1 - l2) * abs(r1 - i)) * (N - num)
    print(ans)


if __name__ == '__main__':
    if not __debug__:
        import doctest
        doctest.testmod()
    # AOJ_ALDS_1_5_D()
    # AOJ_DSL2B()
    # ARC033_C()
    ABC140_E()
