#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_b -d test-b
oj test -d test-c -c "python abc116c.py"
oj test -d test-b -c "python abc116b.py" test-b/sample-3.in
"""

from collections import defaultdict
import sys
import math
import time
import itertools

#累積和
def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s) )
        return ret
    return wrapper


@deco
def sol(N, Q, S, LR):
    M = [0] * N
    logging.debug("%s, %s, %s, %s, %s" % (N, Q, S, LR, M))
    for i in range(1, N):
        logging.debug("i:%s" % i)
        if S[i-1] + S[i] == "AC":
            M[i] = M[i-1] + 1
        else:
            M[i] = M[i-1]

    A = [0]*Q
    for j in range(Q):
        l, r = int(LR[j][0])-1, int(LR[j][1])-1
        A[j] = M[r] - M[l]

    return A





import logging

do_submit = False
do_submit = True

if do_submit:
    logging.basicConfig(level=logging.ERROR, format="%(message)s")
else:
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(line.split()) for line in lines]
    (N, Q) = parsed_lines[0]
    N = int(N)
    Q = int(Q)
    S = parsed_lines[1][0]
    # return (n, S)
    LR = []
    for i in range(2, 2+Q):
        l , r = int(parsed_lines[i][0]), int(parsed_lines[i][1])
        LR.append((l, r))
    return (N, Q, S, LR)



if not do_submit:
    # n, S= input_parse("""
    # 4
    # 1 2 2 1
    # """)
    (N, Q, S, LR) = input_parse("""
    8 3
    ACACTACG
    3 7
    2 3
    1 8
    """)
    for a in sol(N, Q, S, LR):
        print (a)

    (N, Q, S, LR) = input_parse("""
    20 6
    AGCTAATTTACACGTAATCC
    3 7
    2 3
    1 8
    1 20
    9 18
    14 18
    """)
    for a in sol(N, Q, S, LR):
        print (a)

else:
    str = ""
    NQ = input().strip()
    N, Q= list(map(int, NQ.split()))
    str += NQ + "\n"
    str += input().strip() + "\n"# S
    for i in range(Q):
        str += input().strip() + "\n" # l, r
    (N, Q, S, LR) = input_parse(str)
    #print(sol(N, Q, S, LR))
    for a in sol(N, Q, S, LR):
        print (a)





