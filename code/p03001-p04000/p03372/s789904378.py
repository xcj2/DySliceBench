import sys
from heapq import heappush, heappop
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())

INF = 10**18


class HeapSet:
    def __init__(self):
        self.minQue = []
        self.maxQue = []
        self.counter = defaultdict(lambda: 0)

    def insert(self, x):
        heappush(self.minQue, x)
        heappush(self.maxQue, -x)
        self.counter[x] += 1

    def delete(self, x):
        self.counter[x] = max(0, self.counter[x] - 1)

    def get_max(self):
        while self.maxQue and self.counter[-self.maxQue[0]] == 0:
            heappop(self.maxQue)
        return -self.maxQue[0] if self.maxQue else None

    def get_min(self):
        while self.minQue and self.counter[self.minQue[0]] == 0:
            heappop(self.minQue)
        return self.minQue[0] if self.minQue else None

    def __str__(self):

        min = []
        sl = sorted(list(set(self.minQue)))
        for i in range(len(sl)):
            if self.counter[sl[i]]:
                min += [sl[i]] * self.counter[sl[i]]

        return min.__str__()


def main():

    N, C = in_nn()
    xv = []

    for i in range(N):
        x, v = in_nn()
        xv.append((x, v))

    if N == 1:
        ans = 0
        x, v = xv[0]
        ans = max(ans, v - min(x, C - x))
        print(ans)
        exit()

    xv.sort()

    tsum = [0] * (N + 1)
    for i in range(N):
        tsum[i + 1] = tsum[i] + xv[i][1]

    for i in range(N):
        tsum[i + 1] -= xv[i][0]

    rev_tsum = [0] * (N + 1)
    for i in range(N):
        rev_tsum[i + 1] = rev_tsum[i] + xv[N - 1 - i][1]

    for i in range(N):
        rev_tsum[i + 1] -= C - xv[N - 1 - i][0]

    heap = HeapSet()

    for i in range(N + 1):
        heap.insert(tsum[i])

    # print(tsum)
    # print(rev_tsum)
    # print(dmin)

    ans = heap.get_max()
    for i in range(1, N + 1):
        heap.delete(tsum[N + 1 - i])
        v1 = heap.get_max()
        v2 = rev_tsum[i]
        c2 = C - xv[N - i][0]
        value = v1 + v2 - c2
        ans = max(ans, value)

    heap2 = HeapSet()
    for i in range(N + 1):
        heap2.insert(rev_tsum[i])

    ans = max(ans, heap2.get_max())
    for i in range(1, N + 1):
        heap2.delete(rev_tsum[N + 1 - i])
        v1 = heap2.get_max()
        v2 = tsum[i]
        c2 = xv[i - 1][0]
        value = v1 + v2 - c2
        ans = max(ans, value)

    print(ans)


if __name__ == '__main__':
    main()
