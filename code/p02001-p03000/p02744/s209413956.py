import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

n = readint()

ans = [[[0],[0]]]

i = 0
while len(ans[i][0])<n:
    a = ans[i]
    for x in a[1]:
        ans.append([a[0]+[x],a[1]])
    x = a[1][-1]+1
    ans.append([a[0]+[x],a[1] + [x]])
    i+=1

a_ = ord('a')

for i in range(len(ans)):
    a = ans[i][0]
    if len(a)<n:
        continue
    for x in a[:-1]:
        print(chr(x+a_),end='')
    print(chr(a[-1]+a_))
    
