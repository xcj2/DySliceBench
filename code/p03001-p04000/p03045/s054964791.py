N, M = map(int, input().split())

par = [i for i in range(N)]
rank = [0 for i in range(N)]


def get_root(A):
    if par[A] == A:
        return A
    par[A] = get_root(par[A])
    return par[A]


def connect(A, B):
    A = get_root(A)
    B = get_root(B)
    if rank[A] < rank[B]:
        par[A] = B
    else:
        par[B] = A
        if rank[A] == rank[B]:
            rank[A] += 1


def verify_connect(A, B):
    if get_root(A) == get_root(B):
        return True
    else:
        return False


for i in range(M):
    x, y, z = map(int, input().split())
    connect(x-1, y-1)
ans = 0
for i in range(N):
    if i == get_root(i):
        ans += 1

print(ans)
