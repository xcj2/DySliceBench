import sys
sys.setrecursionlimit(10**8)
def line_to_int(): return int(sys.stdin.readline())
def line_to_each_int(): return map(int, sys.stdin.readline().split())
def line_to_list(): return list(map(int, sys.stdin.readline().split()))
def line_to_list_in_iteration(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
# def dp(init, i, j): return [[init]*i for i2 in range(j)]
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
# from itertools import accumulate #A = [0]+list(accumulate(A))
# import bisect #bisect.bisect_left(B, a), bisect.bisect_right(B,a)

n = line_to_int()
a = line_to_list()

# from functools import reduce, partial
# from operator import mul

# prod = partial(reduce, mul)

# if 0 in a:
#     print(0)
# else:
#     if prod(a) <= 10**18:
#         print(prod(a))
#     else:
#         print(-1)
ans = a[0]
limit = 10**18
if 0 in a:
    print(0)
else:
    for i in range(1,n):
        if ans <= limit:
            ans = ans * a[i]
        else:
            print(-1)
            exit()
    if ans <= limit:
        print(ans)
    else:
        print(-1)