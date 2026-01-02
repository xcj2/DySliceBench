import math

def euclid(a, b):
    if a == b:
        return a
    elif b > a:
        return euclid(b, a)
    else:
        while b > 0:
            temp = a % b
            a = b
            b = temp
        return a


def get_e(x):
    l = []
    i = 2
    m = math.floor(math.sqrt(x))
    while i <= m and i <= x:
        if x % i == 0:
            x = x // i
            l += [i]
        else:
            i += 1
    if x != 1:
        l += [x]
    return l


def calc(A, B):
    gcd = euclid(A, B)
    if gcd == 1:
        return 1
    else:
        return 1 + len(set(get_e(gcd)))


(A, B) = tuple([int(s) for s in input().split(' ')])
print(calc(A, B))