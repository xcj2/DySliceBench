import sys

# Set max recursion limit
sys.setrecursionlimit(1000000)


def li_input():
    return [int(_) for _ in input().split()]


def is_exist(A, x):
    l = 0
    r = len(A) - 1

    while l <= r:
        m = (l + r) // 2
        if A[m] == x:
            return True
        
        if A[m] < x:
            l = m + 1
        else:
            r = m - 1

    return False
            


def main():
    n = int(input())
    S = li_input()
    q = int(input())
    T = li_input()

    ans = 0

    for t in T:
        if is_exist(S, t):
            ans += 1

    print(ans)


main()

