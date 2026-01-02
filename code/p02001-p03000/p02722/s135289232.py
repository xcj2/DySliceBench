def main():
    def trial_division(n):
        divs = set()
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divs.add(i)
                if i != n//i:
                    divs.add(n//i)
        return divs

    def gcd(x, y):
        if y == 0:
            return x
        while y != 0:
            x, y = y, x % y
        return x

    N = int(input())
    ans = 0
    divs = trial_division(N) | trial_division(N-1)
    for d in divs:
        if d == 1:
            continue
        num = N
        while num % d == 0 and d <= num:
            num //= d
        if num % d == 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
