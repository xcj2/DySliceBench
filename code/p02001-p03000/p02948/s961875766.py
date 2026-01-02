import sys
import heapq


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    tasks = list(map(tuple, zip(A, B)))
    tasks.sort()
    tasks.reverse()

    earnables = []

    ans = 0
    for i in range(M + 1):
        while len(tasks) > 0 and tasks[-1][0] <= i:
            _, pay = tasks.pop()
            heapq.heappush(earnables, -pay)
        if len(earnables) > 0:
            ans += -heapq.heappop(earnables)

    return ans


# -----------------------------------------------------------------------------
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()

    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))

    ans = solve(N, M, A, B)
    if ans is not None:
        print(ans)


if __name__ == '__main__':
    main()
