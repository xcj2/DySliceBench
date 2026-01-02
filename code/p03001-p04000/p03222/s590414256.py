c = [1, 2, 3, 5, 8, 13, 21, 34, 55]

def count(n):
    if n < 0:
        return 1
    else:
        return c[n]
    
h, w, k = [int(i) for i in input().split(" ")]

p = [[0 for i in range(0, w)] for j in range(0, h + 1)]
p[0][0] = 1

def ul(i, j):
    if j == 0:
        return 0
    else:
        return count(j - 2) * count(w - j - 2) * p[i - 1][j - 1]

def uu(i, j):
    return count(j - 1) * count(w - j - 2) * p[i - 1][j]

def ur(i, j):
    if j == w - 1:
        return 0
    else:
        return count(j - 1) * count(w - j - 3) * p[i - 1][j + 1]

for i in range(1, h + 1):
    for j in range(0, w):
        p[i][j] = ul(i, j) + uu(i, j) + ur(i, j)
    
print(p[-1][k - 1] % 1000000007)