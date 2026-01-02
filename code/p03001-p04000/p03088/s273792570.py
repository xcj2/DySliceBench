# -*- coding: utf-8 -*-
"""
D - We Like AGC
https://atcoder.jp/contests/abc122/tasks/abc122_d

"""
import sys
import re

N = None
memo = None

def ok(last4):
    if re.search(r'AGC|GAC|ACG|A.GC|AG.C', last4):
        return False
    return True


def dfs(cur, last3):
    global memo
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1

    ret = 0
    for c in 'ACGT':
        if ok(last3 + c):
            ret = (ret + dfs(cur + 1, last3[1:]+c)) % (10**9 + 7)
    memo[cur][last3] = ret
    return ret


def main(args):
    global N, memo
    N = int(input())
    memo = [dict() for i in range(N+1)]
    ans = dfs(0, 'TTT')
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
