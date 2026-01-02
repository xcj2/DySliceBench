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

def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s) )
        return ret
    return wrapper


#@deco
def sol(S, n):
    cnt = 0
    ttl = sum(S)
    while ttl > 0:
        mark = False
        for i, s in enumerate(S):
            if s > 0:
                mark = True
                S[i]-=1
            elif mark and s == 0:
                break
        logging.debug("ttl:%s, cnt:%s, S:%s" % (ttl, cnt, S))
        cnt += 1
        ttl = sum(S)
    return cnt



import logging
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.basicConfig(level=logging.ERROR, format="%(message)s")
do_submit = True
#do_submit = False
def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    n = parsed_lines[0][0]
    S = parsed_lines[1]
    return (n, S)


if not do_submit:
    # n, S= input_parse("""
    # 4
    # 1 2 2 1
    # """)
    n, S= input_parse("""
    5
    3 1 2 3 1
    """)
    print(sol(S, n))
else:
    # a, b, c = list(map(int, input().split()))
    # print(sol(a, b, c))
    n = int(input())
    S = list(map(int, input().split()))
    print(sol(S, n))


