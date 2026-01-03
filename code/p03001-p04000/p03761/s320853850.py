###
### atcorder test program
###

import sys

### math class
class math:
    ### pi
    pi = 3.14159265358979323846264338

    ### GCD
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    ### LCM
    def lcm(self, a, b):
        return (a*b)//self.gcd(a,b)

    ### Prime number search
    def Pnum(self, a):
        if a == 1: return False
        for i in range(2,int(a**0.5)+1):
            if a % i == 0:
                return False
        return True

    ### Circle area
    def caria(self, r):
        return r*r*self.pi

math = math()

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
#inlist = [int(w) for w in input().split()]
#R = float(input())
#A = [int(x) for x in input().split()]
#for line in sys.stdin.readlines():
#    x, y = [int(temp) for temp in line.split()]

### output sample
#print("{0} {1} {2:.5f}".format(A//B, A%B, A/B))
#print("{0:.6f} {1:.6f}".format(R*R*math.pi,R*2*math.pi))
#print(" {}".format(i), end="")

#A, B, C = [int(x) for x in input().split()]

N = int(input())
S = []
AB = [chr(i) for i in range(ord('a'), ord('z')+1)]

for i in range(N):
    S.append(input())

for i in AB:
    countmin = 114514
    for j in S:
        if countmin > j.count(i):
            countmin = j.count(i)
        #print(i,countmin,j.count(i))

    for j in range(countmin):
        print(i,end="")
    
print("")
