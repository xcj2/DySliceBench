def main():
    _, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    if K == 0:
        print(max(A))
        return

    def is_ok(x):
        need = 0
        for a in A:
            if a % x == 0:
                need += a//x - 1
            else:
                need += a//x
        if need <= K:
            return True
        else:
            return False

    def binary_search():
        ng = 0
        ok = 10**9
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(binary_search())


if __name__ == '__main__':
    main()
