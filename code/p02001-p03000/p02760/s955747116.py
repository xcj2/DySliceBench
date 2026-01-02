from collections import Counter

def row(M, li):
    ## solve for row
    for i in range(3):
        bad = False
        r = Mat[i]
        c = Counter(r)
        for k,v in c.items():
            if li.get(k, 0) < v:
                bad = True
        if not bad:
            return True

    return False

def col(M, li):
    for Col in zip(*M):
        bad = False
        c = Counter(Col)
        for k, v in c.items():
            if li.get(k, 0) < v:
                bad = True

        if not bad:
            return True

    return False

def r_diag(M, li):
    it = []
    for i in range(3):
        it.append(M[i][i])
    c = Counter(it)
    for k,v in c.items():
        if li.get(k, 0) < v:
            return False

    return True

def l_diag(M, li):
    it = []
    for i in range(3):
        it.append(M[i][3-i-1])
    c = Counter(it)
    for k,v in c.items():
        if li.get(k, 0) < v:
            return False

    return True

def solve(M ,li):
    if row(M, li) or col(M, li) or r_diag(M, li) or l_diag(M, li):
        return "Yes"

    return "No"
Mat = []
for i in range(3):
    li = list(map(int, input().split()))
    Mat.append(li)

n = int(input())
li = {}
for i in range(n):
    a = int(input())
    li[a] = li.get(a, 0) + 1

print(solve(Mat, li))
