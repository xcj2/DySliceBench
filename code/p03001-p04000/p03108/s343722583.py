N, M = map(int, input().split())
lis = [[x, -1] for x in range(1, N + 1)]
Blis = [list(map(int, input().split())) for _ in range(M)]
inc = int(N*(N - 1)/2)
ans = [x for x in range(M)]
ans[M - 1] = inc
def root(a):
    if lis[a - 1][1] < 0:
        return lis[a - 1][0]
    else:
        k = root(lis[a - 1][1])
        lis[a - 1][1] = k
        return k
def size(a):
    return -lis[root(a) - 1][1]
def connect(a, b):
    A = root(a)
    B = root(b)
    if A == B:
        return None
    else:
        if size(A) < size(B):
            A, B = B, A
        lis[A - 1][1] += lis[B - 1][1]
        lis[B - 1][1] = A
for i in reversed(range(1, M)):
    if root(Blis[i][0]) != root(Blis[i][1]):
        ans[i - 1] = ans[i] - size(Blis[i][0])*size(Blis[i][1])
        connect(Blis[i][0], Blis[i][1])
    else:
      ans[i - 1] = ans[i]    
for i in range(M):
  print(ans[i])