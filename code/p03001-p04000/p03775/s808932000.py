def f(a, b):
    a_len = len(str(a))
    b_len = len(str(b))
    if a_len > b_len:
        return a_len
    else:
        return b_len


def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors


def main():
    n = int(input())

    f_min = 11
    divisors = get_divisors(n)
    for i in divisors:
        for j in divisors:
            if i * j == n:
                f_min = min(f_min, f(i, j))
    print(f_min)


if __name__ == "__main__":
    main()
