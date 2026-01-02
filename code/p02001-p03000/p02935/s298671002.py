from collections import defaultdict
import sys
import math
from datetime import datetime

def rec(S):
    if S is None: return 0
    elif len(S) == 1: return sum(S)
    elif len(S) == 2:
        return sum(S) / 2.0
    else: # len(S) >= 2
        S.sort()
        S[1] = (S[0] + S[1]) / 2.0
        return rec(S[1:])



def sol(n, S):
    return rec(S)



do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    n = int(parsed_lines[0][0])
    S = list(map(int, parsed_lines[1]))
    # S = parsed_lines[1][0]
    # return n, k, S
    return n, S


if not do_submit:
    n, S = input_parse("""
    3
    500 300 200
    """)
    print(sol(n, S))

    n, S = input_parse("""
    5
    138 138 138 138 138
    """)
    print(sol(n, S))




else:
    n = int(input().strip())
    S = list(map(int, input().split()))
    #S = input().split()
    # print(sol(n, k, S))

    #s = input().strip()
    # S = input().strip()
    print(sol(n, S))