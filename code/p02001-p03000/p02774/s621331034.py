import sys
from bisect import bisect_left, bisect_right
from math import ceil
def input(): return sys.stdin.readline().strip()


def countPair(Ap, Am, plus, minus, zero, x):
    """
    「積がx未満になる組」の個数を返す。

    Aiをfixしたとき、Ai * Aj < xなるjの個数をカウントしていけば良い。
    二分探索では間に合わなかったので、尺取り法で実装する。
    """
    num = 0
    if x < 0:
        idx = 0 # Amの各値に対して、Ap上を走査する
        for a in Am:
            while idx < plus and a * Ap[idx] >= x:
                idx += 1
            if idx >= plus:
                break
            num += plus - idx
        return num

    elif x == 0:
        num = plus * minus
        return num

    else:
        num = plus * minus # 積が負になる組
        num += zero * (plus + minus) # 0 * a (ただしa!=0)なる組
        num += zero * (zero - 1) // 2 # 0 * 0なる組

        """
        以下のカウントでは(A[i]*A[j])と(A[j]*A[i])を区別してしまう。
        また(A[i]*A[i])も数えてしまうので、あえてまずはこのような重複をありにして、
        最後に２で割るなりして処理する。
        """
        prenum = 0
        dupl = 0
        # 正＊正の場合
        idx = plus - 1 # Apの各値に対して、Ap上を走査する
        for a in Ap:
            while idx >= 0 and a * Ap[idx] >= x:
                idx -= 1
            prenum += idx + 1

            if a * a < x:
                dupl += 1

        # 負＊負の場合
        idx = minus - 1 # Amの各値に対して、Am上を走査する
        for a in Am:
            while idx >= 0 and a * Am[idx] < x:
                idx -= 1
            prenum += minus - idx - 1

            if a * a < x:
                dupl += 1

        return num + (prenum - dupl) // 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Ap = []
    Am = []
    plus = 0
    minus = 0
    zero = 0
    for a in A:
        if a > 0:
            Ap.append(a)
            plus += 1
        elif a < 0:
            Am.append(a)
            minus += 1
        else:
            zero += 1
    Ap.sort()
    Am.sort()

    """
    (K個目の値) = (「積がx未満になる組がK個未満」であるようなxの最大値)
    として決め打ち二分探索を行う。
    """

    l = -10 ** 18 - 1
    r = 10 ** 18 + 1
    while r - l > 1:
        m = (l + r) // 2
        if countPair(Ap, Am, plus, minus, zero, m) < K:
            l = m
        else:
            r = m
    print(l)


if __name__ == "__main__":
    main()
