def main():
    import sys
    from heapq import heappush, heappop
    input = sys.stdin.buffer.readline

    # min
    def STfunc(a, b):
        if a < b:
            return a
        else:
            return b

    # クエリは0-indexedで[l, r)
    class SparseTable():
        def __init__(self, A):
            # A: 処理したい数列
            self.N = len(A)
            self.K = self.N.bit_length() - 1
            self.table = [[0] * (self.K + 1) for _ in range(self.N)]
            for i, a in enumerate(A):
                self.table[i][0] = A[i]
            for k in range(1, self.K + 1):
                for i in range(self.N):
                    j = i + (1 << (k - 1))
                    if j <= self.N - 1:
                        self.table[i][k] = STfunc(self.table[i][k - 1], self.table[j][k - 1])
                    else:
                        self.table[i][k] = self.table[i][k - 1]

        def query(self, l, r):
            # [l, r)の最小値を求める
            k = (r - l).bit_length() - 1
            return STfunc(self.table[l][k], self.table[r - (1 << k)][k])

    N = int(input())
    n = N//2
    A = list(map(int, input().split()))

    A_even = A[0:N:2]
    A_odd = A[1:N:2]
    ST_even = SparseTable(A_even)
    ST_odd = SparseTable(A_odd)
    val2idx = [0] * (N+1)
    for i in range(N):
        val2idx[A[i]] = i

    ans = []
    ans_append = ans.append
    pq = [(ST_even.query(0, n), 0, N)]
    for t in range(n):
        v1, left, right = heappop(pq)
        ans_append(v1)
        i = val2idx[v1]
        if i & 1:
            v2 = ST_even.query((i+1)//2, right//2 + 1)
            ans_append(v2)
            j = val2idx[v2]
            if left != i:
                heappush(pq, (ST_odd.query(left//2, i//2), left, i))
            if j-i > 1:
                heappush(pq, (ST_even.query((i+1)//2, j//2), i+1, j))
            if j+1 != right:
                heappush(pq, (ST_odd.query((j+1)//2, right//2), j+1, right))
        else:
            v2 = ST_odd.query(i//2, right//2)
            ans_append(v2)
            j = val2idx[v2]
            if left != i:
                heappush(pq, (ST_even.query(left//2, i//2), left, i))
            if j-i > 1:
                heappush(pq, (ST_odd.query((i+1)//2, j//2), i+1, j))
            if j+1 != right:
                heappush(pq, (ST_even.query((j+1)//2, right//2), j+1, right))

    print(*ans)


if __name__ == '__main__':
    main()
