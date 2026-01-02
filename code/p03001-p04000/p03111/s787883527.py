N, A, B, C = [int(_) for _ in input().split()]
L = [int(input()) for i in range(N)]

from itertools import combinations

def combi(xs, left):
    for i in range(len(xs) - left):
        for r in combinations(xs, i + 1):
            yield r

def diff(a, b):
    result = a[:]
    for x in b:
        if x in result:
            result.remove(x)
    return result

def calc(xs):
    result = 10**100
    for ra in combi(xs, 2):
        sa = abs(A - sum(ra)) + len(ra) * 10 - 10
        xsa = diff(xs, ra)
        for rb in combi(xsa, 1):
            sb = abs(B - sum(rb)) + len(rb) * 10 - 10
            xsb = diff(xsa, rb)
            for rc in combi(xsb, 0):
                sc = abs(C - sum(rc)) + len(rc) * 10 - 10
                total = sa + sb + sc
                result = min(result, total)
    return result

print(calc(L))
