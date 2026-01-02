import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

a = [readints() for i in range(3)]
n = readint()

for i in range(n):
    b = readint()
    for j in range(3):
        for k in range(3):
            if a[j][k]==b:
                a[j][k]=0
ans = 0
for i in range(3):
    if a[i][0]==a[i][1]==a[i][2]==0:
        ans = 1
        break
    if a[0][i]==a[1][i]==a[2][i]==0:
        ans = 1
        break
if a[0][0]==a[1][1]==a[2][2]:
    ans = 1
if a[0][2]==a[1][1]==a[2][0]:
    ans = 1
print('Yes'if ans else 'No')