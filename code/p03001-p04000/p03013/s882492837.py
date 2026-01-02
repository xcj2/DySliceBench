import sys
from itertools import product

def mat2_mul(X, Y):
    Z = [ [0, 0], 
          [0, 0] ]
    for (i,j,k) in product(range(2),range(2),range(2)):
        Z[i][j] += X[i][k] * Y[k][j]
    return Z

def mat2_pow(X, n):
    if n == 0:
        return [ [1, 0],
                 [0, 1] ]
    elif n % 2:
        return mat2_mul(X, mat2_pow(X, n-1))  
    else:
        half_pow = mat2_pow(X, n/2)
        return mat2_mul(half_pow, half_pow)

def fib(n):
    if n == 0:
        return 0
    else:
        F = [ [0, 1],
              [1, 1] ]
        return mat2_pow(F, n-1)[1][1]
    
n, m = map(int,input().split())

li = [input() for _ in range(m)]

for i in range(1,len(li)):
    if int(li[i]) - int(li[i-1]) == 1:
        print(0)
        sys.exit()

ans = ["a" for i in range(n+1)]

for i in li:
    ans[int(i)] = "#"
    
ans = "".join(ans)

ans = ans.split("#")

result = 1

for i in ans:
    result *= fib(len(i))

print(result%1000000007)