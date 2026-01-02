#!/usr/bin/env python3
import sys
try: from typing import Any, Union, List, Tuple, Dict
except ImportError: pass
sys.setrecursionlimit(10**6)
def debug(*args): print(*args, file=sys.stderr)
def exit(): sys.exit(0)


N, X = map(int, input().split())
x = [0] + list(map(int, input().split()))


r = [0, 0]
rr = 0
for j in range(1, N+1):
    rr += x[j]
    r.append(rr)


def f(k):
    # debug("compute %s" % k)
    s = 0
    m = N // k + 1
    # s += 2*(r[N+1] - r[(m-1)*k])
    # for l in range(k):
    #     n = (N-l) // k
    #     s += x[l+k*n]*2
    s += 2*(r[N+1] - r[N-k+1])
    for i in range(1, m+1):
        # if k*(m-i+1) > N:
        #     t = r[N+1]
        # else:
        #     t = r[k*(m-i+1)]
        t = r[N-k*(i-1)+1]
        if N-k*i+1 < 0:
            u = 0
        else:
            u = r[N-k*i+1]
        s += (2*i+1)*(t-u)
    return s


# def f(k):
#     # debug("compute %s" % k)
#     s = 0
#     # m = N // k + 1
#     # s += 2*(r[N+1] - r[(m-1)*k])
#     for l in range(k):
#         n = (N-l) // k
#         s += x[l+k*n]*2
#         for i in range(1, n+2):
#             s += (2*i+1)*x[l+k*(n-i+1)]
#     return s


# def g(k):
#     s = 0
#     for l in range(k):
#         n = (N-l) // k
#         s += x[l+k*n]
#         for i in range(1, n+2):
#             if l+k*(n-i) < 0:
#                 y = 0
#             else:
#                 y = x[l+k*(n-i)]
#             s += ((i+1)**2)*(x[l+k*(n-i+1)] - y)
#     return s


candidates = [f(k) + k*X + N*X for k in range(1, N+1)]
debug(candidates)

# cand = [g(k) + k*X + N*X for k in range(1, N+1)]
# debug(cand)

ans = min(candidates)
print(ans)
