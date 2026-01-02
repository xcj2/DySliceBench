import bisect
import heapq
import sys


input = sys.stdin.readline
sys.setrecursionlimit(100000)


class v:
    def __init__(self, f):
        self.f = f
        self.v = None

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def update(S, L, M):
    _, a, b = S
    M[0] += b

    if len(L[0]) == 0:
        L[0].append(-a)
        L[1].append(a)
    else:
        r0 = -1 * L[0][0]
        r1 = L[1][0]
        if a < r0:
            M[1] += r0 - a
        elif r1 < a:
            M[1] += a - r1

        if -1 * L[0][0] >= a:
            heapq.heappush(L[0], -a)
            t = -1 * heapq.heappushpop(L[0], -a)
            heapq.heappush(L[1], t)
        elif L[1][0] < a:
            heapq.heappush(L[1], a)
            t = heapq.heappushpop(L[1], a)
            heapq.heappush(L[0], -t)
        else:
            heapq.heappush(L[0], -a)
            heapq.heappush(L[1], a)
    # print(L, M)


def print_min(L, M):
    print(-1 * L[0][0], sum(M))


def main():
    Q = int(input())

    L = [[], []]
    M = [0, 0]
    for q in range(Q):
        S = read_list()
        if S[0] == 1:
            update(S, L, M)
        else:
            print_min(L, M)


if __name__ == "__main__":
    main()
