def main():
    A, B = map(int, input().split())

    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    def prime_factorize(n):
        arr = []
        temp = n
        for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])

        if temp != 1:
            arr.append([temp, 1])


        return arr

    cd = gcd(A, B)
    ans = len(prime_factorize(cd)) + 1
    print(ans)


if __name__ == "__main__":
    main()
