
max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

from collections import defaultdict

def solve(U,R,D,L):

    def helper(U,R):
        A = defaultdict(list)
        B = defaultdict(list)
        for x,y in U:
            A[x+y].append(x)
        for x,y in R:
            B[x+y].append(x)
        m = 1000000
        for d,r in A.items():
            l = B[d]
            j = 0
            for li in l:
                while j < len(r) and li > r[j]:
                    j += 1
                if j == len(r):
                    break
                m = min2(m, r[j]-li)
        return m

    def helper2(U,D):
        A = defaultdict(list)
        B = defaultdict(list)
        for x,y in U:
            A[x].append(y)
        for x,y in D:
            B[x].append(y)
        m = 100000000
        for d,l in A.items():
            l.sort()
            r = B[d]
            r.sort()
            j = 0
            for li in l:
                while j < len(r) and li > r[j]:
                    j += 1
                if j == len(r):
                    break
                m = min2(m, r[j]-li)
        return m



    U.sort()
    R.sort()
    D.sort()
    L.sort()
    m = helper(U,R)
    A,B = [(-x,y) for x,y in U], [(-x,y) for x,y in L]
    A.reverse()
    B.reverse()
    m = min2(helper(A,B), m)
    A,B = [(x,-y) for x,y in D], [(x,-y) for x,y in R]
    m = min2(helper(A,B), m)
    A,B = [(-x,-y) for x,y in D], [(-x,-y) for x,y in L]
    A.reverse()
    B.reverse()
    m = min2(helper(A,B), m)
    m *= 10
    m = min2(helper2(U,D)*5, m)
    A,B = [(y,x) for x,y in L], [(y,x) for x,y in R]
    m = min2(helper2(B,A)*5, m)

    return m if m < 10000000 else 'SAFE'



if __name__ == '__main__':
    N = int(readline())

    t = iter(read().split())

    U,R,D,L = [],[],[],[]
    for x,y,u in zip(t,t,t):
        p = (int(x),int(y))
        u = u.decode('utf8')
        if u == 'U':
            U.append(p)
        elif u == 'R':
            R.append(p)
        elif u == 'D':
            D.append(p)
        else:
            L.append(p)

    print(solve(U,R,D,L))