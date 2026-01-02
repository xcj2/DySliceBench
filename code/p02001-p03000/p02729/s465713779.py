def sq(a, b, mod):  # aのb乗を剰余,kは初期値#20191116-D-Knight
    if b == 0:
        return 1
    elif b % 2 == 0:
        return sq(a, b // 2, mod)**2 % mod
    else:
        return sq(a, b - 1, mod) * a % mod


def nCk(n, k, mod=10 ** 9 + 7):
    x = max(k, n - k)
    y = min(k, n - k)
    kkai = 1
    for i in range(2, y + 1):
        kkai = (kkai * i) % mod
    nkkai = 1
    for i in range(x + 1, n + 1):
        nkkai = (nkkai * i) % mod
    answer = sq(kkai, mod - 2, mod) * nkkai % mod
    return answer

N, M = map(int, input().split())
def c(num):
    if num == 1 or num == 0:
        return 0
    else:
        return (num * (num-1))//2
print(c(N)+c(M))