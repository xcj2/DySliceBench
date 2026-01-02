def main():
    from heapq import heappush, heappop, heappushpop
    import sys

    input = sys.stdin.readline

    class Median:
        def __init__(self):
            self.b = 0
            self.l = []
            self.sum_l = 0
            self.r = []
            self.sum_r = 0

        def update(self, a: int, b: int) -> None:
            self.b += b

            size = len(self.l) + len(self.r)
            if size % 2 == 0:
                x = heappushpop(self.r, a)
                self.sum_r += a - x
                heappush(self.l, -x)
                self.sum_l += x
            else:
                x = heappushpop(self.l, -a)
                self.sum_l += a + x  # a - (-x)
                heappush(self.r, -x)
                self.sum_r -= x  # += (-x)

        def query(self):
            median = -self.l[0]
            ret = (abs(len(self.l) * median - self.sum_l)
                   + abs(self.sum_r - len(self.r) * median)
                   + self.b)
            return median, ret

    med = Median()
    n = int(input())
    for _ in range(n):
        q = iter(input().rstrip().split())
        if next(q) == '1':
            med.update(*map(int, q))
        else:
            print(*med.query())


if __name__ == '__main__':
    main()
