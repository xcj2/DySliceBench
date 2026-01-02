import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


N = readint()
S = readstr()
Q = readint()
K = readints()

if 'D' not in S:
    printrows([0]*Q)
    exit()
d = S.find('D')
e = S.rfind('D')
ans = []
for k in K:
    m = 0
    c = 0
    a = 0
    for i in range(d+1,min(N,d+k)):
        if S[i]=='M':
            m += 1
        if S[i]=='C':
            c += 1
            a += m
    b = a
    for i in range(d+1,N):
        if i+k-1<N:
            if S[i+k-1]=='M':
                m += 1
            elif S[i+k-1]=='C':
                c += 1
                a += m
        if S[i-1]=='M':
            m -= 1
            a -= c
        elif S[i-1]=='C':
            c -= 1
        if S[i]=='D':
            b += a
            if i==e:
                break
    ans.append(b)
printrows(ans)


