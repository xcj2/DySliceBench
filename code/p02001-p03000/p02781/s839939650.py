import math
def check1(N):
    if N == 0:
        return 0
    n = int(math.log10(N))
    return 9*n+(N//(10**n))
def check2(N):
    if N == 0:
        return 0
    n = int(math.log10(N))
    return n*(n-1)/2*81+(N//(10**n)-1)*n*9+check1(N%(10**n))
def check3(N):
    if N == 0:
        return 0
    n = int(math.log10(N))
    summ = 0
    if n >= 3:
        for i in range(n):
            summ += i*(i-1)/2
    return summ*729+(N//(10**n)-1)*n*(n-1)/2*81+check2(N%(10**n))
def main():
    N = int(input())
    K = int(input())
    if K == 1:
        print(int(check1(N)))
    elif K == 2:
        print(int(check2(N)))
    elif K == 3:
        print(int(check3(N)))
        
main()