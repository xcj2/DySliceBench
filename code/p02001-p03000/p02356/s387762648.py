from bisect import bisect_right

def main():
    N, Q = map(int, input().split())
    a = [-1 for i in range(N)]
    sum = [0 for i in range(N + 1)]
    for i, val in enumerate(input().split()):
        a[i] = int(val)
        sum[i + 1] = sum[i] + a[i]
    X = list(map(int, input().split()))

    # print("DEBUG: sum={}".format(sum))
    for x in X:
        ans = solve3(a, x, N, sum)
        print(ans)


def solve1(a, x, N, sum):
    l, r = 0, 0
    ret = 0
    while l < N:
        if r < N + 1:
            r = bisect_right(sum, sum[l] + x, r)
        if r > l:
            ret += (r - 1 - l)
        l += 1

    return ret

def solve2(a, x, N, sum):
    l, r, sum = 0, 0, 0
    ret = 0
    while l < N:
        while r < N and sum + a[r]  <= x:
            sum += a[r]
            r += 1
        ret += (r - l)
        sum -= a[l]
        l += 1

    return ret


def solve3(a, x, N, sum):
    l, sum, ans = 0, 0, 0
    for r in range(N):
        sum += a[r]
        while sum > x:
            sum -= a[l]
            l += 1
        ans += r - l + 1
    return ans


main()

