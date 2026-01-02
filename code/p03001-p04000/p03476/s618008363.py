#素数かどうか

import numpy as np
def list_primes(N):
    is_prime = np.ones(N+1, dtype=np.bool)
    # iが素数ならTrue，素数でないならFalse
    is_prime[0] = False
    is_prime[1] = False
    for i in range(N+1):
        if is_prime[i]:
            is_prime[2*i::i] = False
            # iの倍数の部分をスライスで選択して「素数でない」に設定
    #return is_prime.nonzero()
    return is_prime
    # is_primeがTrueになるもののindexのarray
    
N = 10**5
is_prime = list_primes(N)


#2017ににた数のリストの作成
def solve(is_prime):
    ans = []
    for i in range(len(is_prime)-1):
        if i % 2 == 1:
            if is_prime[i] and is_prime[(i+1)//2]:
                ans.append(i)
    return ans

like2017 = solve(is_prime)



#二分探索
def nibu_right(a,A): #a in A(sorted)
    if a<A[0]:return 0
    elif A[-1]<=a:return len(A)
    else:
        mi = 0
        ma = len(A)-1
        while ma-mi>1:
            mid = (ma+mi)//2
            if a > A[mid]:
                mi = mid
            else:
                ma = mid
        # A[mi]<a  a<=A[ma]
        if A[ma] == a:return ma+1
        else: return ma

def nibu_left(a,A): #a in A(sorted)
    if a<=A[0]:return 0
    elif A[-1]<a:return len(A)
    else:
        mi = 0
        ma = len(A)-1
        while ma-mi>1:
            mid = (ma+mi)//2
            if a < A[mid]:
                ma = mid
            else:
                mi = mid
        # A[mi]<=a  a<A[ma]
        if A[mi] == a:return mi
        else: return mi+1






Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    l_index = nibu_left(l,like2017)
    r_index = nibu_right(r,like2017)
    print(r_index - l_index)