N, M = map(int, input().split())
Parent = [-1 for x in range(N + 5)]
lis = [list(map(int, input().split())) for _ in range(M)]
ini = int(N*(N - 1)/2)
ans = [x for x in range(M)]
ans[M - 1] = ini
def root(a):
    if Parent[a] < 0:
        return a
    else:
        k = root(Parent[a])
        Parent[a] = k
        return k
def size(a):
    return -Parent[root(a)]
def connect(a, b):
    A = root(a)
    B = root(b)
    if A == B:
        return None
    else:
        if size(A) < size(B):
            A, B = B, A
        Parent[A] += Parent[B]
        Parent[B] = A
for i in reversed(range(1, M)):
    ans[i - 1] = ans[i]
    if root(lis[i][0]) != root(lis[i][1]):
        ans[i - 1] -= size(lis[i][0])*size(lis[i][1])
        connect(lis[i][0], lis[i][1])    
for i in range(M):
  print(ans[i])