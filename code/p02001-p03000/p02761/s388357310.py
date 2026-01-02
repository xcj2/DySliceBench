import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


N, M = map(int, input().split())
cs = [None]*N
for i in range(M):
    s, c = map(int, input().split())
    #print(s, c)
    if cs[(s-1)] == None:
        cs[(s-1)] = c
    elif cs[s-1] != c:
        print(-1)
        exit()


def check(x):
    s = str(x)
    if not(len(s) == N):
        return False
    for i in range(N):
        if not(cs[i] == None or cs[i] == int(s[i])):
            return False
    return True


for i in range(10000):
    if check(i):
        print(i)
        exit()
print(-1)
