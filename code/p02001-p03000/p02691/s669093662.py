def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

from bisect import bisect_right
from bisect import bisect_left
import copy

N = read_int()
An = read_int_list()

An_diff = [0]*N
for i,a in enumerate(An):
    An_diff[i] = a - i
An_store = copy.deepcopy(An_diff)
An_diff.sort()
count_map = {}
ans = 0
for i,a in enumerate(An):
    target = (a+i)*(-1)
    shoud_be_minus_cnt = An_store[i]
    if shoud_be_minus_cnt not in count_map:
        count_map[shoud_be_minus_cnt] = 1
    else:
        count_map[shoud_be_minus_cnt] += 1
    cnt = bisect_right(An_diff,target) - bisect_left(An_diff,target)
    if target in count_map:
        cnt -= count_map[target]
    ans += cnt
print(ans)