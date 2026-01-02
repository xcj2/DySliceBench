#!/usr/bin/env python3

import sys
import math
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product                # product(iter, repeat=n)
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict
from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4


def main():
    mod = 1000000007                  # 10^9+7
    inf = float('inf')
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():  return int(input())
    def mi():  return map(int, input().split())
    def mi_0(): return map(lambda x: int(x)-1, input().split())
    def lmi(): return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():  return list(input())
    
    
    n, d, a = mi()
    monsters = sorted([lmi() for _ in range(n)])
    monster_points = []
    monster_hps= []
    for pair in monsters:
        monster_points.append(pair[0])
        monster_hps.append(pair[1])
    
    # どの monster_points[ind] での ind の表すモンスターまで巻き込めるか (右端)
    right_end_monster_ind = [0] * (n)
    for i in range(n):
        right_end_monster_ind[i] = bisect_right(monster_points, monster_points[i]+2*d) - 1
    
    # print(right_end_monster_ind)
    imos_list = [0] * (n+1)
    damage = 0
    ans = 0
    for i in range(n):
        damage += imos_list[i]
        rest_hp = max(0, monster_hps[i] - damage)
        # print("rest {}".format(rest_hp))
        cnt = math.ceil(rest_hp / a)
        ans += cnt
        imos_list[i+1] += (a * cnt)
        imos_list[right_end_monster_ind[i]+1] -= (a * cnt)
        # print(imos_list)
    
    print(ans)    


if __name__ == "__main__":
    main()