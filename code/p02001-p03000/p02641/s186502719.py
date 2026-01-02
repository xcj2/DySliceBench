  
import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))



x,n = readints()
p = readints()

if x not in p:
    print(x)
    exit()
i = 1
while 1:
    if x-i not in p:
        print(x-i)
        exit()
    elif x+i not in p:
        print(x+i)
        exit()
    i+=1

