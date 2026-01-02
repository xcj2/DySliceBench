def main():
    N, M, V, P = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    A.sort(reverse=True)

    def is_ok(mid):
        if mid <= P-1:
            return False  # 採用可能
        if A[mid] + M < A[P-1]:
            return True  # 採用不可能
        votable = M + (P-1) * M + (N - (mid + 1))*M
        for i in range(P-1, mid):
            votable += min(M, max(0, A[mid] + M - A[i]))
        if M*V <= votable:
            return False
        else:
            return True

    def binary_search_meguru():
        left = -1
        right = N
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
