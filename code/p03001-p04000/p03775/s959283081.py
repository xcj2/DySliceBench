def large_digits(A, B):
    return max(len(str(A)), len(str(B)))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def main():
    N = int(input())
    divs = make_divisors(N)
    # loop = len(divs) // 2 + 1
    ans = 10**10 + 1
    for d in divs:
        ans = min(ans, large_digits(d, N // d))
    # print(divs)
    print(ans)

if __name__ == "__main__":
    main()