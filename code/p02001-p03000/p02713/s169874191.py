from collections import defaultdict
from itertools import permutations
# from math import gcd

def gcd(a, b):
    # ユークリッドの互除法による最大公約数
    if b == 0:
        return a
    return gcd(b, a % b)


def make_key2(i, j):
    return '-'.join([str(val) for val in sorted([i, j])])


def make_key3(i, j, k):
    return '-'.join([str(val) for val in sorted([i, j, k])])


if __name__ == '__main__':
    K = int(input())
    ans = 0
    mem2 = defaultdict()
    mem3 = defaultdict()
    for i in range(1, K + 1):
        for j in range(i, K + 1):
            for k in range(j, K + 1):

                set_ijk = list(set([i,j,k]))
                if len(set_ijk) == 1:
                    ans += i

                elif len(set_ijk) == 2:
                    key2 = make_key2(*set_ijk)
                    if key2 in mem2:
                        gcd1 = mem2[key2]
                    else:
                        gcd1 = gcd(*set_ijk)
                        mem2[key2] = gcd1
                    ans += gcd1 * 3
                else:
                    key3 = make_key3(*set_ijk)
                    if key3 in mem3:
                        gcd2 = mem3[key3]
                    else:
                        key2 = make_key2(i, j)
                        if key2 not in mem2:
                            gcd1 = gcd(i, j)
                            mem2[key2] = gcd1
                        else:
                            gcd1 = mem2[key2]

                        key2 = make_key2(gcd1, k)
                        if key2 not in mem2:
                            gcd2 = gcd(gcd1, k)
                            mem2[key2] = gcd2
                        else:
                            gcd2 = mem2[key2]
                    ans += gcd2 * 6

    print(ans)
