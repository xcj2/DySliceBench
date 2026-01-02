# coding: utf-8
import math
import bisect
# 素数判定関数
def isPrime(num):
    # 2未満の数字は素数ではない
    if num < 2: return False
    # 2は素数
    elif num == 2: return True
    # 偶数は素数ではない
    elif num % 2 == 0: return False

    # 3 ~ numまでループし、途中で割り切れる数があるか検索
    # 途中で割り切れる場合は素数ではない
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False

    # 素数
    return True

def isOK(index,key):
    if l[index] <= key:
        return True
    else:
        return False

def binary_search(key):
    left=len(l)-1
    right=-1
    
    while abs(right - left) >1:
        mid=(right+left)//2
        
        if isOK:
            right=mid
        else:
            left=mid
    return right

# 素数判定
def callIsPrime(input_num=1000):
    numbers = []
    # ループしながら素数を検索する
    for i in range(1, input_num):
        if isPrime(i):
            numbers.append(i)

    # 素数配列を返す
    return numbers

primes=callIsPrime(10**5)
l=[]

for i in range(len(primes)):
    if (primes[i]+1)//2 in primes:
        l.append(primes[i])
        
Q=int(input())
for i in range(Q):
    L,R=map(int,input().split())
    L=bisect.bisect_left(l,L)
    R=bisect.bisect_right(l,R)
    
    print(R-L)
    
    


    

