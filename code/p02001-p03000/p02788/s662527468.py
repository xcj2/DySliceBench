def main():
    N, D, A = (int(i) for i in input().split())
    P = [[int(i) for i in input().split()] for j in range(N)]
    P.sort()
    X = [x[0] for x in P]
    H = [h[1] for h in P]
    diff = [H[0]] + [H[i+1] - H[i] for i in range(N-1)]
    BIT = [0] * (N+1)

    def BIT_query(idx):
        """ A1 ~ Aiまでの和(1-index) """
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx & -idx
        return res_sum

    def BIT_update(idx, x):
        """ Aiにxを加算(1-index) """
        while idx <= N:
            BIT[idx] += x
            idx += idx & -idx
        return

    def BIT_init(A):
        for i, e in enumerate(A):
            BIT_update(i+1, e)

    BIT_init(diff)
    from bisect import bisect_right
    ans = 0
    for left in range(N):
        x = P[left][0]
        h = BIT_query(left+1)
        if h > 0:
            cur = (h + A - 1) // A
            damage = cur * A
            BIT_update(left+1, -damage)
            right = bisect_right(X, x + 2*D)
            BIT_update(right+1, damage)
            ans += cur
    print(ans)


if __name__ == '__main__':
    main()
