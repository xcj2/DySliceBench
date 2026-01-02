def lower_bound(l, r, val):
    while r - l > 1:
        mid = (r + l) // 2
        if sum[mid] <= val:
            l = mid
        else:
            r = mid
    return l


def get_sum(l, r):
    return sum[r] - (0 if l == 0 else sum[l - 1])


def search(l, r):
    mid = lower_bound(l, r + 1, get_sum(l, r) / 2 + (0 if l == 0 else sum[l - 1]))
    for i in range(mid - 2, mid + 3):
        if l <= i and i + 1 <= r:
            yield get_sum(l, i), get_sum(i + 1, r)


N = int(input())
A = list(map(int, input().split()))

tmp = 0
sum = [0 for i in range(N)]

for a, b in enumerate(A):
    tmp += b
    sum[a] = tmp

ans = tmp

for ind in range(1, N - 2):
    for l1, r1 in search(0, ind):
        for l2, r2 in search(ind + 1, N - 1):
            t = l1, r1, l2, r2
            ans = min(ans, max(t) - min(t))

print(ans)
