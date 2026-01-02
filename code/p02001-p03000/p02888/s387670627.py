def main():
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()
    L_pair = []
    for i in range(N):
        for j in range(i+1, N):
            L_pair.append((i, j))

    def is_ok(mid, i, j):
        if L[mid] < L[i] + L[j]:
            return True
        else:
            return False

    def binary_search_meguru(i, j):
        left = j
        right = N
        while right - left > 1:
            mid = left + ((right - left) // 2)
            if is_ok(mid, i, j):
                left = mid
            else:
                right = mid
        return right

    ans = 0
    for i, j in L_pair:
        r = binary_search_meguru(i, j)
        ans += r - (j + 1)
    print(ans)


if __name__ == '__main__':
    main()
