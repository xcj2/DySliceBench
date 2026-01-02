import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = MI()
W = [0] * N
for i in range(N):
    w = I()
    W[i] = w


def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    cnt = 0
    w_sum = 0
    for i in range(N):
        w_sum += W[i]
        if w_sum > arg:
            cnt += 1
            w_sum = W[i]
        elif w_sum == arg:
            cnt += 1
            w_sum = 0
        else:
            cnt += 0
    if w_sum != 0:
        cnt += 1
    return cnt <= K


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

a = max(W)
b = sum(W)
print(meguru_bisect(a - 1, b + 1))
