import sys
readline = sys.stdin.readline

P = 10 ** 9 + 7
def mod_prod(a,b):
    return (a % P) * (b % P) % P

def mod_fact(a):
    ret = 1
    for i in range(a):
        ret = ret * (i + 1) % P
    return ret

def mod_pow(a, n):
    ret = 1
    while n > 0:
        if n % 2 == 1:
            ret = ret * a % P
        a = a * a % P
        n = n >> 1
    return ret

def mod_div(a, b):
    b_inv = mod_pow(b, P - 2)
    return a * b_inv % P

def mod_comb(a,b):
    ret = 1
    b = min(b, a - b)
    for i in range(b):
        ret *= a - i
        ret %= P
    ret = mod_div(ret, mod_fact(b))
    return ret

def solve():
    K = int(readline())
    S = readline().rstrip()

    N = len(S)

    ans = 0
    cb = 1
    for i in range(K + 1):
        ans += mod_pow(25, i) * cb * mod_pow(26, K-i)
        cb = cb * mod_div(i + N - 1 + 1, i + 1) % P
        # mod_comb(i+N-1, i)
        ans %= P
    print(ans)

solve()