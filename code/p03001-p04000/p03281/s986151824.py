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


def len_divisor(x):
    m = prime_factor(x)
    ans = 1
    for n in m.values():
        ans *= n + 1
    return ans        


def main():
    ans = 0
    for i in range(1, N + 1, 2):
        if len_divisor(i) == 8:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
