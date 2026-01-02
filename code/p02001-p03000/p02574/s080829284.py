import math

n = int(input())
a = list(map(int, input().split()))


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def is_pairwise():
    cs = [0] * 1000010
    for i in a:
        for p, _ in factorization(i):
            if p != 1 and cs[p] == 1:
                return False
            cs[p] = 1
    return True


def is_setwise():
    c = a[0]
    for i in a:
        c = math.gcd(c, i)
    return c == 1


if is_pairwise():
    print('pairwise coprime')
elif is_setwise():
    print('setwise coprime')
else:
    print('not coprime')
