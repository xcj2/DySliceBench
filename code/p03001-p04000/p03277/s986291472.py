from operator import itemgetter
import sys
input = sys.stdin.readline


class BIT():
    """一点加算、区間取得クエリをそれぞれO(logN)で答える
    add: i番目にvalを加える
    get_sum: 区間[l, r)の和を求める
    i, l, rは0-indexed
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, val):
        """i番目にvalを加える"""
        i = i + 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def get_sum(self, l, r):
        """区間[l, r)の和を求める"""
        return self._sum(r) - self._sum(l)



n =int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a)


def solve(val):
    val = a_sorted[val]
    ruiseki = [0] * (n + 1)
    for i, num in enumerate(a):
        if num >= val:
            ruiseki[i + 1] = ruiseki[i] + 1
        else:
            ruiseki[i + 1] = ruiseki[i] - 1
    b = sorted(enumerate(ruiseki), key = itemgetter(1))
    for i in range(n + 1):
        bit.bit[i] = 0
    res = 0
    for i, _ in b:
        bit.add(i, 1)
        res += bit.get_sum(0, i)
        if res >= cnt:
            return True
    return False


cnt = 0
for i in range(n):
    cnt += n - i
cnt = (cnt + 1) // 2

bit = BIT(n + 1)
ok = 0
ng = n
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(a_sorted[ok])