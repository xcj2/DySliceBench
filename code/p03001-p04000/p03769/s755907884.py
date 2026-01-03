import math
import fractions
#import sys
#input = sys.stdin.readline

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

def ZipArray(a):
    aa = [[a[i],i]for i in range(n)]

    aa.sort(key = lambda x : x[0])
    for i in range(n):
        aa[i][0]=i+1
    aa.sort(key = lambda x : x[1])
    b=[aa[i][0] for i in range(len(a))]
    return b

def ValueToArray10(x, digit):
    ans = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        ans[digit-i-1] = now%10
        now = now //10
    return ans

def Zeros(a,b):
    if(b<=-1):
        return [0 for i in range(a)]
    else:
        return [[0 for i in range(b)] for i in range(a)]

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
            
'''
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10**9 + 7
N = 10 ** 6 + 2
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

'''

#a = list(map(int, input().split()))

#################################################
#################################################
#################################################
#################################################



#11:00


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10**9 + 7
N = 10 ** 4 + 2
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


L = 25
cmb2 = [0 for i in range(L+1)]

for i in range(L+1):
    for j in range(1,i+1):
        cmb2[i] += cmb(i,j,p) * cmb(i,j,p)

#print(cmb2)

cmb3 = Zeros(L+1,L+1)

for i in range(L+1):
    for j in range(L+1):
        for k in range(1,min(i,j)+1):
            cmb3[i][j] += cmb(i,k,p) * cmb(j,k,p)

element = []

#print(element)

for i in range(1,L+1):
    for j in range(1,L+1):
        for k in range(1,L+1):
            for l in range(1,L+1):
                element.append([ cmb3[i][k]*cmb3[j][l] + 2**((i+k)-1) + 2**((j+l)-1) - 2, i,j,k,l])

for i in range(1,L):
    element.append([2**(i-1)-1, -1, i,0,0])
element.sort(key = lambda x : x[0], reverse=True)
#print(element[len(element)-500:])



n = int(input())

ans = []
used = 0

while(True):
    if(n==0):
        print(len(ans))
        print(" ".join(map(str,ans)))
        break
    now = []
    for i in element:
        if(i[0]<=n):
            now = i
            break
    if(now[1]==-1):
        used += 1
        for j in range(now[2]):
            ans.append(used)
    else:
        used+=2
        for j in range(now[1]):
            ans.append(used-1)
        for j in range(now[2]):
            ans.append(used)
        for j in range(now[3]):
            ans.append(used-1)
        for j in range(now[4]):
            ans.append(used)
    n -= now[0]















