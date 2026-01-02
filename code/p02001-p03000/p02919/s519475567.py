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
    N = int(input())
    P = list(map(int, input().split()))
    idx = [0] * N
    bit = BinaryIndexedTree(N)
    for i in range(N):
        idx[P[i]-1] = i
    ans = 0
    for i in range(N)[::-1]:
        bit.add(idx[i], 1)
        x = bit.query(idx[i])
        l = bit.search(x-1)
        ll = bit.search(x-2)
        r = bit.search(x+1)
        rr = bit.search(x+2)
        tmp = (idx[i]-l) * (rr-r) + (r-idx[i]) * (l-ll)
        ans += (i+1) * tmp
    print(ans)


if __name__ == "__main__":
    main()
