from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    n = int(input())
    k = int(input())

    @lru_cache(None)
    def F(n, k):

        if n < 10:
            if 1 < k:
                return 0
            elif k == 1:
                return n
            elif k == 0:
                return 1

        m, r = divmod(n, 10)
        ret = 0
        # rに応じて場合分け
        if k >= 1:
            ret += F(m, k-1)*r  # r<=k
            ret += F(m-1, k-1)*(9-r)  # r>k
        ret += F(m, k)*1  # r==0
        return ret
    print(F(n, k))


resolve()