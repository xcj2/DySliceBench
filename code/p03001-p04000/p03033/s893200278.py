def update(l, r, v):
    L = l + N0; R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] = v

        if L & 1:
            data[L-1] = v
            L += 1
        L >>= 1; R >>= 1
# a_iの現在の値を取得
def _query(k):
    k += N0-1
    s = INF
    while k >= 0:
        if data[k]:
            s = max(s, data[k])
        k = (k - 1) // 2
    return s
# これを呼び出す
def query(k):
    return _query(k)[1]

from bisect import bisect_left
from sys import stdin

if __name__ == '__main__':
    n, q = map(int, stdin.readline().rstrip().split())
    stx = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
    l = [int(stdin.readline().rstrip()) for _ in range(q)]

    INF = (-1, 2**31-1)
    N = len(l)
    N0 = 2**(N-1).bit_length()
    data = [None]*(2*N0)

    stx.sort(key=lambda x:x[2], reverse=True)
    for i, (s, t, x) in enumerate(stx):
        i1 = bisect_left(l, s - 0.5 - x)
        i2 = bisect_left(l, t - 0.5 - x)
        update(i1, i2, (i, x))

    for i in range(q):
        tmp = query(i)
        if tmp == INF[1]:
            print(-1)
        else:
            print(tmp)
