# coding=utf-8

###
### for atcorder program
###

import sys
import math
import array

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
#A = [int(x) for x in input().split()]
#for line in sys.stdin.readlines():
#    x, y = [int(temp) for temp in line.split()]

### output sample
#print("{0} {1} {2:.5f}".format(A//B, A%B, A/B))
#print("{0:.6f} {1:.6f}".format(R*R*math.pi,R*2*math.pi))
#print(" {}".format(i), end="")

def main():
    A,B,C,D = [int(x) for x in input().split()]

    E = mymath.lcm(C,D)

    Ct = 1
    if A == (A//C)*C:
        Ct = 0

    Cd = 1
    #if B == (B//C)*C:
    #   Cd = 0

    Dt = 1
    if A == (A//D)*D:
        Dt = 0

    Dd = 1
    #if B == (B//D)*D:
    #    Dd = 0

    Et = 1
    if A == (A//E)*E:
        Et = 0

    Ed = 1
    #if B == (B//E)*E:
    #   Ed = 0

    Cwa = (B//C+Cd - (A//C+Ct))
    Dwa = (B//D+Dd - (A//D+Dt))
    CDw = (B//E+Ed - (A//E+Et))
    zen = B - A + 1

    print(zen + CDw - Cwa - Dwa)

    #print(zen - len(list(range(A, B+1))))

    #print(list(x*C for x in range(A//C+Ct, B//C+Cd)))
    #print(list(x*D for x in range(A//D+Dt, B//D+Dd)))
    #print(list(x*E for x in range(A//E+Et, B//E+Ed)))
    #print(list(range(A, B+1)))
    #Dlist  = set(x*D for x in range(A//D, B//D+1))
    #ABlist = set(x for x in range(A,B+1))
    
    #print(len(Clist))

    #print(Clist)
    #print(Dlist)
    #print(Clist | Dlist)
    #print(ABlist)

    #anslist = ABlist - Clist

    #print(anslist)

    #count = len(anslist)
 

if __name__ == '__main__':
    main()

