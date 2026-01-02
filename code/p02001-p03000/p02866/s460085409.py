#%%
import sys
def input():
    return sys.stdin.readline().rstrip()

import math

def func(i, j, d):
    if i <= 1:
        return 1
    e = j
    b = int(math.log2(d)/math.log2(i))
    ret = 1
    while e > b:
        ret = ret*(i**b%d)
        e = e - b
    else:
        if e > 0:
            ret = ret*(i**e%d)
    return ret


def main():
    N = int(input())
    Ds = [int(d) for d in input().split()]

    if Ds[0] != 0:
        print(0)
        return

    Ds.sort()
    if Ds[1] == 0:
        print(0)
        return

    i = 1
    l = 1
    r = 1
    ans = 1
    divider = 998244353

    while i < N:
        cnt = 0
        while i < N and Ds[i] == l:
            cnt = cnt + 1
            i = i + 1
        if cnt == 0:
            print(0)
            return

        ans = ans*func(r, cnt, divider)%divider
        r = cnt
        l = l + 1
    
    print(ans)

# %%
if __name__ == '__main__':
    main()

# %%
# from atcoder_test import doTest
# doTest("nikkei2019-2-qual","b",main)
