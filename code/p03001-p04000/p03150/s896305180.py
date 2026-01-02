import re
import sys

sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):
    return [il(t) for _ in range(N)]


S = ii(str).lower()
if S == "keyence":
    print("YES")
    exit()
if (
    re.sub("k[a-z]*eyence", "", S)
    and re.sub("ke[a-z]*yence", "", S)
    and re.sub("key[a-z]*ence", "", S)
    and re.sub("keye[a-z]*nce", "", S)
    and re.sub("keyen[a-z]*ce", "", S)
    and re.sub("keyenc[a-z]*e", "", S)
    and re.sub("keyence[a-z]*", "", S)
):
    print("NO")
else:
    print("YES")
