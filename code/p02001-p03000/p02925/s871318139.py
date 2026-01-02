N = int(input())
A = [list(map(int, input().split())) for n in range(N)]
P = [0] * N


def get_num(i):
    return A[i][P[i]] - 1


def update(mem, K):
    for i in mem:
        P[i] += 1
        if P[i] == N - 1:
            K.remove(i)


def f():
    K = {i for i in range(N)}
    L = {i for i in range(N)}
    mem = set()
    for t in range(N * (N - 1) // 2 + 1):
        if len(K) == 0:
            return t

        for i in L:
            if i in mem:
                continue

            j = get_num(i)
            if j in mem:
                continue

            if i == get_num(j):
                mem.add(i)
                mem.add(j)

        if len(mem) == 0:
            return -1
        update(mem, K)
        L = K & mem
        mem.clear()

    return -2

print(f())
