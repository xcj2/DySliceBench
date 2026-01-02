def main():
    N = int(input())
    CARD = tuple(input().split())

    sort_ = []
    for i in range(1, 10):
        for s in CARD:
            if str(i) in s:
                sort_.append(s)

    sort_ = tuple(sort_)
    bsort = tuple(bubbleSort(list(CARD), N))
    ssort = tuple(selectionSort(list(CARD), N))

    for s in (bsort, ssort):
        print(*s, sep=' ')
        if s == sort_:
            print('Stable')
        else:
            print('Not stable')

def bubbleSort(c, n):
    flag = 1
    while flag:
        flag = 0
        for i in range(1, n):
            if c[i][1] < c[i-1][1]:
                c[i], c[i-1] = c[i-1], c[i]
                flag = 1
    return c

def selectionSort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if c[j][1] < c[minj][1]:
                minj = j
        c[i], c[minj] = c[minj], c[i]
    return c

main()