def factorial(a):
    r = 1
    for i in range(a):
        r *= i+1
    return r

def combinations(a, b):
    if a>=0 and b>=0 and a >= b:
        return pow(9, b) * factorial(a) // factorial(b) // factorial(a-b)
    else:
        return 0

def count(m, a, b):
    # return the count of numbers in range [0, m x 10^a] with b non zero digitals
    ## the count of numbers in range [0, m x 10^a) with b non zero digitals
    r = combinations(a-1, b) + (m-1) * combinations(a-1, b-1)
    if b == 1:
        ## m x 10^a
        r += 1
    return r

def COUNT(N,K):
    digit = list(map(int, str(N)))
    M = len(digit)
    C = count(digit[0], M, K)
    N_ = N % pow(10, M-1)
    return C, N_
    

N = int(input())
K = int(input())

C = 0
while (N>0) and (K>0):
    c, N = COUNT(N, K)
    C+= c
    K-= 1

print(C)    
