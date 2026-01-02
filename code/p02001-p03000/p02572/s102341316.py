def modpow(a, n, mod):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return (modpow((a * a)%mod, n//2, mod)) % mod
        else:
            return ((a%mod) * modpow(a, n-1, mod)) % mod

# modが素であるとする
def modinv(a, mod):
    return modpow(a, mod-2, mod) % mod

def moddiv(a, b, mod):
    return ((a%mod) * modinv(b, mod)) % mod


N = int(input())
A = [int(i) for i in input().split()]
mod = 10**9+7
sumA = sum(A)
result = (sumA * sumA) % mod
for i in range(N):
    result = result - (A[i]*A[i])%mod
print(moddiv(result, 2, mod))