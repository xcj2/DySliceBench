import sys,math
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


def sieve_of_eratosthenes(n):
    prime_list = []  # n以下の素数のリスト
    A = [1]*(n+1)    # A[i] = iが素数なら1,その他は0
    A[0] = A[1] = 0
    for i in range(2,math.floor(math.sqrt(n))+1):
        if A[i]:
            prime_list.append(i)
            for j in range(i**2,n+1,i):
                A[j] = 0
    for i in range(math.floor(math.sqrt(n))+1,n+1):
        if A[i] == 1:
            prime_list.append(i)
    return prime_list,A


prime_list,A = sieve_of_eratosthenes(10**5)

like_2017 = [0]*(10**5+1)
for p in prime_list:
    if p == 2:
        continue
    else:
        if A[(p+1)//2] == 1:
            like_2017[p] = 1

from itertools import accumulate

C = list(accumulate(like_2017))

Q = I()
for i in range(Q):
    l,r = MI()
    print(C[r]-C[l-1])
