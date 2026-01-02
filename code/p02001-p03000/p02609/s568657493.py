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
x = readstr()

a = int(x,2)

bit = x.count('1')

z = [0]*(n+1)
for i in range(1,n+1):
    b = i
    while b>0:
        c = 0
        for j in range(b.bit_length()):
            if b&(1<<j):
                c += 1
        b%=c
        z[i]+=1

if bit!=1:
    p = a%(bit-1)
q = a%(bit+1)

ans = [1]*n
for i in range(n):
    if x[i]=='1':
        if bit==1:
            b = 0
            ans[i]-=1
        else:
            b = p-pow(2,n-i-1,bit-1)+bit-1
            b%=bit-1
    else:
        b = q+pow(2,n-i-1,bit+1)
        b%=bit+1
    ans[i]+=z[b]

printrows(ans)



