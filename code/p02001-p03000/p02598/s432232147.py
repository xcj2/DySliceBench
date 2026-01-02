
import math

def cut(l, e):
    """全ての木片が長さl以下になるように切った時、
    eを処理するのに何回かかるか
    """
    return math.ceil(e / l) - 1


def judge(a, k, l):
    cuts = 0
    for e in a:
        cuts += cut(l, e)
    return cuts <= k


def submit():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    l = 0
    r = max(a)
    while abs(r - l) > 0.000001:
        m = (l + r) / 2
        if judge(a, k, m):
            r = m
        else:
            l = m

    print(math.ceil(m))


submit()
