def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    from itertools import accumulate
    S = [i for i in accumulate(range(1, min(N+1, 100000)))]

    def is_ok(mid):
        if N <= S[mid]:
            return True
        else:
            return False

    def binary_search_meguru():
        left = -1
        right = len(S)
        while right - left > 1:
            mid = left + ((right - left) // 2)
            if is_ok(mid):
                right = mid
            else:
                left = mid
        return right

    ans = binary_search_meguru() + 1
    print(ans)


if __name__ == '__main__':
    main()
