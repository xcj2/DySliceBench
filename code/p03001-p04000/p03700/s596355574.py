def main():
    from math import ceil
    N, A, B = (int(i) for i in input().split())
    h = [int(input()) for i in range(N)]

    def is_ok(h,bomb,N,A,B):
        K = bomb
        cur = 0
        for i in range(N):
            cur += ceil((max(h[i] - B * K,0))/(A - B))
        return (cur <= K)

    def binary_search_meguru(Arr,N,A,B):
        left = -1
        right = 10**9 + 1
        while right - left > 1:
            mid = left + ((right - left) // 2)
            if is_ok(Arr,mid,N,A,B): right = mid
            else: left = mid
        return right
    
    print(binary_search_meguru(h,N,A,B))

if __name__ == '__main__':
    main()