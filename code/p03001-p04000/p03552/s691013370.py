#  --*-coding:utf-8-*--

def f(N, Z, W, A):
    A.insert(0, W)

    lastA = A[-1]
    sc = abs(lastA - A[-2])
    minOfX = sc
    maxOfY = sc
    scX = sc

    for i in range(N-1, 0, -1):
        sc = abs(lastA - A[i-1])

        scX = max(sc, maxOfY)
        scY = min(sc, minOfX)

        minOfX = min(minOfX, scX)
        maxOfY = max(maxOfY, scY)

    return scX
            

def test():
    assert f(3, 100, 100, [10, 1000, 100]) == 900
    assert f(3, 100, 1000, [10, 100, 100]) == 900
    assert f(5, 1, 1, [1, 1, 1, 1, 1]) == 0
    assert f(1, 1, 1, [1000000000]) == 999999999


def main():
    N,Z,W = map(int, input().split())
    A = list(map(int, input().split()))

    print(f(N,Z,W,A))


if __name__ == '__main__':
    main()
