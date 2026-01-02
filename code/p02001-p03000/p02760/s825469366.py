import math
def py():
    print("Yes")
def pn():
    print("No")
def iin():
    x = int(input())
    return x

neko = 0
nya = 0
nuko = 0
a = [] 
x = [[0] * 3 for i in range(3)]
for i in range(3):
    a.append([int(x) for x in input().split()])
n = iin()
b = [0] * n
for i in range(n):
    b[i] = iin()

for i in range(3):
    for j in range(3):
        for f in range(n):
            if a[i][j] == b[f]:
                x[i][j] = 1
for i in range(3):
    if sum(x[i]) == 3:
        neko = neko + 1
    nya = x[0][i] + x[1][i] + x[2][i]
    if nya == 3:
        neko = neko + 1
nya = x[0][0]+ x[1][1] + x[2][2]
if nya == 3:
    neko = neko + 1
nya = x[0][2]+ x[1][1] + x[2][0]
if nya == 3:
    neko = neko + 1
if neko > 0:
    py()
else:
    pn()