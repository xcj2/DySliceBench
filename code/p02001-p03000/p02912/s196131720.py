def solve(N, M, A):
    from math import log, ceil
    from heapq import heappush, heappop, heapify
    Q = [-a for a in A]
    heapify(Q)

    if len(A) == 1:
        return A[0]>>M

    while Q and M:
        a = - heappop(Q)
        b = - Q[0]
        if a == 0:
            continue
        if b == 0:
            k = M
        elif b < a:
            k = min(M, ceil(log(a,2) - log(b, 2)))
        else:
            k = min(M, 1)
        c = a >> k
        #print("prev=%d, dis=%d, %d - %d = %d" % (a, c, M, k, M-k))
        M -= k
        heappush(Q, -c)
    return sum(-a for a in Q)


def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = sorted([int(x) for x in input().split()], reverse=True)

    print(solve(N, M, A))

def gen():
    import random
    with open("9", "w") as f:
        print(10**5, 10**5, file=f)
        print(*[random.randint(1, 10**9) for i in range(10**5)],file=f)

main()

