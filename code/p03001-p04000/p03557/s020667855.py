def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD = 10 ** 9 + 7


def to_cumsum(arr, pad=True):
    """
    1次元配列を累積和の1次元配列に変換する
    pad: 先頭に0の項を作る場合はTrue
    """
    cumsum = 0
    padding = 1 if pad else 0
    new = [0] * (len(arr) + padding)
    for i, e in enumerate(arr):
        cumsum += e
        new[i + padding] = cumsum
    return new


N = I()
A = LMI()
B = LMI()
C = LMI()

A.sort()
B.sort()
C.sort()


def bi(A, x):
    l = -1
    r = len(A)
    while l + 1 < r:
        p = (l + r) // 2
        if x < A[p]:
            r = p
        else:
            l = p
    return r


BC = [0] * N
for i, b in enumerate(B):
    BC[i] = N - bi(C, b)
BC = to_cumsum(BC)
ans = 0
for i, a in enumerate(A):
    ans += BC[N] - BC[bi(B, a)]
print(ans)
