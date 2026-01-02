#!/usr/bin/env python3


def valid(honest, a):
    n = len(honest)
    for i in range(n):
        if honest[i]:
            for idx, is_honest in a[i]:
                if honest[idx] != is_honest:
                    return False
    return True

def count_bit(n):
    ret = 0
    while n > 0:
        if n % 2:
            ret += 1
        n //= 2
    return ret

def solve(n, a):
    ret = 0
    for status in range(1 << n):
        honest = [0] * n
        for j in range(n):
            if (1 << j) & status:
                honest[j] = 1
        if valid(honest, a):
            ret = max(ret, count_bit(status))
    print(ret)
    return ret

def main():
    N = int(input())
    a = [[] for _ in range(N)]
    for i in range(N):
        A = int(input())
        for _ in range(A):
            x, y = map(int, input().split())
            a[i].append((x - 1, y))
    solve(N, a)

if __name__ == '__main__':
    main()
