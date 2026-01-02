import sys
import heapq
from functools import lru_cache


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    n = N // 3

    @lru_cache(maxsize=None)
    def diff(s):
        count = 0
        for i in range(N):
            if A[i] == B[(i + s) % N]:
                count += 1

        if count == 0:
            print("Yes")
            L = []
            for i in range(N):
                L.append(B[(i + s) %N])
            print(*L)
            exit()

        return count

    l = 0
    r = N - 1
    diff(l)
    diff(r)

    while r - l > 2:
        a = diff(l + (r - l) // 3)
        b = diff(l + 2 * (r - l) // 3)
        if a > b:
            l = l + (r - l) // 3
        else:
            r =l + 2 * (r - l) // 3
    diff((l+r)//2)

    print("No")


if __name__ == "__main__":
    main()
