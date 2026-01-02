n = int(input())


# def main():
#     lft = 0
#     rgt = n
#     while rgt - lft > 1:
#         mid = (rgt + lft) // 2
#         if (n % mid) == 0 and ((n+1) % mid) == 0:
#             lft = mid
#         else:
#             rgt = mid
#     print(lft)

def main():
    p = prime_factor(n)
    ans = f([(i,j) for i, j in p.items()], 0, 1)
    print(ans)

def f(p, i, x):
    if i == len(p):
        tmp = n // x - 1
        if (tmp + 1) * x != n:
            return 0
        return tmp
    ans = 0
    tmp = 1
    for j in range(p[i][1]+1):
        ans += f(p, i+1, x*tmp)
        tmp *= p[i][0]
    return ans

def main():
    import math
    ans = 0
    for i in range(1, int(math.pow(n, 0.5)) + 2):
        if (n - i) % i == 0 and (n - i) // i > i:
            if n <= i:
                break
            ans += (n - i) // i

    print(ans)

def prime_factor(n):
    ret = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            ret[i] = ret.get(i, 0) + 1
            n /= i
        i += 1
    if n != 1:
        ret[n] = 1
    return ret


if __name__ == '__main__':
    main()
    2499694822001