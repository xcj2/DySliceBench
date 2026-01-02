#!/usr/bin/env python3

import sys
# import math
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
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
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
    

    def parse(com):
        if com == 'AB':
            return 0, 1
        elif com == 'BC':
            return 1, 2
        else:
            return 0, 2

    def sim_1(t_copy, commands):
        s = 'ABC'
        result = []
        for com in commands:
            i, j = parse(com)
            if t_copy[i] == 0 and t_copy[j] == 0:
                return False, result
            elif t_copy[i] == 0:
                result.append(s[i])
                t_copy[i], t_copy[j] = 1, 0
            else:
                result.append(s[j])
                t_copy[i], t_copy[j] = 0, 1
        return True, result
    

    def sim_2(t_copy, commands):
        s = 'ABC'
        size = len(commands)
        result = []
        for k in range(size):
            # print(t_copy)
            com = commands[k]
            i, j = parse(com)
            if t_copy[i] == 0 and t_copy[j] == 0:
                raise RuntimeError
            # 配分後は必ず (1 以上, 1 以上, 0 以上)
            elif t_copy[i] == 0:
                result.append(s[i])
                t_copy[i] += 1
                t_copy[j] -= 1
            elif t_copy[j] == 0:
                result.append(s[j])
                t_copy[j] += 1
                t_copy[i] -= 1
            else:
                # 片方はどうしても 0 になってしまう
                if t_copy[i] == 1 and t_copy[j] == 1:
                    if k != size - 1:
                        next_com = commands[k + 1]
                        next_i, next_j = parse(next_com)
                        if not (i == next_i and j == next_j):
                            next_duplicate_one = list(set([i, j]) & set([next_i, next_j]))[0]
                            tmp = [next_i, next_j]
                            tmp.remove(next_duplicate_one)
                            next_not_duplicate = tmp[0]
                            if t_copy[next_not_duplicate] == 0:
                                result.append(s[next_duplicate_one])
                                t_copy[next_duplicate_one] += 1
                                tmp = [i, j]
                                tmp.remove(next_duplicate_one)
                                res = tmp[0]
                                t_copy[res] -= 1
                                continue    # ここを忘れてハマり続けた...
                    # 自由？
                    result.append(s[i])
                    t_copy[i] += 1
                    t_copy[j] -= 1
                # 0 にならないですむ                 
                elif t_copy[i] <= t_copy[j]:
                    result.append(s[i])
                    t_copy[i] += 1
                    t_copy[j] -= 1
                else:
                    result.append(s[j])
                    t_copy[j] += 1
                    t_copy[i] -= 1
        return result
            
    
    n, a, b, c  = mi()
    t = [a, b, c]
    commands = [input() for _ in range(n)]
    i, j = parse(commands[0])
    # (0, 0, 0)
    if sum(t) == 0:
        predicate = False
    # (1, 0, 0)
    elif sum(t) == 1:
        predicate, result = sim_1(t[:], commands)
    # (2 以上, 0, 0) で最初に沈む
    elif t.count(0) == 2 and t[i] == 0 and t[j] == 0:
        predicate = False
    # (2 以上, 0, 0) で最初に沈まない
    # (1 以上, 1 以上, 0)
    # (1 以上, 1 以上, 1 以上)
    # うまく立ち回り続ける
    else:
        predicate = True
        result = sim_2(t[:], commands)
    
    if predicate:
        print('Yes')
        print(*result, sep='\n')
    else:
        print('No')


if __name__ == "__main__":
    main()

