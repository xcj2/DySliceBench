def calcGaps(n):
    gaps = [1]
    while 3 * gaps[-1] + 1 < n:
        gaps.append(3 * gaps[-1] + 1)
    return gaps[::-1]


def insertionSort(a, n, gap, cnt):
    for i in range(gap, n):
        v = a[i]
        j = i - gap
        while j >= 0 and a[j] > v:
            a[j + gap] = a[j]
            j = j - gap
            cnt += 1
        a[j + gap] = v
    return a, cnt


def shellSort(a, n):
    cnt = 0
    Gaps = calcGaps(n)
    for gap in Gaps:
        a, cnt = insertionSort(a, n, gap, cnt)
    print(len(Gaps))
    print(*Gaps)
    print(cnt)
    print(*a, sep='\n')


n = int(input())
A = [int(input()) for _ in range(n)]

shellSort(A, n)
