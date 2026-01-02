import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def read_values():
    return map(int, input().split())


def read_index():
    return map(lambda x: x - 1, map(int, input().split()))


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def functional(N, mod):
    F = [1] * (N + 1)
    for i in range(N):
        F[i + 1] = (i + 1) * F[i] % mod
    return F


def main():
    import queue
    N, M, K = read_values()

    friend = [set() for _ in range(N)]
    friend_num = [0] * N
    for _ in range(M):
        a, b = read_values()
        a -= 1
        b -= 1
        friend[a].add(b)
        friend[b].add(a)
        friend_num[a] += 1
        friend_num[b] += 1

    
    block = [set() for _ in range(N)]
    for _ in range(K):
        a, b = read_values()
        a -= 1
        b -= 1
        block[a].add(b)
        block[b].add(a)

    already = [False] * N
    C = [0] * N
    for i in range(N):
        if already[i]:
            continue
        s = {i}
        q = queue.Queue()
        already[i] = True
        q.put(i)
        while not q.empty():
            k = q.get()
            out = friend[k]
            for l in out:
                if already[l]:
                    continue
                s.add(l)
                q.put(l)
                already[l] = True
        c = len(s)
        for j in s:
            if c > len(block[j]):
                C[j] = c - len([p for p in block[j] if p in s])
            else:
                C[j] = len(s.difference(block[j]))
    res = [str(C[i] - friend_num[i] - 1) for i in range(N)]
    print(" ".join(res))


if __name__ == "__main__":
    main()