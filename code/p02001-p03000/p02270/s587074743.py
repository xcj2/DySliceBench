def main():
    N, K = (int(i) for i in input().split())
    w = [int(input()) for i in range(N)]
    S = 0
    for i in range(N):
        S += w[i]

    def is_ok(P):
        w_i = 0
        for i in range(K):
            cur = 0
            while w_i < N :
                if cur + w[w_i] <= P:
                    cur += w[w_i]
                    w_i += 1
                else:
                    break
        if w_i == N:
            return True
        else:
            return False

    def binary_search_meguru():
        left = -1
        right = S + 1
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
