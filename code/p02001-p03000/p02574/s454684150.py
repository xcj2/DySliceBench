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

def eratosthenes(n):
    a = [1]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if a[i]:
            for j in range(i*i,n+1,i):
                a[j]=0
    return [i for i in range(2,n+1) if a[i]]

flag = 0
ans = ['pairwise coprime', 'setwise coprime', 'not coprime']

n = readint()
a = readints()

prime = eratosthenes(10**6)

check = {x:0 for x in prime}

for x in a:
    for y in set(trial_division(x)):
        check[y] += 1

m = max(check.values())
if m==n:
    flag = 2
elif m>1:
    flag = 1
print(ans[flag])
        

