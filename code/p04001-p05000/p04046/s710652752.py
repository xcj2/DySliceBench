mod = int(1e9+7)


def exgcd(a, b, arr):
    if b == 0:
        arr.clear()
        arr.append(1)
        arr.append(0)
        return a
    else:
        d = exgcd(b, a % b, arr)
        x = arr[1]
        y = arr[0] - a//b * arr[1]
        arr[0] = x
        arr[1] = y
        return d


def Inv(a):
    arr = []
    exgcd(a, mod, arr)
    return (arr[0] + mod) % mod


H, W, A, B = map(int, input().split())

fac = [1 for i in range(H + W)]
for i in range(1, len(fac)):
    fac[i] = fac[i-1] * i % mod
inv = [1 for i in range(H+W)]
for i in range(0, len(inv)):
    inv[i] = Inv(fac[i])


def Cnm(n, m):
    return fac[n] * inv[n-m] * inv[m] % mod


ans = Cnm(H+W-2, H-1)
for i in range(1, B+1):
    tmp = Cnm(H-A+i-2, i-1) * Cnm(A+W-i-1, W-i) % mod
    ans = (ans - tmp + mod) % mod
print(ans)
