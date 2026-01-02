
import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

k = readint()
flag = 1
if k%2==0 or k%5==0:
    flag = 0

if flag:
    a = 7
    a %= k
    i = 1
    while 1:
        if a%k==0:
            print(i)
            exit()
        else:
            a+=7*pow(10,i,k)
            a%=k
            i+=1
else:
    print(-1)

