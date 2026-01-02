def main():
    a, b = map(int, input().split())
    common_divisors = set(get_divisors(a)) & set(get_divisors(b))
    number_of_prime_common_divisor = sum([is_prime(i) for i in common_divisors])
    print(number_of_prime_common_divisor+1)

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

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x%2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0:
            return False
    return True

if __name__ == "__main__":
    main()