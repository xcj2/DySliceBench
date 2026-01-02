def main():
    """
    1 <= N <= 10^5
    1 <= Ai,Bi <= 10^9
    """
    N = int(input())
    *A, = map(int, input().split())
    *B, = map(int, input().split())

    ans = f(N, A, B)
    print(ans)


def a(N, A, B):
    ans = 0
    return ans


def f(N, A, B):
    diff = [b - a for a, b in zip(A, B)]
    diff = sorted(diff)
    diff_sum = sum(diff)

    if diff_sum > 0:
        return -1

    if len([d for d in diff if d <= 0]) == N:
        return 0

    start = 0
    end = N - 1
    used = [False] * N
    while start < end:
        ds = diff[start]
        de = diff[end]
        if ds <= 0 and de <= 0:
            break

        if ds < 0 and de > 0:
            cost = min(abs(ds), de)
            diff[start] += cost
            diff[end] -= cost

            used[start] = True
            used[end] = True

        if diff[start] >= 0:
            start += 1
        if diff[end] <= 0:
            end -= 1

    ans = sum(used)
    return ans


if __name__ == "__main__":
    main()
