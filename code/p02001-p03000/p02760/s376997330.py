def hasTri(arrs):
    k = [arrs[0][0], arrs[1][1], arrs[2][2]]
    l = [arrs[0][2], arrs[1][1], arrs[2][0]]
    if not False in k:
        return True
    if not False in l:
        return True
    return False
def hascol(arrs):
    for i in range(3):
        k = [arrs[0][i], arrs[1][i], arrs[2][i]]
        if not False in k:
            return True
    return False
def hasrow(arrs):
    for i in arrs:
        arr = [x for x in i if x != False]
        if len(arr)==3:
            return True
    return False
A = [[0,0,0],[0,0,0],[0,0,0]]
B = [[False,False,False],[False,False,False],[False,False,False]]
for i in range(3):
    A[i][0],A[i][1],A[i][2] = map(int, input().split())
N = int(input())
Al = [i for x in A for i in x]
have = []
for _ in range(N):
    a = int(input())
    if a in Al:
        have.append(a)
indexs = [[]]
for k in have:
    index = [[ix,iy] for ix, row in enumerate(A) for iy, j in enumerate(row) if j == k]
    if len(index[0]) == 2:
        indexs = indexs + index
        B[index[0][0]][index[0][1]] = k
if hasTri(B) or hasrow(B ) or hascol(B):
    print("Yes")
else:
    print("No")



