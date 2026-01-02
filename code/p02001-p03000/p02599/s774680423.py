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


def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    queries = [None] * Q
    for i in range(Q):
        l, r = map(int, input().split())
        queries[i] = [l, r, i]
    queries.sort(key=lambda x: x[1])

    bit = BinaryIndexedTree(N)
    numdupls = 0
    prevs = [-1] * N
    cur = 0
    ans = [-999] * Q
    for i in range(Q):
        l, r, qindex = queries[i]
        while cur < r:
            c = C[cur] - 1
            if prevs[c] != -1:
                bit.add(prevs[c], 1)
                numdupls += 1
            prevs[c] = cur
            cur += 1
        ans[qindex] = r-l+1 - (numdupls - bit.query(l-2))
#        print(ans, "l=", l, "r=", r, numdupls, bit.query(l-2))
    for i in range(Q):
        print(ans[i])


if __name__ == "__main__":
    main()
