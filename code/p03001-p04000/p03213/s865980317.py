import sys


def input():
    return sys.stdin.readline().strip()


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


def main():
    N = int(input())
    A = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        F = factorization(i)
        for f in F:
            A[f[0]] += f[1]
    cnt = [0 for _ in range(5)]
    for a in A:
        if a >= 74:
            cnt[0] += 1
        elif a >= 24:
            cnt[1] += 1
        elif a >= 14:
            cnt[2] += 1
        elif a >= 4:
            cnt[3] += 1
        elif a >= 2:
            cnt[4] += 1
    answer = cnt[0]
    answer += sum(cnt[:2]) * sum(cnt[2:])
    answer += sum(cnt[:2]) * (sum(cnt[:2]) - 1)
    answer += sum(cnt[:3]) * (sum(cnt[3:-1]))
    answer += sum(cnt[:3]) * (sum(cnt[:3]) - 1)
    answer += sum(cnt[:4]) * (sum(cnt[:4]) - 1) * cnt[-1] // 2
    answer += sum(cnt[:4]) * (sum(cnt[:4]) - 1) * (sum(cnt[:4]) - 2) // 2
    print(answer)


if __name__ == "__main__":
    main()
