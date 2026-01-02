def gcd(a, b):
    if a > b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(n, m, s, t):
    if s == t:
        return n
    else:
        l = lcm(n, m)
        dx = l // n
        dy = l // m
        x = 0
        y = 0
        cx = 0
        cy = 0
        while cx < n and cy < m:
            if x == y:
                if s[cx] != t[cy]:
                    return -1
                x += dx
                cx += 1
                y += dy
                cy += 1
            elif x < y:
                x += dx
                cx += 1
            else:
                y += dy
                cy += 1
        return l

_n, _m = map(int, input().split())
_s = input()
_t = input()
print(solve(_n, _m, _s, _t))
