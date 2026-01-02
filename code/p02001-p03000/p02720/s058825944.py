from collections import deque
import sys
sys.setrecursionlimit(200000)


def read():
    K = int(input())
    return K,


def dfs(i, d, s, q):
    if i == 1:
        q.append(s + str(d))
        return
    if d >= 1:
        dfs(i-1, d-1, s+str(d), q)
    dfs(i-1, d, s+str(d), q)
    if d < 9:
        dfs(i-1, d+1, s+str(d), q)


def solve(K):
    q = deque()
    for i in range(1, 11):
        for d in range(1, 10):
            dfs(i, d, "", q)
    return q[K-1]
    

if __name__ == '__main__':
    inputs = read()
    print("{}".format(solve(*inputs)))
