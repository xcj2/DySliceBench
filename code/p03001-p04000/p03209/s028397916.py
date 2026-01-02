#!/usr/bin/env python3

N, X = map(int, input().split())

def get_a(n):
    if n == 0:
        return 1
    else:
        return get_a(n - 1) * 2 + 3

def get_p(n):
    if n == 0:
        return 1
    else:
        return get_p(n - 1) * 2 + 1

def solver(n, x):
    a = get_a(n)
    p = get_p(n)
    if x >= a:
        ans = p
    elif x == 0:
        ans = 0
    elif 1 <= x < (1 + a) // 2:
        ans = solver(n - 1, x - 1)
    elif x == (1 + a) // 2:
        ans = get_p(n - 1) + 1
    elif (1 + a) // 2 < x < a:
        ans = solver(n - 1, x - get_a(n - 1) - 2) + get_p(n - 1) + 1

    return ans

def main():
    print(solver(N, X))

if __name__ == "__main__":
    main()