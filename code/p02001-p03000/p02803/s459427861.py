#!/usr/bin/env python3

import sys
# import math
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
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
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
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
    
    
    h, w = mi()
    maze = []
    maze.append(['#'] * (w + 2))
    for _ in range(h):
        maze.append(['#'] + li() + ['#'])
    maze.append(['#'] * (w + 2))

    # for line in maze:
    #     print(*line)


    def bfs(point_dist):
        'point から BFS を行い最も離れていた点との距離を返す'
        q = deque([point_dist])
        max_distance = 0
        while q:
            point, dist = q.popleft()
            i, j = point
            # 距離が最小であることは保証されるが各頂点からの共通の隣接頂点で距離が等しいものが重複登録されることはある
            if visited[i][j]:
                continue
            else:
                visited[i][j] = True
            max_distance = max(max_distance, dist)

            tmp = [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]
            for elm in tmp:
                if not visited[elm[0]][elm[1]] and maze[elm[0]][elm[1]] == '.':
                    q.append([elm, dist+1])
        return max_distance



    ans = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if maze[i][j] == '.':
                # print("{} {}".format(i, j))
                visited = [[False] * (w + 2) for _ in range(h + 2)]
                ans = max(ans, bfs([(i, j), 0]))
    
    print(ans)


if __name__ == "__main__":
    main()