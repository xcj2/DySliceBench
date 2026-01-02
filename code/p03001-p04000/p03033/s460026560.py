def main():
    import sys
    input = lambda : sys.stdin.readline().rstrip()

    n, q = map(int, input().split())
    stx = []
    for _ in range(n):
        s, t, x = map(int, input().split())
        stx.append([x, s - x, t - x])
    stx.sort(reverse=True)
    d = [int(input()) for _ in range(q)]

    N = q
    N0 = 2**(N-1).bit_length()
    data = [None]*(2*N0)
    INF = (-1, 10**9 + 1)
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
    def _query(k):
        k += N0-1
        s = INF
        while k >= 0:
            if data[k]:
                s = max(s, data[k])
            k = (k - 1) // 2
        return s
    def query(k):
        return _query(k)[1]



    import bisect

    for i, (x, start, last) in enumerate(stx):
        l = bisect.bisect_left(d, start)
        r = bisect.bisect_left(d, last)
        update(l, r, (i, x))

    for i in range(q):
        res = query(i)
        if res == 10**9 + 1:
            print(-1)
        else:
            print(res)
if __name__ == '__main__':
    main()
    

