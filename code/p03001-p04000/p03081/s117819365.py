import sys
from collections import Counter
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, q = LI()
s = SI()
query = [LS() for _ in range(q)]


# posにいるゴーレムが，場外に出るか出ないかを判定
def check(pos, c):

    for t, d in query:
        # そのマスが呪文の影響を受ける対象マスではない場合
        if s[pos] != t:
            continue
        if d == 'L':
            if pos == 0:
                # 消滅する
                return c == 'L'
            # 呪文によって左にずれる
            pos -= 1
        else:
            if pos == n - 1:
                return c == 'R'
            pos += 1
    # 消滅しない
    return False


lo = -1
hi = n
while hi - lo > 1:
    mid = (lo + hi) // 2
    # 消滅するのであれば，さらに右よりにあるゴーレムで消滅する物を探す
    # 始めs[mid]にいるゴーレムが消滅するのであれば，
    # それより左にいるゴーレムは，左端で消滅する
    if check(mid, 'L'):
        lo = mid
    else:
        hi = mid
# 最も＞側にいる，左側に向かって進んで消滅するゴーレムのインデックス
l = lo


lo = -1
hi = n
while hi - lo > 1:
    mid = (lo + hi) // 2
    if check(mid, 'R'):
        hi = mid
    else:
        lo = mid
r = hi 

print(n - (l + 1 + n - r))
