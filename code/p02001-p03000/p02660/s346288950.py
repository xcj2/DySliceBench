import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

def trial_division(n):  # n > 1
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def count_primes(n):
    a = trial_division(n)
    b = [[a[0],1]]
    for i in range(1,len(a)):
        if b[-1][0]==a[i]:
            b[-1][1]+=1
        else:
            b.append([a[i],1])
    return b


n = readint()
if n==1:
    print(0)
    exit()

a = count_primes(n)
ans = 0
for i in range(len(a)):
    x,y = a[i]
    b = 1
    while y>0:
        y-=b
        if y>=0:
            ans += 1
            b+=1

print(ans)
