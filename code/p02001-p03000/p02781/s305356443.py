import math
import fractions

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def ValueToBits(x,digit):
    res = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        res[i]=now%2
        now = now >> 1
    return res

def BitsToValue(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans+= arr[i] * 2**i
    return ans

def ValueToArray10(x, digit):
    ans = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        ans[digit-i-1] = now%10
        now = now //10
    return ans

#a = list(map(int, input().split()))

n = int(input())
k = int(input())

arr = ValueToArray10(n,100)
nonzero = [0 for i in range(101)]


for i in range(100):
    if(arr[i]!=0):
        nonzero[i+1] = nonzero[i]+1
    else:
        nonzero[i+1] = nonzero[i]
        
#print(arr,nonzero)

ans = 0

def c2(n):
    if(n<=1):
        return 0
    else:
        return n*(n-1)//2

def c3(n):
    if(n<=2):
        return 0
    else:
        return n*(n-1)*(n-2)//6

if(nonzero[100]==k):
    ans += 1

for ii in range(100):

    i = 99 - ii
    #print(ii,ans,arr[i])
    if(nonzero[i]>=k+1):
        continue
    else:
        if(arr[i]==0):
            continue
        else:
            rem = ii
            if(nonzero[i]==k):
                ans += 1
            elif(nonzero[i] == k-1):
                ans +=  rem * 9 + (arr[i]-1)
            elif(nonzero[i] == k-2):
                ans +=  c2(rem) * 81 + (arr[i]-1) * rem * 9
            elif(nonzero[i] == k-3):
                ans += c3(rem) * 729 + (arr[i]-1) * c2(rem) * 81
            

print(ans)



























