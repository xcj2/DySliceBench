import sys
sys.setrecursionlimit(100000)

N, M = [int(x) for x in input().split()]
g = 0

A = []
B = []

for i in range(M):
    a, b = [int(x) for x in input().split()]
    A.append(a)
    B.append(b)

A.reverse()
B.reverse()


# ----- Union Find -----------
PARENT = list(range( N + 1 ))
SIZE = [1] * (N + 1 )

def root(n):
    if PARENT[n] == n:
        return n
    else:
        ret = root(PARENT[n])
        PARENT[n] = ret
        return ret

def same(n1, n2):
    return root(n1) == root(n2)


def unite(n1, n2):
    n1 = root(n1)
    n2 = root(n2)
    if n1 == n2:
        return
    PARENT[n1] = n2
    global g
    g = g + SIZE[n2] * SIZE[n1]
    SIZE[n2] += SIZE[n1]
    SIZE[n1] = 0

Z = N * (N - 1) // 2

ans = []
for i in range(M):
    a, b = A[i], B[i]
    unite(a, b)
    # print(PARENT[1:])
    # print(SIZE[1:])
    # print(g)
    # print(Z - g)
    ans.append(Z - g)
    # print("----")

ans.reverse()
del ans[0]
for a in ans:
    print(a)
print(Z)
