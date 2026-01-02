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


def c2i(c):
    return ord(c) - ord('a')


def main():
    N = int(input())
    S = list(input())
    bits = [BinaryIndexedTree(N) for _ in range(26)]
    for i, c in enumerate(S):
        bits[c2i(c)].add(i, 1)
    Q = int(input())
    for _ in range(Q):
        t, x, y = input().split()
        if t == "1":
            i = int(x) - 1
            bits[c2i(S[i])].add(i, -1)
            bits[c2i(y)].add(i, 1)
            S[i] = y
        else:
            l, r = int(x), int(y)
            ans = 0
            for i in range(26):
                cs = bits[i].query(r-1)
                if l-2 >= 0:
                    cs -= bits[i].query(l-2)
                if cs >= 1:
                    ans += 1
            print(ans)


if __name__ == "__main__":
    main()
