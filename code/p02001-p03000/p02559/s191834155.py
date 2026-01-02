import math


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
        pos = 0
        cur = 0
        idx = 2 ** int(math.log(self.N, 2))
        while idx >= 1:
            if pos + idx <= self.N and cur + self.arr[pos+idx] < x:
                cur += self.arr[pos+idx]
                pos += idx
            idx //= 2
        return pos


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    bit = BinaryIndexedTree(N)
    for i, a in enumerate(A):
        bit.add(i, a)
    for _ in range(Q):
        qtype, a, b = map(int, input().split())
        if qtype == 0:
            bit.add(a, b)
        else:
            ans = bit.query(b-1) - bit.query(a-1)
            print(ans)


if __name__ == "__main__":
    main()
