class Acc2D:
    def __init__(self, a):
        h, w = len(a), len(a[0])
        self.acc2D = self._build(h, w, a)

    def _build(self, h, w, a):
        ret = [[0] * (w + 1) for _ in range(h + 1)]
        for r in range(h):
            for c in range(w):
                ret[r + 1][c + 1] = ret[r][c + 1] + ret[r + 1][c] - \
                    ret[r][c] + a[r][c]
        return ret

    def get(self, r1, r2, c1, c2):
        # [r1,r2), [c1,c2) : 0-indexed
        acc2D = self.acc2D
        return acc2D[r2][c2] - acc2D[r1][c2] - acc2D[r2][c1] + acc2D[r1][c1]


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())

    G = [[0] * 101 for _ in range(101)]
    # G[p2][p5]

    data = []
    for _ in range(N):

        *a, = input().rstrip().split('.')

        lena = 0
        p2, p5 = 0, 0
        if len(a) > 1:
            a[1] = a[1].rstrip('0')
            lena = len(a[1])
            a[0] = a[0] + a[1]
            p2 = p5 = -lena

        c = int(a[0])
        if c:
            while c % 2 == 0:
                c //= 2
                p2 += 1
            while c % 5 == 0:
                c //= 5
                p5 += 1

        p2 += 40
        p5 += 40
        G[p2][p5] += 1
        data.append((p2, p5))

    acc2d = Acc2D(a=G)

    ans = 0
    for p2, p5 in data:
        ans += acc2d.get(80 - p2, -1, 80 - p5, -1)
        if p2 >= 40 and p5 >= 40:
            ans -= 1
    ans //= 2
    print(ans)


if __name__ == '__main__':
    main()

# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
