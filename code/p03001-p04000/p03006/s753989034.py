#-*- coding: utf-8
#  -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""
from collections import defaultdict
import sys
import math
from datetime import datetime

def sol2(n, S):
    dp = defaultdict(int)
    pre_x = None
    pre_y = None
    for i, (x, y) in enumerate(S):
        #print(x, y, pre_x, pre_y)
        if i == 0:
            pre_x, pre_y = x, y
        else:
            dp[(x - pre_x, y - pre_y)] +=1
            pre_x, pre_y = x, y
    #print(dp)
    return n - max(dp.values())


def rec(S, pre, diff, n):
    if S == None or len(S) == 0 or len(S)==n: return 0

    tugi = (pre[0]+diff[0], pre[1]+diff[1])
    print("pre:%s, diff:%s, so tugi:%s while S:%s" % (str(pre), str(diff), str(tugi), S))
    if tugi in S:
        print("hit:%s" % str(tugi))
        S.remove(tugi)
        return 1 + rec(S, tugi, diff)
    else:
        print("end")
        return 0


def sol_botsu2(n, S):
    dp = defaultdict(int)
    if n == 1:
        return 1
    # n >= 2
    mx = 0
    tugi = S[1]
    for s in S:
        if tugi == s: continue
        tmp = rec(S[1:], s, (tugi[0]-s[0], tugi[1]-s[1]))
        mx = max(tmp, mx)

    return n - mx



def sol(n, S):
    PQ = []
    for s1 in S:
        for s2 in S:
            if s1 == s2: continue
            PQ.append((s2[0] - s1[0], s2[1] - s1[1]))
    mx = 0
    for p, q in set(PQ):
        tmp = 0
        for s1 in S:
            for s2 in S:
                if s1 == s2: continue
                if (s2[0] - s1[0], s2[1] - s1[1]) == (p, q):
                    tmp += 1
        mx = max(tmp, mx)

    return n - mx

do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    #print(parsed_lines)
    n = int(parsed_lines[0][0])
    #W = [int(x) for x in parsed_lines[1]]
    S = []
    for i in range(1, n+1):
        x = int(parsed_lines[i][0])
        y = int(parsed_lines[i][1])
        S.append((x, y))
    # k = int(parsed_lines[0][1])
    # S = parsed_lines[1][0]
    # return n, k, S
    return n, S


if not do_submit:
    n, S = input_parse("""
    2
    1 1
    2 2
    """)
    #print(sol(n, S))

    n, S = input_parse("""
    3
    1 4
    4 6
    7 8
    """)
    #print(sol(n, S))

    n, S = input_parse("""
    4
    1 1
    1 2
    2 1
    2 2
    """)
    print(sol(n, S))


else:
    n = int(input())
    S = []
    for i in range(n):
        x ,y = list(map(int, input().split()))
        S.append((x, y))
    # print(sol(n, k, S))
    #S = input().strip()
    # S = input().strip()
    print(sol(n, S))

