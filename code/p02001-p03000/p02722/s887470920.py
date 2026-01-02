

def main():
    N = int(input())

    def prime_factorize(n):
        res = []
        while n % 2 == 0:
            res.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                res.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            res.append(n)
        return res

    def isqrt(n):
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x

    # N = K^a * (bK + 1)
    # if a == 0


    ans = 1 # i == N-1
    for i in range(2, isqrt(N-1)+1):
        if (N-1) % i == 0:
            ans += 1
            if i != (N-1) // i:
                ans += 1
    
    # if a >= 1:
    divs = [N]
    for i in range(2, isqrt(N)+1):
        if N % i == 0:
            divs.append(i)
            j = N // i
            if i != j:
                divs.append(j)
    
    for div in divs:
        M = N
        while M % div == 0:
            M //= div
        if M % div == 1:
            ans += 1
    
    if N == 2:
        ans = 1
    print(ans)

if __name__ == "__main__":
    main()