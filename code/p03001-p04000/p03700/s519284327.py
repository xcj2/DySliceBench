def main():
    N, A, B = (int(i) for i in input().split())
    H = [int(input()) for i in range(N)]

    def is_ok(H, mid):
        H = [h - mid*B for h in H]
        need = 0
        for h in H:
            if h > 0:
                need += (h + (A - B) - 1)//(A - B)
        if need <= mid:
            return True
        else:
            return False

    def binary_search_meguru(H):
        ng = -1
        ok = 10**9 + 1
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2  # 爆破回数
            if is_ok(H, mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(binary_search_meguru(H))


if __name__ == '__main__':
    main()
