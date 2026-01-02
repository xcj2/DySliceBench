import math

def sizeN(n):
    count = 1
    for i in range(n):
        count = count*2 + 3
    return count


def countP(n):
    if n < 0:
        return 0
    count = 1
    for i in range(n):
        count = count*2 + 1
    return count


def sharpen(x):
    return x - 1


def answer(N, X):
    count_p = 0
    x = X
    for n in range(N,-1,-1):
        if x < math.ceil(sizeN(n)/2):
            x = sharpen(x)
        else:
            x = sharpen(x - math.floor(sizeN(n)/2))
            count_p += countP(n-1)+1
    return count_p


if __name__ == '__main__':

    N, X = map(int, input().split())
    print(answer(N, X))
