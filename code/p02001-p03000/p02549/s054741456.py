def getsum(bit, i):

    s = 0
    i = i + 1

    while i > 0:

        s += bit[i]

        i -= i & (-i)
    return s

def interval_sum(bit, a, b):
    if a == 0:
        return getsum(bit, b)
    else:
        return getsum(bit, b) - getsum(bit, a - 1)

def updatebit(bit , n , i ,v):

    i += 1

    while i <= n:

        bit[i] += v

        i += i & (-i)


def construct(arr, n):

    bit = [0]*(n+1)

    for i in range(n):
        updatebit(bit, n, i, arr[i])

    return bit


n, k = map(int, input().split())

intervals = []
for _ in range(k):
    a, b = map(int, input().split())
    intervals.append((a, b))
intervals.sort()


data = [0] * n
data[0] = 1
bit = construct(data, n)

mod = 998244353

for i in range(1, n):
    cnt = 0
    for a, b in intervals:
        if i - a < 0:
            break
        cnt += interval_sum(bit, max(i - b, 0), max(i - a, 0))
    cnt %= mod
    updatebit(bit, n, i, cnt)

print(interval_sum(bit, n - 1, n - 1) % mod)
