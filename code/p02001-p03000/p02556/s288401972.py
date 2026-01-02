def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10

    def manhattan_distance(p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        return abs(x1-x2) + abs(y1-y2)
    
    def chebyshev_distance(p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        return max(abs(x1-x2),abs(y1-y2))



    N = II()
    # N = 10
    points = []
    from random import random
    f_0 = []
    f_1 = []
    for i in range(N):
        x,y = LMIIS()
        
        # x = int(random()*10**2)
        # y = int(random()*10**2)
        points.append((x,y))
        f_0.append(x-y)
        f_1.append(x+y)
    ans = 0
    ans = max(ans,max(f_0)-min(f_0))
    ans = max(ans,max(f_1)-min(f_1))
    
    print(ans)

    # ans2 = 0
    # for i in range(N):
    #     for j in range(i+1,N):
    #         tmp = manhattan_distance(points[i],points[j])
    #         if ans2 < tmp:
    #             max_pair2 = points[i],points[j]
    #             ans2 = tmp

    # print(ans2)
    # assert(ans==ans2)




main()