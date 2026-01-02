#!python3

from itertools import accumulate

def my_bisect(a, x, key, lo=0, hi=None, side="left"):
    if hi is None:
        hi = len(a)

    lov = key(a[lo])
    hiv = key(a[hi])

    if side == "left":
        while lo < hi:
            mid = (lo + hi) // 2
            miv = key(a[mid])

            if miv < val: lo, lov = mid+1, miv
            else: hi, hiv = mid, miv
    else:
        while lo < hi:
            mid = (lo + hi) // 2
            miv = key(a[mid])

            if val < miv: hi, hiv = mid, miv
            else: lo, lov = mid+1, miv

    return lo

from bisect import bisect_right

def resolve():
    N, M = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))

    a.sort(reverse=True)
    b = list(accumulate(a))
    c = [-i for i in a]

    def count_shake(z):
        n = 0
        for i, x in enumerate(a):
            y = x - z
            #j = my_bisect(a, y, lambda x: -x, lo=i, side="right")
            j = bisect_right(c, y, i)
            if i == j:
                break
            n += 2 * (j - i) - 1
        return n



    lo = a[-1] * 2
    hi = a[0] * 2

    while True:
        mid = (lo + hi) // 2
        x = count_shake(mid)

        if hi - lo <= 1:
            break
        if x < M: hi = mid
        else: lo = mid

    s = 0
    d = [-1] * N
    m = x
    for i, x in enumerate(a):
        y = x - mid
        j = bisect_right(c, x - mid)
        if j == 0: break
        d[i] = j-1
        s += b[j-1] + x * j

    print(s - mid * (m-M))




if __name__ == "__main__":
    resolve()
