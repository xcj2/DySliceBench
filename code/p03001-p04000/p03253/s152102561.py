n, m = map(int, input().split())

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y // 2) ** 2 % mod
    else            : return power(x, y // 2) ** 2 * x % mod

mod = 10 ** 9 + 7

N = 10 ** 6
factorial = [1]
for i in range(1, N):
    factorial.append(factorial[i - 1] * i % mod)

inverseFactorial = [0] * N
inverseFactorial[N - 1] = power(factorial[N - 1], mod - 2)
for i in range(N - 2, -1, -1):
    inverseFactorial[i] = inverseFactorial[i + 1] * (i + 1) % mod

def comb(x, y):
    return factorial[x] * inverseFactorial[y] * inverseFactorial[x - y] % mod

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

facts = factorization(m)

if m == 1:
    print(1)
else:
    ans = 1
    for a, b in facts:
        ans *= comb(n+b-1, b)
        ans %= mod
    print(ans)
