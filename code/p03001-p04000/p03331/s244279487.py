def main():
    n = int(input())
    print(solve(n))

def digit_sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

def digit_sums_up(n):
    s = digit_sum(n)
    yield s

    while True:
        n += 1
        s += 1
        x = 10
        while n % x == 0:
            s -= 9
            x *= 10
        yield s

def digit_sums_down(n):
    s = digit_sum(n)
    yield s

    while True:
        x = 10
        while n % x == 0:
            s += 9
            x *= 10
        s -= 1
        n -= 1
        yield s

def solve(n):
    m = float('inf')
    for i, a, b in zip(range(n - 1), digit_sums_up(1), digit_sums_down(n - 1)):
        m = min(m, a + b)
    return m


main()