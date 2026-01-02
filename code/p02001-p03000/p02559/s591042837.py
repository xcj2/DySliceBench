import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline






def main():
    def segfunc(x, y):
        return x + y

    def init(init_val):
        for i in range(n):
            seg[i + num - 1] = init_val[i]

        for i in range(num - 2, -1, -1):
            seg[i] = segfunc(seg[2 * i + 1], seg[2 * i + 2])

    def update(k, x):
        k += num - 1
        seg[k] = x
        while k:
            k = (k - 1) // 2
            seg[k] = segfunc(seg[k * 2 + 1], seg[k * 2 + 2])

    def query(p, q):
        if q <= p:
            return ide_ele
        p += num - 1
        q += num - 2
        res = ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = segfunc(res, seg[p])
            if q & 1 == 1:
                res = segfunc(res, seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = segfunc(res, seg[p])
        else:
            res = segfunc(segfunc(res, seg[p]), seg[q])
        return res

    N, Q = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    # seg tree初期値 (単位元)
    n = N
    ide_ele = 0
    num = 2 ** (n - 1).bit_length()
    seg = [ide_ele] * 2 * num

    init(A)

    for _ in range(Q):
        q, p, x = [int(x) for x in input().split()]
        if q == 0:
            A[p] += x
            update(p, A[p])
        else:
            print(query(p, x))





if __name__ == '__main__':
    main()

