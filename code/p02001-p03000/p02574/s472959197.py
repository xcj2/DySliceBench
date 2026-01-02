# import sys
# input = sys.stdin.readline

def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))
import math
from functools import reduce

def gcd(numbers):
    return reduce(math.gcd, numbers)
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

n = int(input())
a = lmp()
agcd = gcd(a)
used = set()
flag = True
for i in range(n):
    tar = a[i]
    if tar == 1:
        pass
    else:
        f = factorization(tar)
        for j in range(len(f)):
            if f[j][0] not in used:
                used.add(f[j][0])
            else:
                flag = False
                break
        if not flag:
            break
if flag:
    print("pairwise coprime")
elif agcd == 1:
    print("setwise coprime")
else:
    print("not coprime")



