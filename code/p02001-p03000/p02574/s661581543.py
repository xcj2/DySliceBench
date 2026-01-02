# Python3 program to find prime factorization 
# of a number n in O(Log n) time with 
# precomputation allowed. 
import math as mt 

MAXN = 1000001

# stores smallest prime factor for 
# every number 


# Calculating SPF (Smallest Prime Factor) 
# for every number till MAXN. 
# Time Complexity : O(nloglogn) 
def sieve(): 
    spf = [0 for i in range(MAXN)] 
    spf[1] = 1
    for i in range(2, MAXN): 
		
		# marking smallest prime factor 
		# for every number to be itself. 
        spf[i] = i 

	# separately marking spf for 
	# every even number as 2 
    for i in range(4, MAXN, 2): 
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
		
		# checking if i is prime 
        if (spf[i] == i): 
			
			# marking SPF for all numbers 
			# divisible by i 
            for j in range(i * i, MAXN, i): 
				
				# marking spf[j] if it is 
				# not previously marked 
                if (spf[j] == j): 
                    spf[j] = i 
    return spf

# A O(log n) function returning prime 
# factorization by dividing by smallest 
# prime factor at every step 
def getFactorization(x,spf): 
	ret = set()
	while (x != 1): 
		ret.add(spf[x]) 
		x = x // spf[x] 

	return ret 

# # Driver code 

# # precalculating Smallest Prime Factor 
# sieve() 
# x = 12246
# print("prime factorization for", x, ": ", 
# 								end = "") 

# # calling getFactorization function 
# p = getFactorization(x) 

# for i in range(len(p)): 
# 	print(p[i], end = " ") 

# This code is contributed 
# by Mohit kumar 29 


def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor,gcd
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10

    N = II()
    A = LMIIS()
    # from random import random
    # N = int(random()*10**6)
    # A = []
    # for i in range(N):
    #     A.append(1+int(random()*10**6))

    spf = sieve()
    primes = set()
    PairWise = True
    for a in A:
        p = getFactorization(a,spf)
        if len(p & primes) > 0:
            PairWise = False
            break
        primes |= p
    else:
        print('pairwise coprime')
        return

    all_gcd = A[0]
    for a in A:
        all_gcd = gcd(all_gcd,a)
        if all_gcd == 1:
            print('setwise coprime')
            return
    print('not coprime')

    


    
main()