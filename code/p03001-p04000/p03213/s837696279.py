N = int(input())

def decompose(n):
    prime_exp = [0] * (n+1)
    for i in range(2, n+1):
        exponent = 0
        while(n % i == 0):
            n /= i
            exponent += 1
        if exponent != 0:
            prime_exp[i] = exponent
    return prime_exp

def decompose_fact(n):
    prime_exp = [0] * (n+1)
    for i in range(2, n+1):
        for j, k in enumerate(decompose(i)):
            prime_exp[j] += k
    return prime_exp

def solve(n):
    ans = 0
    dec_f = decompose_fact(n)
    for i in range(n+1):
        if dec_f[i] >= 74:
            ans += 1

    for i in range(n+1):
        for j in range(n+1):
            if i != j and (dec_f[i] >= 2 and dec_f[j] >= 24):
                ans += 1

    for i in range(n+1):
        for j in range(n+1):
            if i != j and (dec_f[i] >= 4 and dec_f[j] >= 14):
                ans += 1

    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if i != j and i != k and j != k and j < k and (dec_f[i] >= 2 and dec_f[j] >= 4 and dec_f[k] >= 4):
                    ans += 1
    return ans

print(solve(N))