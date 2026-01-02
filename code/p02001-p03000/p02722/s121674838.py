def main():
    from collections import Counter as ct

    def soinsuu(a):
        yy, j = [], 2
        y = yy.append
        while(a > 1):
            for i in range(j, int(a**0.5)+1):
                if a % i == 0:
                    y(i)
                    a, j = a//i, i
                    break
            else:
                y(a)
                break
        return ct(yy)

    def yakusuu(a):
        s = {1}
        for i, j in a.items():
            s |= {l*i**k for l in s for k in range(1, j+1)}
        s.remove(1)
        return s

    n = int(input())

    ans = 1
    for i in soinsuu(n-1).values():
        ans *= i+1
    ans -= 1

    for i in yakusuu(soinsuu(n)):
        m = n
        while m % i == 0:
            m //= i
        m -= 1
        if m % i == 0:
            ans += 1
    print(ans)


main()