
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))


n = getint()

array6 = [6]
while array6[-1] < n:
    array6.append(6 * array6[-1])

array9 = [9]
while array9[-1] < n:
    array9.append(9 * array9[-1])

cache = [-1] * (n + 1)
def solve(rest):
    res = cache[rest]
    if res >= 0:
        return res
    res = rest

    for m6 in reversed(array6):
        if m6 <= rest:
            res = min(res, solve(rest - m6) + 1)
            break
    for m9 in reversed(array9):
        if m9 <= rest:
            res = min(res, solve(rest - m9) + 1)
            break
    cache[rest] = res
    return res

print(solve(n))