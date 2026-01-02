import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
s = input().strip()
t = input().strip()

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

def cond(candidate):
    count = gcd(n, m)
    n_step = n // count
    m_step = m // count

    for i in range(count):
        if s[n_step * i] != t[m_step * i]:
            return False
    return True

candidate = lcm(n, m)

if cond(candidate):
    print(candidate)
else:
    print(-1)
