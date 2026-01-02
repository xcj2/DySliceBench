import sys

def gcd(a, b):
    return gcd(b, a%b) if b else a 

def lcm(a, b):
    return a // gcd(a, b) * b

def f(n):
    res = 0
    
    while not n % 2:
        n //= 2
        res += 1
        
    return res

            
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(N):
    A[i] //= 2
    
t = f(A[0])
A[0] >> t
M >> t

for i in range(1, N):
    if f(A[i]) != t:
        print(0)
        sys.exit()
        
    A[i] >> t
    
l = 1
for a in A:
    l = lcm(l, a)
    
if l > M: 
    print(0)
    sys.exit()
    
M /= l

print(int((M+1)/2))
