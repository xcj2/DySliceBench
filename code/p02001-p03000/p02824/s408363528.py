def main():
    N, M, V, P = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    A.sort(reverse=True)

    def is_ok(x):
        # x問目が選ばれるか判定
        if x <= P-1:
            return True
        elif A[x-1] + M < A[P-1]:
            return False
        voted = (P-1)*M + (N-x)*M + M
        for i in range(P, x):
            voted += min(max((A[x-1] + M - A[i-1]), 0), M)
        if M*V <= voted:
            return True
        else:
            return False

    def binary_search_meguru():
        ng = N+1
        ok = P
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
