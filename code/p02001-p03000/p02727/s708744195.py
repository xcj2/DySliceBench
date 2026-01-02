from pprint import pprint
from bisect import bisect_left
import numpy


def read():
    X, Y, A, B, C = list(map(int, input().strip().split()))
    P = list(map(int, input().strip().split()))
    Q = list(map(int, input().strip().split()))
    R = list(map(int, input().strip().split()))
    return X, Y, A, B, C, P, Q, R

def argsort(x, reverse=False):
    return sorted(range(len(x)), key=lambda k: x[k], reverse=reverse)

def solve(X, Y, A, B, C, P, Q, R):
    P = list(sorted(P, reverse=True))
    Q = list(sorted(Q, reverse=True))
    R = list(sorted(R, reverse=True))

    i = X
    j = Y
    score = sum(P[0:i]) + sum(Q[0:j])
    for r in R:
        if i > 0 and j > 0:
            if P[i-1] < Q[j-1] and P[i-1] < r:
                score = score - P[i-1] + r
                i -= 1
            elif Q[j-1] < r:
                score = score - Q[j-1] + r
                j -= 1
            else:
                break
        elif i > 0:
            if P[i-1] < r:
                score = score - P[i-1] + r
                i -= 1
            else:
                break
        elif j > 0:
            if Q[j-1] < r:
                score = score - Q[j-1] + r
                j -= 1
            else:
                break
        else:
            break
    return sum(P[:i] + Q[:j] + R[:(X-i)+(Y-j)])

if __name__ == '__main__':
    inputs = read()
    print("{}".format(solve(*inputs)))
