# 1, 2, 3, 5

from itertools import chain
from math import ceil

# def factorization(n):
#     tmp = n
#     arr = []
#     for i in range(2, ceil(n ** (1/2)) + 1):
#         m, r = divmod(tmp, i)
#         print(f'm: {m}, r: {r}')
#         count = 0 if r == 0 else 1
#         while r == 0:
#             m, r  = divmod(tmp, i)
#             if r == 0:
#                 tmp = m
#                 count += 1


#         if count != 0:
#             arr.append((i, count))

#     return arr

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

def get_prime_facts(n):
    return set(map(lambda x: x[0], factorization(n)))

def solution(A, B):
    s = get_prime_facts(A) & get_prime_facts(B) | {1}

    return len(s)

if __name__ == '__main__': 
    A, B = map(int, input().split())
    a = solution(A, B)

    print(a)
