import numpy as np

def ii():
    return int(input())


def lii():
    return list(map(int, input().split(' ')))


def lvi(N):
    l = []
    for _ in range(N):
        l.append(ii())
    return l


def lv(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def main():
    N = ii()
    A = []
    for _ in range(N):
        a = ii()
        A.append(a)

    ans = 0
    if A[0] != 0:
        return -1

    for i in range(1, N):
        diff = A[i] - A[i-1]
        if diff == 1:
            pass
        elif diff == 0:
            ans += A[i-1]
        elif diff > 1:
            return -1
        else:
            ans += A[i-1]

    ans += A[-1]

    return ans

if __name__ == '__main__':
    print(main())