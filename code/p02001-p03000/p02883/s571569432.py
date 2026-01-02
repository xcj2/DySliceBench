def main():
    N, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    F = [int(i) for i in input().split()]
    A.sort()
    F.sort(reverse=True)
    ma = 0
    for a, f in zip(A, F):
        ma = max(ma, a*f)

    def is_ok(mid):
        need = 0
        for a, f in zip(A, F):
            if mid < a*f:
                need += (a - mid//f)
        if need <= K:
            return True
        else:
            return False

    def binary_search_meguru():
        left = -1
        right = ma + 1
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
