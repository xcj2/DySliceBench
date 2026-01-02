def main():
    def check(p):
        # 積めた荷物の数
        i = 0
        # トラックの数だけ試行
        for _ in range(k):
            # 現在のトラックの重量
            s = 0
            while s + w[i] <= p:
                # 積める場合は積んで次の荷物へ
                # 積めない場合は次のトラックへ
                s += w[i]
                i += 1
                if i == n:
                    return n
        return i

    def solve():
        left, right = 0, 100000 * 10000 + 1
        while left < right:
            mid = (left + right) // 2
            if n <= check(mid):
                right = mid
            else:
                left = mid + 1
        return left

    n, k = [int(i) for i in input().split()]
    w = [int(input()) for _ in range(n)]
    ans = solve()
    print(ans)


if __name__ == '__main__':
    main()

