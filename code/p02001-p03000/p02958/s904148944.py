def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
P = iil()
P_sorted = sorted(P)

indexes = []
count = 0

for i in range(n):
    if P[i] != P_sorted[i]:
        indexes.append(i)
        count += 1

if count == 0:
    print('YES')
elif count != 2:
    print('NO')
else:
    tmp = P[indexes[0]]
    P[indexes[0]] = P[indexes[1]]
    P[indexes[1]] = tmp
#    for j in range(n):
        #if P[j] != P_sorted[j]:
    if P != P_sorted:
        print('NO')
        exit()
    print('YES')