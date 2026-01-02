import heapq

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
assert len(A) == X and len(B) == Y and len(C) == Z

# to reverse the order
A = [-x for x in A]
B = [-x for x in B]
C = [-x for x in C]

A.sort()
B.sort()
C.sort()

def val(pos):
    a, b, c = pos
    return A[a] + B[b] + C[c]

def nextpos(pos):
    a, b, c = pos
    if a + 1 < len(A):
        yield (a + 1, b, c)
    if b + 1 < len(B):
        yield (a, b + 1, c)
    if c + 1 < len(C):
        yield (a, b, c + 1)

def cakelist():
    H = []  # heap
    heapq.heappush(H, (val((0, 0, 0)), (0, 0, 0)))
    visited = {(0, 0, 0)}
    while len(H) > 0:
        v, pos = heapq.heappop(H)
        yield -v
        for npos in nextpos(pos):
            if npos not in visited:
                heapq.heappush(H, (val(npos), npos))
                visited.add(npos)

cl = cakelist()
for i in range(K):
    print(next(cl))
