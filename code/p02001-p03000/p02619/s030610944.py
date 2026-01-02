import sys
from itertools import accumulate
import bisect

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    D = ii()
    c = list(mi())
    s = [list(mi()) for i in range(D)]

    t = [ii()-1 for i in range(D)]

    last = [[0]*26 for i in range(D)]
    v = [0]*D

    for d in range(D):
        for i in range(26):
            if i == t[d]:
                last[d][i] = d+1
            else:
                last[d][i] = last[d-1][i]

        k = sum(c[i]*(d+1-last[d][i]) for i in range(26))
        v[d] = v[d-1] + s[d][t[d]] - k
    
    print(*v, sep='\n')


if __name__ == '__main__':
    main()
