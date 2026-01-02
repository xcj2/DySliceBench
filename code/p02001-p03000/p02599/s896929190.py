from typing import Union
import sys
from operator import itemgetter

Num = Union[int, float]


class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.bit = [0] * (self.size + 1)
    
    def add(self, k: int, x: Num) -> None:
        """
        (0-index で) k 番目の要素に x をたす。
        >>> b = FenwickTree(5)
        >>> b.add(0, 10)
        >>> b.bit
        [0, 10, 10, 0, 10, 0]
        """
        if not 0 <= k < self.size:
            raise IndexError(f"FenwickTree.add(): size is {self.size}. accessed [{k}]")
        k += 1    # 1-index
        while k <= self.size:
            self.bit[k] += x
            LSB = k & (-k)
            k += LSB
    
    def _accum_sum(self, k: int) -> Num:
        """ (1-index, 内部関数) bit の 1 ~ k 番目の要素の和を求める。"""
        s = 0
        while k > 0:
            s += self.bit[k]
            LSB = k & (-k)
            k -= LSB
        return s
    
    def sum(self, l: int, r: int) -> Num:
        """
        (0-index で) [l, r) 区間の和を求める。
        >>> b = FenwickTree(5)
        >>> b.add(1, 10)
        >>> b.add(2, 20)
        >>> b.sum(1, 3)
        30
        """
        if not 0 <= l <= r <= self.size:
            raise IndexError(f"FenwickTree.sum(): size is {self.size}. got slice is [{l}:{r}]")
        # 0-index の数列における [l]...[r-1] の閉区間を計算。1-index なら [l+1]...[r]。
        return self._accum_sum(r) - self._accum_sum(l)



def input(): return sys.stdin.readline().rstrip()

def mi(): return map(int, input().split())

def mi_0(): return map(lambda x: int(x)-1, input().split())


def solve(n, q, interval, query):
    """
    [s, t] なる点を含むリスト interval
    [l, r(, query-number)] (0-index) なるクエリを q 個含むリスト query。l <= s and t <= r なる点の個数は何個か？
    """
    query_to_ans = [-1] * q
    query.sort(key=itemgetter(0))
    interval.sort(key=itemgetter(0))
    ft = FenwickTree(5 * 10 ** 5 + 5)
    # main
    for l, r, query_num in reversed(query):
        # l 以上のものを全て処理対象に入れる
        while interval and l <= interval[-1][0]:
            _, t = interval.pop()
            ft.add(t, 1)
        query_to_ans[query_num] = (r - l + 1) - ft.sum(0, r+1)
    # output
    for ans in query_to_ans:
        print(ans)



def main():
    n, q = mi()
    L = tuple(mi())
    prev = dict()
    intervals = []
    for i in range(n):
        if L[i] not in prev:
            prev[L[i]] = i
        else:
            intervals.append((prev[L[i]], i))
            prev[L[i]] = i
    query = []
    for i in range(q):
        l, r = mi_0()
        query.append((l, r, i))
    solve(n, q, intervals, query)
    


if __name__ == '__main__':
    main()
