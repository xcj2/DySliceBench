import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
import bisect
def main():
    N, K = MI()
    A = LI()
    A.sort()
    def is_ok(arg):
        # 条件を満たすかどうか？問題ごとに定義、argを求めたい値にして条件をreturnで返す
        cnt = 0
        for a in A:
            if a == 0:
                if arg >= 0:
                    cnt += N - 1
                else:
                    cnt += 0
            elif a < 0:
                aa = -((-arg) // a)
                cnt += N - bisect.bisect_left(A, aa)
                if aa <= a:
                    cnt -= 1
            else:
                aa = arg // a
                cnt += bisect.bisect_right(A, aa)
                if aa >= a:
                    cnt -= 1
        cnt //= 2
        return cnt >= K

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
    cnt_neg = bisect.bisect_left(A, 0)
    cnt_pos = N - bisect.bisect_right(A, 0)
    cnt_zer = N - cnt_pos - cnt_neg

    if K <= cnt_neg * cnt_pos:
        ng = - 10 ** 18 - 10
        ok = 1
        ans = meguru_bisect(ng, ok)
        print(ans)
    elif K <= cnt_neg * cnt_pos + cnt_zer * (N - 1) - cnt_zer * (cnt_zer - 1) // 2:
        print(0)
    else:
        ng = -1
        ok = 10 ** 18 + 10
        ans = meguru_bisect(ng, ok)
        print(ans)

if __name__ == "__main__":
    main()
