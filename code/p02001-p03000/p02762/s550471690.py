from operator import itemgetter

N, M, K = map(int, input().split())

par = [i for i in range(N)]
rank = [1 for i in range(N)]

def get_root(A):
    if par[A] == A:
        return A
    par[A] = get_root(par[A])
    return par[A]

def connect(A, B):
    A = get_root(A)
    B = get_root(B)
    if A == B:
        return
    if rank[A] < rank[B]:
        A, B = B, A
    par[B] = A
    rank[A] += rank[B]
    rank[B] = 0


def verify_connect(A, B):
    if get_root(A) == get_root(B):
        return True
    else:
        return False


# like
like_path = [[] for i in range(N)]
like_query = [input() for i in range(M)]
dislike_query = [input() for i in range(K)]
for line in like_query:
    A, B = map(int, line.split())
    connect(A-1, B-1)
    like_path[A-1].append(B-1)
    like_path[B-1].append(A-1)

tmp_ans = []
for i in range(N):
    tmp_ans.append(rank[get_root(i)]-len(like_path[i])-1)

for line in dislike_query:
    A, B = map(int, line.split())
    if verify_connect(A-1, B-1):
        tmp_ans[A-1] -= 1
        tmp_ans[B-1] -= 1

print(" ".join(map(str, tmp_ans)))
