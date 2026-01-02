import sys
from itertools import permutations as perm
from bisect import bisect_left as bisect
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


def gcd(a, b):
    # greatest common divisor
    while b > 0:
        a, b = b, a % b

    return a


def solve():
    def get_ans(c1, c2, c3):
        ret = 0
        lenc3 = len(RGB[c3])
        for c1i in range(len(RGB[c1])):
            tmp = bisect(RGB[c2], RGB[c1][c1i])
            for c2i in range(tmp, len(RGB[c2])):
                c3i = bisect(RGB[c3], RGB[c2][c2i])
                if lenc3 == c3i:
                    continue
                # print(c1i, c2i, c3i)
                c21d = RGB[c2][c2i] - RGB[c1][c1i]
                t = bisect(RGB[c3], RGB[c2][c2i] + c21d, c3i)

                if lenc3 != t and RGB[c3][t] - RGB[c2][c2i] == c21d:
                    ret += lenc3 - c3i - 1
                else:
                    ret += lenc3 - c3i

        return ret
    int(input())
    S = list(input().strip())
    RGB = {k: [] for k in "RGB"}
    for i, s in enumerate(S):
        RGB[s].append(i)

    ans = 0
    # print(RGB)
    for c1, c2, c3 in perm(list("RGB")):
        # print(c1, c2, c3)
        ans += get_ans(c1, c2, c3)
        # print(ans)
    print(ans)


solve()
