def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

A = []
B = [[False for i in range(3)] for j in range(3)]
l = []
for i in range(3):
    A.append(iil())
    for item in A[i]:
        l.append(item)


n = ii()
for i in range(n):
    call = ii()
    if call in l:
        p = l.index(call)
        B[p//3][p%3] = True

if B[0][0]*B[0][1]*B[0][2] == 1:
    print('Yes')
elif B[1][0]*B[1][1]*B[1][2] == 1:
    print('Yes')
elif B[2][0]*B[2][1]*B[2][2] == 1:
    print('Yes')
elif B[0][0]*B[1][1]*B[2][2] == 1:
    print('Yes')
elif B[0][2]*B[1][1]*B[2][0] == 1:
    print('Yes')
elif B[0][0]*B[1][0]*B[2][0] == 1:
    print('Yes')
elif B[0][1]*B[1][1]*B[2][1] == 1:
    print('Yes')
elif B[0][2]*B[1][2]*B[2][2] == 1:
    print('Yes')
else:
    print('No')