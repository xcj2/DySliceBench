import sys
import math
def input():
    return sys.stdin.readline()[:-1]

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def trial_division(n):
    factor = []
    tmp = int(math.sqrt(n)) + 1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    if n!=1:
        factor.append(n)
    return factor

n,m=map(int,input().split())
mod=10**9+7
if m==1:
    print(1)
    quit()
li=trial_division(m)
tmp=li[0]
countli=[]
count=1
for i in range(1,len(li)):
    if tmp!=li[i]:
        countli.append(count)
        count=1
    else:
        count+=1
    tmp=li[i]
countli.append(count)
ans=1
for i in range(len(countli)):
    ans*=combinations_count(countli[i]+n-1,countli[i])
print(ans%mod)