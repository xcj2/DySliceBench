from bisect import bisect_left
import sys
input = sys.stdin.readline


class BinaryIndexedTree():
    def __init__(self, N):
        self.N = N
        self.arr = [0] * (N+1)

    def query(self, i):
        ret = 0
        i += 1
        while i:
            ret += self.arr[i]
            lsb = i & (-i)
            i -= lsb
        return ret

    def add(self, i, v):
        i += 1
        while i < self.N+1:
            lsb = i & (-i)
            self.arr[i] += v
            i += lsb

    def search(self, x):
        lo = -1
        hi = self.N
        while lo < hi:
            mid = (lo+hi)//2
            if self.query(mid) < x:
                lo = mid + 1
            else:
                hi = mid
        return lo


def main():
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i] - K
    sortedB = sorted(B)
    C = [0] * (N+1)
    bit = BinaryIndexedTree(N+1)
    ans = 0
    for i in range(N+1):
        x = bisect_left(sortedB, B[i])
        C[i] = x
        ans += bit.query(x)
        bit.add(C[i], 1)
    print(ans)


if __name__ == "__main__":
    main()
