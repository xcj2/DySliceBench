#!python3

# input
N = int(input())


def prime_factor(x):
    m = {}
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
            x //= i
        i += 1
    if x != 1:
        m[x] = 1
    return m


def make_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


def main():
    m = prime_factor(N - 1)
    ans = 1
    for v in m.values():
        ans *= v + 1
    
    l = make_divisors(N)
    for x in l:
        y = N // x
        while y % x == 0:
            y //= x
        if y % x == 1:
            ans += 1
    
    print(ans)
    

if __name__ == "__main__":
    main()
