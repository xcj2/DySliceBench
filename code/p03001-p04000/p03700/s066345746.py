def main():
    N, A, B = (int(i) for i in input().split())
    H = [int(input()) for i in range(N)]

    def is_ok(x):
        y = 0  # 中心爆破必要回数
        for i, h in enumerate(H):
            if h - x*B <= 0:
                continue
            le = 0
            ri = 10**9 + 1
            while ri - le > 1:
                mid = le + ((ri - le) // 2)
                if h - B*(max(x - mid, 0)) - A*mid <= 0:
                    ri = mid
                else:
                    le = mid
            y += ri
        if y <= x:  # 魔物を消し去るのが可能
            return True
        else:
            return False

    def binary_search_meguru():
        left = -1
        right = 10**9 + 1
        while right - left > 1:
            mid = left + ((right - left) // 2)
            if is_ok(mid):
                right = mid
            else:
                left = mid
        return right

    print(binary_search_meguru())


if __name__ == '__main__':
    main()
