#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, A: int, B: int, C: int, S: "List[str]"):
    L = 'ABC'
    ll = []
    def rec(i, a, b, c):
        #print(a, b, c, ll)
        if i == N:
            return ll
        s = S[i]
        vals = [a, b, c]
        if s == 'AB':
            u, v = 0, 1
        if s == 'BC':
            u, v = 1, 2
        if s == 'AC':
            u, v = 0, 2

        if vals[u] == 0 and vals[v] == 0:
            if len(ll) > 0:
                ll.pop()
            return False
        elif vals[u] == 1 and vals[v] == 1:
            ll.append(L[u])
            vals[u] += 1
            vals[v] -= 1
            tmp = rec(i + 1, vals[0], vals[1], vals[2])
            if tmp:
                return tmp
            else:
                ll.append(L[v])
                vals[u] -= 2
                vals[v] += 2
                return rec(i + 1, vals[0], vals[1], vals[2])
        elif vals[u] == 0 or (vals[v] > 1 and vals[u] == 1):
            ll.append(L[u])
            vals[u] += 1
            vals[v] -= 1
            return rec(i + 1, vals[0], vals[1], vals[2])
        else:
            ll.append(L[v])
            vals[u] -= 1
            vals[v] += 1
            return rec(i + 1, vals[0], vals[1], vals[2])

    ret = rec(0, A, B, C)
    if ret:
        print('Yes')
        for c in ret:
            print(c)
        '''
        vals = [A, B, C]
        for i in range(N):
            x = S[i]
            c = ret[i]
            for d in x:
                k = L.find(d)
                if d == c:
                    vals[k] += 1
                else:
                    vals[k] -= 1
            print(x, c)
            print(vals)
        '''
    else:
        print('No')

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, A, B, C, s)

if __name__ == '__main__':
    main()
