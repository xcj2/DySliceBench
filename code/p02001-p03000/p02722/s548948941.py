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

    def soinsuu2(a):
        s = {1}
        for i, j in a.items():
            s2 = set()
            for k in range(1, j+1):
                for l in s:
                    s2.add(l*pow(i, k))
            s |= s2
        s.remove(1)
        return s

    n = int(input())

    ans = 0
    s = soinsuu(n)
    s2 = soinsuu2(s)
    for i in s2:
        m = n
        while m % i == 0:
            m //= i
        m -= 1
        if m % i == 0:
            ans += 1

    n -= 1
    ans2 = 1
    for i in soinsuu(n).values():
        ans2 *= i+1
    ans2 -= 1
    print(ans+ans2)


main()
