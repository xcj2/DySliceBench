# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0096
"""
import sys


Memo = [0 for _ in range(2001)]
def init_memo():
    global Memo
    # a, b??????????????°?????§ 0???2000?????????????????????????????°??????????????????
    for a in range(1000+1):
        for b in range(1000+1):
            Memo[a+b] += 1


def solve(target):
    global Memo
    ans = 0
    for ab in range(min(target+1, 2001)):
        cd = target - ab
        if 0 <= cd <= 2000:
            ans += Memo[ab] * Memo[cd]
    return ans


def main(args):
    init_memo()
    for line in sys.stdin:
        target = int(line.strip())
        result = solve(target)
        print(result)


if __name__ == '__main__':
    main(sys.argv[1:])