import sys
from collections import deque
from bisect import bisect_right
from math import ceil
def input(): return sys.stdin.readline().strip()

N, D, A = map(int, input().split())
monsters = [(-1, -1)]
for _ in range(N):
    x, h = map(int, input().split())
    monsters.append((x, h))
monsters.sort()
#print("monsters = {}".format(monsters))
"""
どうせ左端のモンスターはいつか倒さないといけない（かつ爆弾投下順は不問）ので、
左端のモンスターから順に、なるべく爆弾を右に寄せて落としていけば良い。

別解としてBITでも殴ってみた
"""
class BIT:
    """
    https://tjkendev.github.io/procon-library/python/range_query/bit.html
    Binary index treeの実装
    配列[a1, a2,...,an]に対して以下のクエリをO(logn)で行う:
        1. aiにxを加える
        2. 区間和 ai + a(i+1) + ... + aj の和を求める
    """
    def __init__(self, n):
        """
        添字は1スタート
        """
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def add(self, i, x):
        """
        i>0に対してaiにxを加算(x < 0でもOK)
        """
        if i <= 0 or self.n < i:
            print("i should be within 1 to n")
        else:
            self.el[i] += x
            while i <= self.n:
                self.data[i] += x
                i += i & -i

    def sum(self, i):
        """
        添字1からiまでの累積和を求める
        """
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def get(self, i, j=None):
        """
        添字iからjまでの累積和を求める
        j=Noneの場合はaiの値を返す
        """
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i - 1)

"""
BITで区間に対する加算をする場合はimos法を利用することに注意する
"""

Damage = BIT(N)
ans = 0
for i in range(1, N + 1):
    x, h = monsters[i]
    d = Damage.sum(i) # モンスターiに入っているダメージ
    if d < h:
        times = ceil((h - d) / A)
        ans += times
        new_damage = times * A
        #print("ans+={} for monster {}".format(times, i))

        idx = bisect_right(monsters, (monsters[i][0] + 2 * D, 10**10))
        Damage.add(i, new_damage)
        if idx != N + 1:
            Damage.add(idx, -new_damage)

print(ans)
