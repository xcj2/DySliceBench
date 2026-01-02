import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

n,k = readints()
a = readints()

mod = 10**9+7

ans = 1
if n==k:
    for x in a:
        ans *= x
        ans %= mod
else:
    plus = []
    minus = []
    for x in a:
        if x>=0:
            plus.append(x)
        elif x<0:
            minus.append(x)
    if len(minus)==n and k%2==1:
        minus.sort(reverse=1)
        for i in range(k):
            ans*=minus[i]
            ans %= mod
    else:
        plus.sort(reverse=1)
        minus.sort()
        i = 0
        j = 0
        if k%2==1:
            ans *= plus[0]
            i+=1
            k-=1
        lp = len(plus)
        lm = len(minus)
        while k>0:
            if i+1<lp and j+1<lm:
                if plus[i]*plus[i+1] > minus[j]*minus[j+1]:
                    ans *= plus[i]*plus[i+1]
                    i+=2
                else:
                    ans *= minus[j]*minus[j+1]
                    j+=2
            elif i+1<lp:
                ans *= plus[i]*plus[i+1]
                i+=2
            else:
                ans *= minus[j]*minus[j+1]
                j+=2
            ans %= mod
            k-=2
print(ans)



        









