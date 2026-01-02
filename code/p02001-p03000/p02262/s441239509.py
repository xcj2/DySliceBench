def insertionSort(a, n, g):
    global cnt
    for i in range(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j = j - g
            cnt += 1
        a[j + g] = v

def shellSort(a, n):
    global cnt
    g = []
    h = 1
    for i in range(21):
        if h > n:    break
        g.append(h)
        h = h*3 + 1
    m = len(g)
    print(m)
    new_list = list(reversed(g))
    printArray(new_list)
    for i in range(len(g)-1, -1, -1):
        insertionSort(a, n, g[i])
    print(cnt)
    for i in range(len(a)):
        print(a[i])



#配列の出力
def printArray(array):
    print(' '.join(map(str, array)))

###----------mainここから---------------

#配列の要素数と要素の入力(複数行)
n = int(input())
a = [int(input()) for i in range(n)]
cnt = 0
shellSort(a, n)
