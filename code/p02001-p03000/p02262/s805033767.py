def insertionSort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return cnt, A

def shellSort(A, n):
    cnt = 0
    g = [1]
    while g[-1] * 3 + 1 < n:
        g.append(g[-1] * 3 + 1)
    g.reverse()
    print(len(g))
    print(' '.join([str(_g) for _g in g]))
    for i in range(len(g)):
        cnt, A = insertionSort(A, n, g[i], cnt)
    return cnt, A

def run():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(int(input()))
    cnt, ans = shellSort(A, n)
    print(cnt)
    print('\n'.join([str(a) for a in ans]))

if __name__ == '__main__':
    run()


