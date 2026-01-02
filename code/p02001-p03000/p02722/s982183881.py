import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
def getlist2():
    return [int(x) * 100000 for x in input().split()]
import math
import bisect
import heapq
from decimal import Decimal
# from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15

def factorization2(n):
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

# factorization(24)

## [[2, 3], [3, 1]]
##  24 = 2^3 * 3^1

def factorization(n):
    ret = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret.append(i)
            ret.append(n // i)
    ret.append(n)
    return ret

def simulation(n, k):
    while(n >= k):
        if n % k == 0:
            n = n // k
        else:
            n -= k

    if n == 1:
        return True
    else:
        return False
def simulation_answer(n):
    ans = 0
    for i in range(2, n+1):
        if simulation(n, i):
            # print(i)
            ans += 1
    return ans

def submit_answer(n):
    # fcminus = factorization(n - 1)
    ans1 = factorization(n-1)
    # for a, b in fcminus:
    #     ans1 *= (b + 1)

    fc = factorization(n)
    ans2 = 0
    for fact in fc:
        tmp = n
        while (tmp % fact == 0):
            tmp /= fact
        if tmp % fact == 1:
            ans1.append(fact)
        # for power in range(1, b+1):
        #     wari = a**power
        #     while(tmp % wari == 0):
        #         tmp /= wari
        #     # if (n // (a ** power)) == (a ** power) + 1:
        #     if tmp % wari == 1:
        #         ans2 += 1
        #         print(a ** power)

    # print(ans2)
    # for i in range(2, n + 1):
    #     if simulation(n, i):
    #         print(i)
    # return (ans1 + ans2)
    # print(list(set(ans1)))
    return(len(list(set(ans1))))

def main():
    # n = getN()
    # print(factorization(n))
    # print(simulation_answer(n))
    # print(submit_answer(n))
    # for i in range(2, 100000):
    #     if simulation_answer(i) == submit_answer(i):
    #         status = "OK"
    #     else:
    #         status = "NG"
    #
    #         print("{}:  {}".format(i, status))
    #         print("simu: ", simulation_answer(i))
    #         print("sub: ", submit_answer(i))
    n = getN()
    if n == 2:
        print(1)
        return
    else:
        print(submit_answer(n))
        return

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""