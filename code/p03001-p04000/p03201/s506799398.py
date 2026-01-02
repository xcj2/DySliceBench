#!/usr/bin/env python3
import sys, os
try: from typing import Any, Union, List, Tuple, Dict
except ImportError: pass
sys.setrecursionlimit(10**6)
def debug(*args): pass # if os.environ.get("USER")=="shun" else None
def exit(): sys.exit(0)


n = int(input())
a = list(map(int, input().split()))
a.sort()
max_a = a[-1]
m = 0
while True:
    if 2**m > max_a:
        break
    m += 1
used = [False] * n


def bisect(val, start, end):
    debug(used)
    if start >= end:
        return None
    elif start + 1 == end:
        if a[start] == val:
            if used[start]:
                return None
            used[start] = True
            return start
        else:
            return None
    mid = (start + end) // 2
    if a[mid] == val:
        if used[mid]:
            res = bisect(val, start, mid)
            return res
        else:
            res = bisect(val, mid+1, end)
            if res is not None:
                return res
            used[mid] = True
            return mid
        # if used[mid]:
        #     res = bisect(val, mid+1, end)
        #     if res is not None:
        #         return res
        #     res = bisect(val, start, mid)
        #     return res
        # else:
        #     used[mid] = True
        #     debug("fuga", used)
        #     return mid
    elif a[mid] > val:
        return bisect(val, start, mid)
    else:
        return bisect(val, mid, end)
    # for i in reversed(range(end)):
    #     if (not used[i]) and (a[i]  == val):
    #         used[i] = True
    #         return i
    return None


def _find(b, end, e):
    # debug(b, end, e)
    val = 2**e - b
    if val <= 0:
        return None
    return bisect(val, 0, end)
    # for i in reversed(range(end)):
    #     if (not used[i]) and (a[i] + b == 2**e):
    #         used[i] = True
    #         return i
    # return None


def find(b, end):
    for e in reversed(range(m+1)):
        res = _find(b, end, e)
        if res is not None:
            return True
    return False


ans = 0
for j in reversed(range(n)):
    if used[j]:
        continue
    b = a[j]
    used[j] = True
    res = find(b, j)
    if res:
        ans += 1


print(ans)
