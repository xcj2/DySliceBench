import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def check(H):
    N = len(H)
    for i in range(N):
        if H[i] != 0:
            return False

    return True


def main():
    N = int(input())
    H = list(map(int, input().split()))

    ans = 0
    while True:
        if check(H):
            break

        # 区間分割
        i = 0
        while i < N:
            if H[i] == 0:
                i += 1
            else:
                # 区間が始まる
                ans += 1
                while i < N and H[i] > 0:
                    H[i] -= 1
                    i += 1

    print(ans)


if __name__ == "__main__":
    main()
