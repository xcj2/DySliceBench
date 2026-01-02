#!/usr/bin/env python3

import sys
import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict (e.g. list is not allowed)
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4 (previous contest @AtCoder)


def main():
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79...e+308
    # inf = 2 ** 64 - 1               # (for fast JIT compile in PyPy) 1.84...e+19
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())


    def calc_minimum_num_of_problems(comp_list, target_score):
        constraints = problem[:]
        num_of_problems = 0
        for i, elm in enumerate(comp_list):
            # complete するという前提
            if elm:
                target_score -= problem[i] * (i + 1)    # 基礎点が全て確定
                target_score -= bonus[i]    # ボーナス点が確定
                num_of_problems += problem[i]    # 解いた問題に加算されてしまう
                constraints[i] = 0    # これ以上解いていい問題はない
            else:
                constraints[i] -= 1    # complete はしちゃダメ
        # print(f"comp list {comp_list}")
        # print(f"constrains {constraints}")
        # print(f"target {target_score}")
        # 後は基礎点が高い順に貪欲
        for i in range(d - 1, -1, -1):
            if target_score <= 0:
                break
            if constraints[i] * (i + 1) <= target_score:
                target_score -= constraints[i] * (i + 1)
                num_of_problems += constraints[i]
                constraints[i] = 0
            else:
                solved = math.ceil(target_score / (i + 1))
                target_score -= solved * (i + 1)
                assert(target_score <= 0)
                num_of_problems += solved
                constraints[i] -= solved
        if target_score > 0:
            num_of_problems = float('inf')
        # print(num_of_problems)
        return num_of_problems
    
    
    d, g = mi()
    g //= 100
    problem = []    # 第 k 問 (k 点) は problem[k-1] 個ある
    bonus = []    # 第 k 問をコンプすると bonus[k-1] 点を得る
    for _ in range(d):
        p, b = mi()
        problem.append(p)
        bonus.append(b // 100)
    
    ans = float('inf')
    for complete_or_not in product([True, False], repeat=d):
        ans = min(ans, calc_minimum_num_of_problems(complete_or_not, g))
    print(ans)



if __name__ == "__main__":
    main()
