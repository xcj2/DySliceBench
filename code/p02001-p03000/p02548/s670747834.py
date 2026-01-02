# cook your dish here
import sys,math
try:sys.stdin,sys.stdout=open('input.txt','r'),open('out.txt','w')
except:pass
from sys import stdin,stdout;mod=int(1e9 + 7);from statistics import mode
from collections import *;from math import ceil,floor,inf,factorial,gcd,log2,sqrt,log
ii1=lambda:int(stdin.readline().strip())
is1=lambda:stdin.readline().strip()
iia=lambda:list(map(int,stdin.readline().strip().split()))
isa=lambda:stdin.readline().strip().split()
# print('{:.3f}'.format(1),round(1.123456789,4))
# sys.setrecursionlimit(500000)
def lcm(a,b): return (a*b)//gcd(a,b)
def setbits(n):return bin(n).count('1')
def resetbits(n):return bin(n).count('0')
def modinv(n,p):return pow(n,p-2,p)
def ncr(n,r):
    num,den=1,1;r=min(n,n-r)
    for i in range(r):num*=(n-i);den*=(i+1)
    return num//den
def ncr_p(n, r, p):
    num,den=1,1;r=min(r,n-r)
    for i in range(r):num = (num * (n - i)) % p ;den = (den * (i + 1)) % p
    return (num * modinv(den,p)) % p
def isPrime(num) :
    if num<=1:return False
    if num==2 or n==3:return True
    if (num % 2 == 0 or num % 3 == 0) :return False
    m = int(num**0.5)+1
    for i in range(5,m,6):
        if (num % i == 0 or num % (i + 2) == 0) :return False
    return True
def bin_search(s, low, high, val):
    while low <= high:
        mid = low + (high - low) // 2;
        if s[mid] == val:return mid
        elif s[mid] < val:low = mid + 1
        else:high = mid - 1
    return -1
def sumofdigit(num):
    count=0;
    while num : count+=num % 10;num //= 10;
    return count;
def inputmatrix():
    r,c=iia();mat=[0]*r;
    for i in range(r):mat[i]=iia();
    return r,c,mat;
def prefix_sum(n,s):
    for i in range(1,n):s[i]+=s[i-1]
    return s;
def binomial(n, k):
    if 0 <= k <= n:
        ntok = 1;ktok = 1
        for t in range(1, min(k, n - k) + 1):ntok *= n;ktok *= t;n -= 1
        return ntok // ktok
    else:return 0
def divisors(n):
    res = [];
    for i in range(1,ceil(sqrt(n))+1):
        if n%i == 0:
            if i==n//i:res.append(i)
            else:res.append(i);res.append(n//i)
    return res;

# coding start heres
MAX = ii1()
factor = [0]*(MAX + 1);
def primefactor():
    factor[1] = 1;
    for i in range(2,MAX):
        factor[i] = i;
    for i in range(4,MAX,2):
        factor[i] = 2;
    i = 3;
    while(i * i < MAX):
        if (factor[i] == i):
            j = i * i;
            while(j < MAX):
                if (factor[j] == j):
                    factor[j] = i;
                j += i;
        i+=1;
def fun(n):
    if (n == 1):
        return 1;
    ans = 1;
    dup = factor[n];
    c = 1;
    j = int(n / factor[n]);
    while (j > 1):
        if (factor[j] == dup):
            c += 1;
        else:
            dup = factor[j];
            ans = ans * (c + 1);
            c = 1;
        j = int(j / factor[j]);
    ans = ans * (c + 1);
    return ans;

if __name__ == "__main__":
    primefactor()
    sum=0
    for i in range(1,MAX):
        a=fun(i)
        sum+=a
    print(sum)
