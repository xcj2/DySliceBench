# coding=utf-8

###
### for atcorder program
###

import sys
import math

# math class
class mymath:
    ### pi
    pi = 3.14159265358979323846264338

    ### Prime Number
    def pnum_eratosthenes(self, n):
        ptable = [0 for i in range(n+1)]
        plist = []

        for i in range(2, n+1):
            if ptable[i]==0:
                plist.append(i)
                for j in range(i+i, n+1, i):
                    ptable[j] = 1
        return plist

    ### GCD
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    ### LCM
    def lcm(self, a, b):
        return (a*b)//self.gcd(a,b)

    ### Mat Multiplication
    def mul(self, A, B):
        ans = []
        for a in A:
            c = 0
            for j, row in enumerate(a):
                c += row*B[j]
            ans.append(c)
        return ans

mymath = mymath()

### output class
class output:
    ### list
    def list(self, l):
        l = list(l)
        #print(" ", end="")
        for i, num in enumerate(l):
            print(num, end="")
            if i != len(l)-1:
                print(" ", end="")
        print()

output = output()

### input sample
#i = input()
#N = int(input())
#A, B, C = [x for x in input().split()]
#N, K = [int(x) for x in input().split()]
#inlist = [int(w) for w in input().split()]

#R = float(input())
#A.append(list(map(int,input().split())))

#for line in sys.stdin.readlines():
#    x, y = [int(temp) for temp in line.split()]

#abc list
#abc = [chr(ord('a') + i) for i in range(26)]

### output sample
#print("{0} {1} {2:.5f}".format(A//B, A%B, A/B))
#print("{0:.6f} {1:.6f}".format(R*R*math.pi,R*2*math.pi))
#print(" {}".format(i), end="")

# リスト内包表記 ifあり
# [x-k if x != 0 else x for x in C]

# ソート
# N = N.sort()

# 10000個の素数リスト
# P = mymath.pnum_eratosthenes(105000)

def get_input():
    N = []
    while True:
        try:
            N.append(input())
            #N.append(int(input()))
            #N.append(float(input()))
        except EOFError:
            break
    return N

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def dist(A, B):
    d = 0
    for i in range(len(A)):
        d += (A[i]-B[i])**2            
    d = d**(1/2)
    return d


N = int(input())
A = [int(x) for x in input().split()]

#print(list(range(N-1, 0, -1)))

def printA(A):
    for i, n in enumerate(A):
        print(n, end='')
        if i != N-1:
            print(' ', end='')
    print()

printA(A)

count = 0
for i in range(1, N):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
        A[j+1] = A[j]
        j -= 1
        #printA(A)
    A[j+1] = v
    printA(A)
    #print(A)

