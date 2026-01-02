import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    d = {}
    # n以下のaで始まり、bで終わる整数のそれぞれ求める
    # 計算量: O(log_n)
    for a in range(1, 10):
        for b in range(1, 10):
            cnt = 0
            # 1桁の整数が条件を満たすケース
            if a == b and a <= n:
                cnt += 1
            # 2桁以上の整数で条件を満たすケース
            i = 1
            while True:
                _min = a * (10**i) + b  # 整数が a0000b

                _max = a * (10**i) + b
                _i = i - 1
                while _i > 0:
                    _max += 9 * (10**_i)  # 整数が a999b
                    _i -= 1
                if _max <= n:
                    cnt += 10**(i - 1)
                    i += 1
                    continue
                elif _min > n:
                    break
                else:  # a0..0b <= n < a9..9b
                    cnt += ((n - _min) // 10) + 1
                    break
            d[10 * a + b] = cnt
    ans = 0
    for a in range(1, 10):
        for b in range(1, 10):
            ans += d[a * 10 + b] * d[b * 10 + a]
    print(ans)
    return


if __name__ == "__main__":
    main()
