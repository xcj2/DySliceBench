import sys
from collections import Counter
from math import ceil
def input():
    return sys.stdin.readline()[:-1]
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def main():
    N = int(input())
    P = []
    for _ in range(N):
        P.append(list(map(int,input().split())))
    P = sorted(P)
    K = []
    if N == 1:
        print(1)
        exit(0)
    for k in range(N-1):
        for l in range(k+1,N):
            a, b, c, d = P[k][0], P[k][1], P[l][0], P[l][1]
            e = c-a
            f = d-b
            K.append((e,f))
    C = Counter(K).most_common()
    S = set([])
    temp = 0
    for k in range(N-1):
        for l in range(k+1,N):
            a, b, c, d = P[k][0], P[k][1], P[l][0], P[l][1]
            e = c-a
            f = d-b
            if e == C[0][0][0] and f == C[0][0][1]:
                if k not in S or l not in S:
                    S.add(k)
                    S.add(l)
                    temp += 1
    print(N-temp)
if __name__ == '__main__':
    main()
