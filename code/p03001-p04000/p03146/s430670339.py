from collections import defaultdict
import sys

import math

def f(a):
    if a % 2 == 0: return a/2
    else: return  3*a + 1

def sol(a):
    dp = [a]
    #print(dp)
    for i in range(1, 1000000+1):
        x = dp[i-1]
        ans = f(x)
        if ans in dp:
            #print(i, ans, dp)
            return i+1
        else:
            dp.append(ans)
    return None




do_submit = True
#do_submit = False
def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    a = parsed_lines[0]
    return a[0]


if not do_submit:
    a= input_parse("""
    54
    """)
    print(sol(a))
else:
    # a, b, c = list(map(int, input().split()))
    # print(sol(a, b, c))
    a = list(map(int, input().split()))
    print(sol(a[0]))