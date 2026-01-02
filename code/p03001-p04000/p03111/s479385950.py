# -*- coding: utf-8 -*-
import sys
# ----------------------------------------------------------------
# Use Solve Function

def solve(lines):
    def dfs(depth, l):
        if depth == 0:
            calc(l)
            return
        for i in range(4):
            dfs( depth - 1, l + str(i) )

    def calc(l):
        res = 0
        if not '0' in l or not '1' in l or not '2' in l:
            return
        aa = [[] for i in range(3)]
        for i,x in enumerate(list(l)):
            x = int(x)
            if x == 3:
                continue
            take = NLIST[i]
            aa[x].append(take)
        for i, a in enumerate(aa):
            if len(a) > 1:
                res += 10 * (len(a) - 1)
            res += abs(ABC[i] - sum(a))
        RESULT.append(res)




    RESULT = []
    N,A,B,C = map(int, lines.pop(0).split(' '))
    ABC = [A,B,C]
    NLIST = []
    for i in range(N):
        NLIST.append(int(lines.pop(0)))
    dfs(N, "")
    print(min(RESULT))
    
lines = [x.strip() for x in sys.stdin.readlines()]

#
# solve !!
#
solve(lines)