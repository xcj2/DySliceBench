N = int(input())
K = int(input())


def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def contain_one(n):
    a = 100
    max_num = 10**a

    while 1:
        if n // max_num == 0:
            a -= 1
            max_num = 10**a
        else:
            break

    return 9*a+(n//max_num)


def contain_two(n):
    if n <=10:
        return 0

    a = 100
    max_num = 10**a

    while 1:
        if n // max_num == 0:
            a -= 1
            max_num = 10**a
        else:
            break

    cnt = 0
    #10^a位まで
    for i in range(1, a):
        cnt += 9*9*i

    #10^a位
    tmp = n // max_num
    cnt += 9*a*(tmp-1)

    #nの10^a桁より小さい数
    tmp = n % max_num
    #怪しい
    if tmp != 0:
        cnt += contain_one(tmp)

    return cnt


def contain_three(n):
    if n <=100:
        return 0

    a = 100
    max_num = 10**a

    while 1:
        if n // max_num == 0:
            a -= 1
            max_num = 10**a
        else:
            break

    cnt = 0
    #10000以上の時ここがダメ
    for i in range(2, a):
        if i == 2:
            cnt += 9**2 * 9
        else:
            #3H(a-2) = aCa-2
            cnt += 9**2 * 9 * cmb(i, i-2)
            #aH2
            #cnt += 9**2 * 9 * (i*(i+1)//2)
            # tmp = tmp * 3
            # cnt += tmp


    tmp = n // max_num
    if a == 2:
        cnt += 9**2 * (tmp-1)
    else:
        cnt += 9**2 * (tmp-1) * cmb(a, a-2)


    tmp = n % max_num
    if tmp != 0:
        cnt += contain_two(tmp)

    return cnt


if K == 1:
    print(contain_one(N))
elif K == 2:
    print(contain_two(N))
else:
    print(contain_three(N))
