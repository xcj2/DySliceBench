# region header
import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
import copy
# @lru_cache(maxsize=None)
# sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
# endregion
# region input function


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])

# endregion


class BinaryIndexedTree:
    def __init__(self, n):
        self.N = n
        self.bit = [0] * (n + 1)  # 1-index

    def sum(self, idx):
        """return sum(a[0]~a[idx])

        Args:
            idx (int): 1-index

        Returns:
            int: sum(a[0]+...+a[i])
        """
        res = 0
        while idx:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res

    def add(self, idx, x):
        """a[idx]+=x

        Args:
            idx (int): 1-index
            x (int): add value
        """
        while idx <= self.N:
            self.bit[idx] += x
            idx += idx & (-idx)


n, q = inpl()
c = inpl()
query = [inpl() + [i] for i in range(q)]
query.sort(key=itemgetter(1))
rightest = [-1] * (n + 1)
now_q = 0
Bit = BinaryIndexedTree(n)
ans = [0] * q

for i in range(n):
    if rightest[c[i]] != -1:
        Bit.add(rightest[c[i]] + 1, -1)
    rightest[c[i]] = i
    Bit.add(i + 1, 1)

    while now_q < q and query[now_q][1] == i + 1:
        ans[query[now_q][2]] = Bit.sum(query[now_q][1]) - Bit.sum(query[now_q][0] - 1)
        now_q += 1
print("\n".join(map(str, ans)))
