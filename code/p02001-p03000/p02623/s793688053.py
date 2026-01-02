import sys
import bisect
import itertools
import collections
import fractions
import heapq
import math
from operator import mul
from functools import reduce
from functools import lru_cache


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    N, M, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))

    def is_ok(bcount):
        return Asum[acount] + Bsum[bcount] <= K


    def meguru_bisect(ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    nowtime = 0

    Asum = [0]
    Bsum = [0]
    tmp = 0
    for a in A:
        tmp += a
        Asum.append(tmp)
    tmp = 0
    for b in B:
        tmp += b
        Bsum.append(tmp)

    maxbooks = 0
    before = M
    ans = 0
    for acount in range(N+1):
        maxB = meguru_bisect(M+1, -1)
        if maxB < 0:
            continue
        ans = max(ans, acount+maxB)

    print(ans)



if __name__ == '__main__':
    solve()
