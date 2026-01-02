#!/usr/bin/env python3
import sys
import itertools

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


def main():
    N, M, X = lmi()
    CA = llmi(N)

    def get_cost(set_of_bought):
        ans = 0
        for s in set_of_bought:
            ans += CA[s][0]
        return ans

    def check(set_of_bought):
        XX = [0] * M
        for s in set_of_bought:
            for i in range(M):
                XX[i] += CA[s][i + 1]
        if all(v >= X for v in XX):
            return True
        return False
    ans = INF
    for i in range(1 << N):
        cur = set()
        for n in range(N):
            if i>>n & 1:
                cur.add(n)
        # print(cur)

        if check(cur):
            ans = min(ans,get_cost(cur))
    if ans == INF:
        print(-1)
    else:
        print(ans)



if __name__ == '__main__':
    main()
