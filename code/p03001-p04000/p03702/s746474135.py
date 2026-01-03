def main():
    N, A, B = map(int, input().split())
    H = [0] * N
    for i in range(N):
        H[i] = int(input())
    
    def isOK(x):
        cnt = 0
        for i in range(N):
            now = H[i] - B * x
            if now > 0:
                cnt += now // (A - B) if now % (A - B) == 0 else (now // (A - B)) + 1
            if cnt > x:
                return False
        return True
        

    def binary_search():
        ng = -1
        ok = 1010101010

        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2

            if (isOK(mid)):
                ok = mid
            else:
                ng = mid
        return ok

    ans = binary_search()
    print(ans)

    

if __name__ == "__main__":
    main()