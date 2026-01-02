import sys
import heapq
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readline_s = sys.stdin.readline
readlines = sys.stdin.buffer.readlines

INF = 10 ** 10 + 7


def main():
    X, Y, Z, K = map(int, readline().split())
    A = sorted(list(map(int, readline().split())), reverse=True)
    B = sorted(list(map(int, readline().split())), reverse=True)
    C = sorted(list(map(int, readline().split())), reverse=True)

    ans = solve3(X, Y, Z, K, A, B, C)
    print('\n'.join(map(str, ans)))


def solve3(X, Y, Z, K, A, B, C):

    init_v = -(A[0] + B[0] + C[0])
    q = [(init_v, 0, 0, 0)]
    heapq.heapify(q)
    search = set()
    ans = []

    for k in range(K):
        v, a, b, c = heapq.heappop(q)
        ans.append(-v)
        if a + 1 < X and not ((a + 1, b, c) in search):
            nv = A[a + 1] + B[b] + C[c]
            heapq.heappush(q, (-nv, a + 1, b, c))
            search |= {(a + 1, b, c)}
        if b + 1 < Y and not ((a, b + 1, c) in search):
            nv = A[a] + B[b + 1] + C[c]
            heapq.heappush(q, (-nv, a, b + 1, c))
            search |= {(a, b + 1, c)}
        if c + 1 < Z and not ((a, b, c + 1) in search):
            nv = A[a] + B[b] + C[c + 1]
            heapq.heappush(q, (-nv, a, b, c + 1))
            search |= {(a, b, c + 1)}

    return ans


def solve2(X, Y, Z, K, A, B, C):

    ABC = []
    for i in range(X):
        if (i + 1) > K:
            break
        for j in range(Y):
            if (i + 1) * (j + 1) > K:
                break
            for k in range(Z):
                if (i + 1) * (j + 1) * (k + 1) > K:
                    break
                else:
                    ABC.append(A[i] + B[j] + C[k])

    return sorted(ABC, reverse=True)[:K]


def solve1(X, Y, Z, K, A, B, C):

    AB = []
    for i in range(X):
        for j in range(Y):
            AB.append(A[i] + B[j])

    AB.sort(reverse=True)
    AB = AB[:min(X * Y, K)]

    ABC = []
    for i in range(len(AB)):
        for j in range(Z):
            ABC.append(AB[i] + C[j])

    ABC.sort(reverse=True)

    return ABC[:K]


if __name__ == '__main__':
    main()
