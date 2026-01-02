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

a = ord('a')-1
ans = []
i = 1
while n:
    if n%26==0:
        ans.append('z')
        n = n//26-1
    else:
        ans.append(chr(n%26+a))
        n//=26

ans.reverse()
print(''.join(ans))
