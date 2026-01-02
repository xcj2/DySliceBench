def biggest_cup(s,v):
    try:
        return s.index(v)
    except ValueError:
        return 127

def neighbors(s):
    a = biggest_cup(s,0)
    b = biggest_cup(s,1)
    c = biggest_cup(s,2)
    if b > a:
        t = list(s)
        t[a] = 1
        yield tuple(t)
    elif b < a:
        t = list(s)
        t[b] = 0
        yield tuple(t)
    if c > b:
        t = list(s)
        t[b] = 2
        yield tuple(t)
    elif c < b:
        t = list(s)
        t[c] = 1
        yield tuple(t)


def solve_bfs(s0, m):
    n = len(s0)
    visited = {s0}
    q = [s0]
    for i in range(m+1):
        nq = []
        for s in q:
            if all(v == 0 for v in s) or all(v == 2 for v in s):
                return i
            for t in neighbors(s):
                if t not in visited:
                    visited.add(t)
                    nq.append(t)
        q = nq
    return -1


def solve_optimized(s0, m):
    qq = []
    q = [s0]
    for i in range(m+1):
        nq = []
        for s in q:
            if all(v == 0 for v in s) or all(v == 2 for v in s):
                return i
            for t in neighbors(s):
                if t not in qq:
                    nq.append(t)
        qq,q = q,nq
    return -1

if __name__ == '__main__':
    while True:
        n,m = map(int,input().split())
        if n == m == 0:
            break
        s = [None]*n
        for i in map(int,input().split()[1:]):
            s[-i] = 0
        for i in map(int,input().split()[1:]):
            s[-i] = 1
        for i in map(int,input().split()[1:]):
            s[-i] = 2
        print(solve_optimized(tuple(s), m))
