def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    A.sort()
    B.sort()
    C.sort()

    def is_ok1(mid, S, K):
        if K <= S[mid]:
            return True
        else:
            return False

    def is_ok2(mid, S, K):
        if K < S[mid]:
            return True
        else:
            return False

    def binary_search_meguru(S, K, is_ok):
        left = -1
        right = N
        while right - left > 1:
            mid = left + ((right - left) // 2)
            if is_ok(mid, S, K):
                right = mid
            else:
                left = mid
        return right

    ans = 0
    for b in B:
        a = binary_search_meguru(A, b, is_ok1)
        c = binary_search_meguru(C, b, is_ok2)
        ans += a * (N-c)
    print(ans)


if __name__ == '__main__':
    main()
