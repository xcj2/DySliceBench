import sys
from collections import defaultdict, deque
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
    s = input()
    if s == "Sunny":
        print("Cloudy")
    elif s == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")
    return


# B
def B():
    s = S()
    for i in range(len(s)):
        if i % 2:
            if s[i] not in ["L", "U", "D"]:
                print("No")
                return
        else:
            if s[i] not in ["R", "U", "D"]:
                print("No")
                return
    print("Yes")
    return


# C
def C():
    n, k, q = LI()
    a = IR(q)
    sc = [0] * n
    for i in a:
        sc[i - 1] += 1
    for i in sc:
        print("Yes" if i > q - k else "No")
    return


# D
def D():
    n, m = LI()
    a = LI()
    q = []
    for i in range(n):
        heappush(q, -a[i])
    for i in range(m):
        x = heappop(q)
        x *= -1
        x >>= 1
        heappush(q, -x)
    print(-sum(q))
    return


# E
def E():
    return


# F
def F():
    return


# Unittest
def resolve():
    C()
    return


# Solve
if __name__ == "__main__":
    C()
