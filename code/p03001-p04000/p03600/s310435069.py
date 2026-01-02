def main():
    import sys

    def I():
        return int(sys.stdin.readline().rstrip())

    def LI():
        return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり

    N = I()
    A = [[0] * (N + 1)] + [[0] + LI() for _ in range(N)]

    ans = (sum(sum(A[i]) for i in range(N + 1))) // 2
    minus = 0

    # A[i][j]が実現可能か、必要かを判定していく
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            for k in range(1, N + 1):
                if k == i or k == j:
                    continue
                else:
                    if A[i][j] > A[i][k] + A[k][j]:  # A[i][j]が実現できない
                        print(-1)
                        exit()
                    elif A[i][j] == A[i][k] + A[k][j]:  # A[i][j]は無駄
                        minus += A[i][j]
                        break

    print(ans - minus)

if __name__ == '__main__':
    main()