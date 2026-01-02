import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    N, X = map(int, input().split())
    B = 1
    P = 1
    for i in range(N):
        B = 2 * B + 3
        P = 2 * P + 1

    def cnt(X, B, P, ans):
        if B == 5:
            if X == 5:
                return ans + 3
            elif X == 4:
                return ans + 3
            elif X == 3:
                return ans + 2
            elif X == 2:
                return ans + 1
            else:
                return ans
        if X == B:
            return ans + P
        elif X > B // 2 + 1:
            ans += P // 2 + 1
            P = P // 2
            X = X - (B // 2 + 1)
            B = B // 2 - 1
            return cnt(X, B, P, ans)
        elif X == B // 2 + 1:
            ans += P // 2 + 1
            return ans
        else:
            B = B // 2 - 1
            P = P // 2
            X -= 1
            return cnt(X, B, P, ans)

    answer = cnt(X, B, P, 0)
    print(answer)


if __name__ == "__main__":
    main()
