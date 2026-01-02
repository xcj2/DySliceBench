def main():
    N, M = (int(i) for i in input().split())

    def gcd(x, y):
        if y == 0:
            return x
        while y != 0:
            x, y = y, x % y
        return x

    def trial_division(n):
        divs = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divs.append(i)
                if i != n//i:
                    divs.append(n//i)
        return divs

    if M % N == 0:
        return print(M//N)

    divs = [i for i in trial_division(M) if i >= N]
    print(M//min(divs))


if __name__ == '__main__':
    main()
