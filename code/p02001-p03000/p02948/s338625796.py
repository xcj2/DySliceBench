#  --*-coding:utf-8-*--

import heapq


def g(Q, n):
    x = 0

    for i in range(n):
        if len(Q) == 0:
            break

        x += -heapq.heappop(Q)

    return x


def f(AB, M):
    lastA = None
    Q = []
    sumOfB = 0

    for a,b in AB:
        if a > M:
            break

        if a != lastA:
            if lastA != None:
                sumOfB += g(Q, a-lastA)

            lastA = a

        heapq.heappush(Q, -b)
            
    if lastA != None:
        sumOfB += g(Q, M-lastA+1)

    return sumOfB


def main():
    N,M = map(int, input().split())
    AB = sorted(list(map(int, input().split())) for i in range(N))

    print(f(AB, M))


if __name__ == '__main__':
    main()
