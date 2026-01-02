import heapq
import sys
input = sys.stdin.readline

INF = 10**20
A = 50  # max A


def inpl():
    return list(map(int, input().split()))


def main():
    N, M, S = inpl()
    S = min(S, M * A)

    lines = [[] for _ in range(N * (M * A + 1))]
    for _ in range(M):
        in_s, in_t, cost, time = inpl()
        in_s -= 1
        in_t -= 1

        for n in range(cost, M * A + 1):
            s = in_s + n * N
            t = in_t + (n - cost) * N
            lines[s].append((t, time))

            s = in_s + (n - cost) * N
            t = in_t + n * N
            lines[t].append((s, time))

    for i in range(N):
        cost, time = inpl()
        for n in range(0, M * A + 1):
            s = i + n * N
            if n + cost > M * A:
                t = i + (M * A) * N
            else:
                t = i + (n + cost) * N
            lines[s].append((t, time))

    def dijkstra(N, S):
        weight = [INF] * N
        weight[S] = 0
        q = [[0, S]]
        heapq.heapify(q)
        while q:
            w0, s = heapq.heappop(q)
            for t, w in lines[s]:
                w += w0
                if weight[t] > w:
                    heapq.heappush(q, [w, t])
                    weight[t] = w

        return weight

    weight = dijkstra(N * (M * A + 1), 0 + S * N)

    ansl = [INF] * N
    for i, w in enumerate(weight):
        n = i % N
        if n == 0:
            continue
        else:
            ansl[n] = min(w, ansl[n])

    print("\n".join(map(str, ansl[1:])))


if __name__ == "__main__":
    main()
