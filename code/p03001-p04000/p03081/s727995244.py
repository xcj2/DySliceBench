def main():
    def binary_search(ng, ok):
        def is_ok(mid):
            """落下するならTrue"""
            for char, drc in qs:
                if s[mid] == char:
                    mid += drc
                    if mid < 0 or mid >= n:
                        return True
            return False

        while abs(ng - ok) > 1:
            mid = (ng + ok) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    n, q = map(int, input().split())
    s = input()

    qs = []
    for _ in range(q):
        char, drc = input().split()
        drc = -1 if (drc == 'L') else 1
        qs.append((char, drc))
        # char:指定マス文字,英大文字
        # drc:方向,L=-1,R=1

    mid = n // 2
    left = binary_search(ng=mid + 1, ok=-1)  # okを返すので、最大mid
    right = binary_search(ng=mid, ok=n)  # okを返すので、最小mid+1
    # ok=落下する境目（落下側）
    # oolxxxroo -> r-1-l=6-1-2=3=xの個数
    # 012345678

    print(right - 1 - left)


if __name__ == '__main__':
    main()
