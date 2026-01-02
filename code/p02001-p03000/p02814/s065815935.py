import sys
input = sys.stdin.readline
n, m = [int(x) for x in input().strip().split()]
a = list(set([int(x)//2 for x in input().strip().split()]))

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def div2cnt(x):
    ret = 0
    while x % 2 == 0:
        ret += 1
        x //= 2
    return ret

cnt = div2cnt(a[0])

for i, aa in enumerate(a):
    if div2cnt(aa) != cnt:
        print(0)
        exit()
    a[i] >>= cnt
else:
    m >>= cnt

lcm_ = 1
for aa in a:
    lcm_ = lcm(lcm_, aa)
    if lcm_ > m:
        print(0)
        exit()

print((m // lcm_ + 1) // 2)