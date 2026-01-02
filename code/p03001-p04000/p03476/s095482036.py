def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

import bisect
import sys
input = sys.stdin.readline

Q=one_int()

import math
lim = int(math.pow(10, 5))
is_prime = [True for _ in range(lim+1)]
is_prime[0], is_prime[1] = False, False
for i in range(2, int(math.sqrt(lim))+1):
    if is_prime[i]:
        for j in range(i*2, lim+1, i):
            is_prime[j] = False
 

# sosu_dict = {s:0 for s in sosuu_list}

like_list = [0 for i in range(10**5 + 1)]
count=0
for i in range(10**5):
    if (is_prime[(i+1)//2]) and (is_prime[i]):
        count+=1
    like_list[i] = count

for i in range(Q):
    l,r = many_int()
    print(like_list[r]-like_list[l-1])