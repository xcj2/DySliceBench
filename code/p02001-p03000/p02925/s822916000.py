import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000000)

f = 0
def ts(E):
    L = []
    n = len(E)
    done = [0] * n
    checking = [0] * n
    def visit(j):
        global f
        checking[j] = 1
        if done[j] == 0:
            done[j] = 1
            for k in E[j]:
                if f: return 1
                if checking[k]:
                    f = 1
                    return 1
                visit(k)
                D[j] = max(D[j], D[k] + 1)
            L.append(j)
        checking[j] = 0
        return f
    for i in range(n):
        if visit(i):
            return []
    return L[::-1]

def ca(i, j):
    return max(i, j) * (max(i, j)-1) // 2 + min(i, j)

N = int(input())
M = N * (N-1) // 2
X = [[] for i in range(M)]
for i in range(N):
    A = [int(a)-1 for a in input().split()]
    for j in range(N-2):
        X[ca(i, A[j])].append(ca(i, A[j+1]))
D = [0] * M
L = ts(X)
print(max(D) + 1 if L else -1)