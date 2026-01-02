import sys
from itertools import accumulate
from bisect import bisect
def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    ac = [0] + list(accumulate(A))

    def calc(lst): return abs(max(lst) - min(lst))
    def sm(l,r): return ac[r+1] - ac[l]

    ans = 10**18
    Q_left, S_left = 1, 3
    for R_left in range(2,N-1):
        P, Q = ac[Q_left], sm(Q_left, R_left-1)
        for nql in range(Q_left+1, R_left):
            nP, nQ = ac[nql], sm(nql, R_left-1)
            if calc([nP, nQ]) > calc([P, Q]): break
            Q_left, P, Q = nql, nP, nQ
        R, S = sm(R_left, S_left-1), sm(S_left, N-1)
        for nsl in range(S_left+1, N):
            nR, nS = sm(R_left, nsl-1), sm(nsl, N-1)
            if calc([nR, nS]) > calc([R, S]): break
            S_left, R, S = nsl, nR, nS
        ans = min(ans, calc([P,Q,R,S]))
    print(ans)

if __name__ == '__main__':
    main()
