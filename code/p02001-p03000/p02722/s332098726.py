def main():
    n = int(input())
    ans = set()
    divisors = get_divisors(n)
    ans |= set(get_divisors(n-1))
    ans |= set([divisor for divisor in divisors if is_ok(n, divisor)])
    ans -= set([1])
    print(len(ans))

def is_ok(n, d):
    if d < 2:
        return False
    while n%d == 0:
        n //= d
    return n%d == 1

def get_divisors(n):
    out = []
    if n < 1:
        return out
    m = int(n**0.5)
    for i in range(1, m+1):
        if not n%i:
            out.append(i)
            if n != i**2:
                out.append(n//i)
    return out


if __name__ == "__main__":
    main()