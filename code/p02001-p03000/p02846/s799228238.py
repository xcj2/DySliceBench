from sys import stdin


def input():
    return stdin.readline()[:-1]


def intput():
    return int(input())


def sinput():
    return input().split()


def intsput():
    return map(int, sinput())


# Code

t1, t2 = intsput()

a1, a2 = intsput()

b1, b2 = intsput()

leap1 = a1 * t1 + a2 * t2
leap2 = b1 * t1 + b2 * t2

if leap1 == leap2:
    print('infinity')
    exit()


if leap2 < leap1:
    a1, a2, b1, b2 = b1, b2, a1, a2
    leap1, leap2 = leap2, leap1

lag = leap2 - leap1

# 1 is always slower
if a1 < b1 and a2 < b2:
    print(0)
    exit()

if a1 > b1:
    gap = (a1 - b1) * t1
    q = gap // lag
    ans = q * 2 + 1
    if lag * q == gap:
        ans -= 1
    print(ans)
    exit()

print(0)
