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
def sol(S):
    zeroFirst= 0
    oneFirst = 0
    for i, s in enumerate(S):
        expected = '0' if i % 2 else '1'
        # 0 -> 0, 1 -> 1, 2 -> 0, 3-> 1
        logging.debug("expected {} and s {} zeroFirst {}, oneFirst {}".format(
            expected, s, zeroFirst, oneFirst
        ))
        if s == expected:
            oneFirst+=1
        else:
            zeroFirst+=1

    logging.debug("zeroFirst {}, oneFirst {}".format(zeroFirst, oneFirst))
    return min(oneFirst, zeroFirst)






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
    (S) = parsed_lines[0][0]
    return (S)



if not do_submit:
    (S) = input_parse("""
    10010010
    """)
    print (sol(S))

    (S) = input_parse("""
    000
    """)
    print (sol(S))

else:
    str = ""
    str = input().strip()
    (S) = input_parse(str)
    print (sol(S))





