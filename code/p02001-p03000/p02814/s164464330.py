from functools import reduce

n, m = map(int, input().split())
A =[i//2 for i in list(map(int, input().split()))]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)


def cntTwo(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    return cnt

if len(set(map(cntTwo, A))) != 1:
    print(0)
    exit()

def merge(a, b):
    l = lcm(a, b)
    if l > 10 ** 9:
        return 0
    return l

x = reduce(merge, A)
if x == 0:
    print(0)
else:
    print(m//x - m//(x*2))
