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

def get_input():
  N = []
  while True:
    try:
      N.append(input())
      #N.append(int(input()))
    except EOFError:
      break
  return N
 
N = get_input()

for S in N:
    i = 0
    while True:
        if i >= len(S):
            break
        if (S[i]=='@'):
            for j in range(int(S[i+1])):
                print(S[i+2], end='')
            i += 3
        else:
            print(S[i], end='')
            i += 1
        
    print()






