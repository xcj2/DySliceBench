import sys
def input():
    return sys.stdin.readline().rstrip('\n')

def make_a(n, M, L):
    if n == 0:
        return L
    W = len(L[0])
    newL = []
    for l in L:
        for i in range(l[W - 1], M + 1):
            newL += [list(l + [i])]
    return make_a(n - 1, M, newL)

def calc(N, M, Q, R):
    result = 0
    for A in make_a(N - 1, M, [[1]]):
        score = 0
        for a, b, c, d in R:
            score += (d if A[b - 1] - A[a - 1] == c else 0)
        result = max(score, result)
    return result


(N, M, Q) = tuple([int(s) for s in input().split()])
R = [tuple([int(s) for s in input().split()]) for _ in range(Q)]
print(calc(N, M, Q, R))