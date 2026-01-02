import sys
import math
import bisect
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


# A
def A():
    S = input()
    if S == 'AAA' or S == 'BBB':
        print('No')
    else:
        print('Yes')
    return


# B
def B():
    N, A, B = LI()
    ans = N // (A + B) * A + min(N % (A + B), A)
    print(ans)
    return


# C
def C():
    A, B = LI()
    for i in range(1, 1001):
        if i * 8 // 100 == A and i * 10 // 100 == B:
            print(i)
            return
    print(-1)
    return


# D
def D():
    s = S()
    d = deque(s)
    q = I()
    f = 1
    for i in range(q):
        query = input().split()
        if len(query) == 1:
            f *= -1
        else:
            if query[1] == '1':
                if f == 1:
                    d.appendleft(query[2])
                else:
                    d.append(query[2])
            else:
                if f == 1:
                    d.append(query[2])
                else:
                    d.appendleft(query[2])
    ans = ''.join(d)
    if f == -1:
        ans = ans[::-1]
    print(ans)
    return


# E
def E():
    return


# F
def F():
    return


# Solve
if __name__ == "__main__":
    D()
