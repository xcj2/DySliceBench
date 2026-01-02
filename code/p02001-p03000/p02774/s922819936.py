from bisect import bisect_left, bisect_right
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

n_m = bisect_left(a, 0)  # a[i] < 0 の数
n_0 = bisect_right(a, 0) - n_m  # a[i] = 0 の数
n_p = n - n_m - n_0  # a[i] > 0 の数

nn_m = n_m * n_p  # 積が負になるペア数
nn_0 = n_0 * (n - n_0) + n_0 * (n_0 - 1) // 2  # 積が0になるペア数
nn_p = n * (n - 1) // 2 - nn_m - nn_0  # 積が正になるペア数

if k <= nn_m:
    # k番目の値は負

    def check_minus(x):
        # k番目の値がx(<0)以下

        # a[i] * a[j] <= x

        # a[i]   * a[j] <= x  : a[j] >= abs(x) / abs(a[i])
        # a[i+1] * a[j] <= x  : a[j] >= abs(x) / abs(a[i+1])
        #     a[i]  <=     a[i+1] < 0
        # abs(a[i]) >= abs(a[i+1])
        # a: [-------00000+++++++]
        #     i             jjjjj
        #      i             jjjj
        #       i              jj

        # a[i] * a[j] <= -7
        # n_m = 4
        # n_0 = 3
        # a = [-5, -3, -2, -1, 0, 0, 0, 1, 2, 3, 4, 5]
        #       i                          j (j  j  j)
        #           i                         j (j  j)
        #               i                        j
        #                   i                          j
        # a[i] * a[j] = -5
        #  -2  *   4  = -6

        cnt = 0
        j = n_m + n_0
        for i in range(n_m):
            while j < n and a[i] * a[j] > x:
                j += 1
            # a[i] * a[j] <= x
            # [j, n)
            cnt += n - j

        return cnt >= k

    # a[i] * a[j] <= x
    lb = -10**18  # False
    ub = -1  # True
    while ub - lb > 1:
        mid = (ub + lb) // 2
        if check_minus(mid):
            ub = mid
        else:
            lb = mid
    ans = ub
elif k <= nn_m + nn_0:
    # k番目の値は0
    ans = 0
else:
    # k番目の値は正
    a_p = a[n_m + n_0:]
    a_m = [-a[i] for i in reversed(range(n_m))]

    def check_plus(x):
        # k番目の値がx(>=0)以下
        def func(b):
            # b [++++++++++++++]
            #    ijjjjjjjjjjj
            #     ijjjjjjjj
            #      ijjjj
            #       ij

            # b[i] * b[j] <= x
            # b[i]   * b[j] <= x : b[j]  <= x / b[i]
            # b[i+1] * b[j] <= x : b[j]  <= x / b[i+1]

            c = 0
            j = len(b) - 1
            for i in range(len(b)):
                if i >= j:
                    break
                # i < j
                while i < j and b[i] * b[j] > x:
                    j -= 1
                # b[i] * b[j] <= x
                # (i, j]
                c += j - i
            return c

        cnt = nn_m + nn_0
        cnt += func(a_p)
        cnt += func(a_m)
        return cnt >= k

    # a[i] * a[j] <= x
    lb = 0  # False
    ub = 10**18 + 1  # True
    while ub - lb > 1:
        mid = (ub + lb) // 2
        if check_plus(mid):
            ub = mid
        else:
            lb = mid
    ans = ub
print(ans)
