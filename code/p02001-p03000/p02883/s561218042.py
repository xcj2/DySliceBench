def main():
    N, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    F = [int(i) for i in input().split()]
    A.sort()
    F.sort(reverse=True)

    def is_ok(mid):
        # midは目標成績
        need = 0
        for i in range(N):
            if mid < A[i]*F[i]:
                b = (F[i]*A[i] - mid)
                need += (b + F[i] - 1)//F[i]
        if need <= K:
            return True
        else:
            return False

    def binary_search_meguru():
        ng = -1
        ok = 10**18 + 1
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(binary_search_meguru())


if __name__ == '__main__':
    main()
