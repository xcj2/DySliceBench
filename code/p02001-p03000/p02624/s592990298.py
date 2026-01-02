#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))


INF = float("inf")
MOD = 10**9 + 7

def main():
    n = INT()
    table = [0] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n + 1):
        if table[i] == 0:
            table[i] = 2
            for j in range(i + i, n + 1, i):
                cnt = 0
                c = j
                while c % i == 0:
                    c //= i
                    cnt += 1
                table[j] = table[c] * (cnt + 1)

    # print(table)
    ans = 0
    for i in range(n + 1):
        ans += i * table[i]
    print(ans)

    return


if __name__ == '__main__':
    main()
