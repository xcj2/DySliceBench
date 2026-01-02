import sys
input = sys.stdin.readline

def x_p(x,y):
    if x == H-1:
        return 0
    x += 1
    return ([x,y] in l)

def x_m(x,y):
    if x == 0:
        return 0
    x -= 1
    return ([x,y] in l)

def y_p(x,y):
    if y == W-1:
        return 0
    y += 1
    return ([x,y] in l)

def y_m(x,y):
    if y == 0:
        return 0
    y -= 1
    return ([x,y] in l)

H,W = [int(i) for i in input().split()]
l = []
for i in range(H):
    A = list(input())
    for j in range(W):
        if A[j] == "#":
            l.append([i,j])

for i in l:
    flag = 0
    x,y = i
    if x_p(x,y) == True or x_m(x,y) == True or y_p(x,y) == True or y_m(x,y) == True:
        flag = 1
    if flag == 0:
        print('No')
        exit()
print('Yes')
