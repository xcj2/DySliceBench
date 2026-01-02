import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr

    N, P = map(int, input().split())
    arr = factorization(P)
    answer = 1
    for a in arr:
        if a[1] >= N:
            ans = a[0] ** (a[1] // N)
            answer *= ans
    print(answer)


if __name__ == "__main__":
    main()
