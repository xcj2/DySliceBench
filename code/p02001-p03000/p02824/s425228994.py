def main():
    N, M, V, P = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    A.sort(reverse=True)

    def is_ok(x):
        if x <= P-1:
            return True
        elif A[x-1] + M < A[P-1]:
            return False

        votes = M*(P-1 + N-x) + M
        for i in range(P-1, x-1):
            votes += A[x-1] + M - A[i]
        if M*V <= votes:
            return True
        else:
            return False

    def binary_search_meguru():
        ng = N+1
        ok = -1
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
