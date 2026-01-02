def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r + 1):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def makedic(A, n):
    d = {}
    for i in range(n):
        key = A[i][1]
        value = A[i][0]
        if key in d:
            d[key] += value
        else:
            d[key] = value
    return d

def main():
    N = int(input())
    A = []
    for i in range(N):
        a, v = input().split()
        v = int(v)
        A.append((a, v))

    sd = makedic(A, N)
    quicksort(A, 0, N - 1)
    ed = makedic(A, N)

    print('Stable' if sd == ed else 'Not stable')

    for l in A:
        print(l[0], l[1])

if __name__ == '__main__':
    main()




