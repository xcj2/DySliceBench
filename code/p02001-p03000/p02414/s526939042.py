def main():
    n, m, l = [int(x) for x in input().split()]

    a = readMatrix(n, m)
    b = readMatrix(m, l)

    printMatrix(multiplyAB(a, b))

def readMatrix(r, c):
    m = []
    for _ in range(r):
        m.append([int(x) for x in input().split()])

    return m

def multiplyAB(a, b):
    n = len(a)
    m = len(b)
    l = len(b[0])

    c = [[0 for _ in range(l)] for _ in range(n)]

    for i in range(n):
        for j in range(l):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]

    return c

def printMatrix(m):
    for r in m:
        print(' '.join([str(x) for x in r]))

if __name__ == '__main__':
    main()

