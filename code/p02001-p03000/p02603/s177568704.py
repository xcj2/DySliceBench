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
a = readints()


money = 1000
kabu = 0
for i in range(n-1):
    if a[i]<a[i+1]:
        b = money//a[i]
        kabu += b
        money -= b*a[i]
    else:
        money += kabu*a[i]
        kabu = 0

print(money + kabu*a[-1])


