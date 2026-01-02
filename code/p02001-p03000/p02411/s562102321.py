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
        print(" ", end="")
        for i, num in enumerate(l):
            print(num, end="")
            if i != len(l)-1:
                print(" ", end="")
        print()

output = output()

### input sample
#i = input()
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
    A = []

    while(True):
        m, f, r = [int(x) for x in input().split()]
        if (m == -1) and (f == -1) and (r == -1):
            break
        else:
            A.append([m,f,r])
    
    for i in A:
        seiseki = i[0]+i[1]
        if i[0]==-1 or i[1]==-1:
            print("F")
        elif seiseki >= 80:
            print("A")
        elif seiseki >= 65:
            print("B")
        elif seiseki >= 50:
            print("C")
        elif seiseki >= 30 and i[2] >= 50:
            print("C")
        elif seiseki >= 30:
            print("D")
        else:
            print("F")

if __name__ == '__main__':
    main()
