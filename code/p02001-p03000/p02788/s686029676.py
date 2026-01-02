def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


import heapq
def main():
    N, D, A = read_values()
    M = [read_list() for _ in range(N)]
    M.sort(key=lambda l: l[0])
    Q = []

    F = 0
    res = 0
    for x, h in M:
        while Q:
            if Q[0][0] >= x:
                break
            else:
                _, f = heapq.heappop(Q)
                F -= f
        R = max((h - F - 1) // A + 1, 0)
        res += R
        F += R * A
        heapq.heappush(Q, (x + 2 * D, R * A))

    print(res)
       

if __name__ == "__main__":
    main()
