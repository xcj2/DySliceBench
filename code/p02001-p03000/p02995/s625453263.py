import fractions

ABCD = list(map(int, input().split()))

A = ABCD[0]
B = ABCD[1]
C = ABCD[2]
D = ABCD[3]


# def lcm(x, y):
#     return (x * y) // fractions.gcd(x, y)


def floor(a, b):
  # return int((a - a%b)/b)
  return a//b
def gcd(a, b):
  while b != 0:
      a, b = b, a % b
  return a
def lcm(a, b):
  return floor((a * b), gcd(a, b))

firstC = floor((A-1),C)
firstD = floor((A-1),D)
firstCD = floor((A-1),lcm(C,D))

# if A%lcm(C,D) ==0 and firstCD > 0:
#     firstCD -= 1

endC = floor(B,C)
endD = floor(B,D)
endCD = floor(B,lcm(C,D))

End = B-endC-firstD + endCD
First = (A-1) - firstC - firstD + firstCD



thereC = endC - firstC
thereD = endD - firstD
thereCD = endCD - firstCD

NoP = thereC+thereD - thereCD

# print(thereC)
# print(thereD)
# print(thereCD)
# print(NoP)
print((B-A+1)-NoP)
# print(End-First)







