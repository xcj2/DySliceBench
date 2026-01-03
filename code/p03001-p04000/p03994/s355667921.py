#!/usr/bin/env python3
import sys
try: from typing import Any, Union, List, Tuple, Dict
except ImportError: pass
def debug(*args): print(*args, file=sys.stderr)
def exit(): sys.exit(0)


s = input()
K = int(input())
n = len(s)


def code(s):
    return ord(s)-97

def char(c):
    c = c % 26
    return chr(c+97)


# ans = ""
ans_list = []
for p in range(n):
    c = code(s[p])
    if c == 0:
        # ans += "a"
        ans_list.append("a")
        continue
    if 26-c > K:
        # ans += s[p]
        ans_list.append(s[p])
        continue
    # ans += "a"
    ans_list.append("a")
    K -= 26-c
ans = "".join(ans_list)
ans = ans[:-1] + char(code(ans[-1])+K)

print(ans)
