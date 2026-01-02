from string import ascii_lowercase
import sys


def input():
    return sys.stdin.readline().strip()


def sum_b(data, i):
    s = 0
    while i > 0:
        s += data[i]
        i -= i & -i
    return s


def add_b(data, i, x):
    while i <= n:
        data[i] += x
        i += i & -i


n = int(input())
s = input()
q = int(input())

bits = {c: [0] * (n + 1) for c in ascii_lowercase}
[add_b(bits[c], i, 1) for i, c in enumerate(s, 1)]

for q_type, *q in (input().split() for _ in range(q)):
    if q_type == '1':
        iq = int(q[0])
        cq = q[1]
        for b in bits.values():
            if sum_b(b, iq) - sum_b(b, iq - 1) == 1:
                add_b(b, iq, -1)
                break
        add_b(bits[cq], iq, 1)
    else:
        l, r = map(int, q)
        print(sum([bool(sum_b(b, r) - sum_b(b, l - 1) > 0) for b in bits.values()]))
