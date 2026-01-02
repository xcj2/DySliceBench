def gcd(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    if b == 0:
        return a
    else:
        r = a % b
        if r == 0:
            return b
        else:
            return gcd(b, r)

def lcm(a, b):
    g = gcd(a, b)
    return (a*b) // g

def count_baisuu(A, B, x): #AからBまでにxで割り切れる個数はどれだけか
    start = A
    stop = B
    modx_a = A % x
    if modx_a == 0:
        start = 0
        stop = B-A
    else:
        start = A-modx_a+x
        stop = B-start
        start = 0
    if stop < 0:
        return 0
    else:
        return 1 + stop // x 

A, B, C, D = map(int,input().split())
afromb = B-A+1 #B-A+1個の整数がある
cd_lcm = lcm(C, D)
#cの倍数,dの倍数, lcm(c,d)の倍数は最低でもいくつあるか
divc = count_baisuu(A, B, C)
divd = count_baisuu(A, B, D)
divcd = count_baisuu(A, B, cd_lcm)
print(str((B-A+1)-(divc+divd-divcd)))