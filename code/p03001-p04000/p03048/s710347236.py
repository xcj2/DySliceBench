def inpl():
    return list(map(int, input().split()))


def gcd(a, b):
    # greatest common divisor
    la = max(a, b)
    sm = min(a, b)
    if la % sm == 0:
        return sm
    else:
        return gcd(sm, la - sm)


def lcm(a, b):
    # least common multiple
    return a * b // gcd(a, b)

import sys

sys.setrecursionlimit(5000)


R, G, B, N = inpl()
ans = 0
for r in range(N // R + 1):
    rest = N - r * R
    for i in range(B):
        if (G * i) % B == rest % B:
            x = i
            break
    else:
        # print(r)
        continue
    if rest - G * x < 0:
        continue
    ans += (rest - G * x) // lcm(B, G) + 1
    # print(r, rest, x, ans)

print(ans)
