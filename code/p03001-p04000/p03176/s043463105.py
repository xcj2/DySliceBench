def main():
    import sys
    input = sys.stdin.readline
    #区間の管理は　[a, b)で管理していることに注意

    # INT_MIN = -10 ** 18
    # MAX_N = 4 * 10 ** 5
    # MAX_N = 20


    # def init(n_):
    #     #簡単にするために2のべき乗に揃える
    #     n = 1
    #     while n <= n_:
    #         n *= 2
    #     return n

    #初期化
    N = int(input())
    # n = 1
    # while n <= N:
    #     n *= 2

    n = 262144
    data = [0] * (2 * n - 1)

    def update(k, a):
        k = k + n - 1
        # data[k] = a
        while k >= 0:
            data[k] = max(a, data[k])
            k = (k - 1) // 2
            # data[k] = max(data[2 * k + 1], data[2 * k + 2])

    def query(a, b, k, l, r):
        if r <= a or b <= l:
            return 0
        elif a <= l and r <= b:
            return data[k]
        else:
            return max(query(a, b, 2 * k + 1, l, (l + r)//2), query(a, b, 2 * k + 2, (l + r)//2, r))

    H = tuple(map(int, input().split()))
    A = tuple(map(int, input().split()))

    # ans = 0

    dp = [A[0]] + [0] * (N - 1)
    update(H[0] - 1, A[0])
    for i in range(1, N):
        # h = int(input())
        # a = int(input())
        dp[i] = query(0, H[i] - 1, 0, 0, n) + A[i]
        # h = H[i]
        # a = A[i]
        # tmp = query(1, h + 1) #[1, h)での最大値
        # print (h, tmp)
        update(H[i] - 1, dp[i])
        # ans = max(ans, tmp + a)
        # print (data)

    print (query(0, N, 0, 0, n))

if __name__ == '__main__':
    main()