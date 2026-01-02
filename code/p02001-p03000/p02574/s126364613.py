import math
import functools

def gcd(num : list):
    return functools.reduce(math.gcd, num)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            while temp%i==0:
                temp //= i
            arr.append(i)

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr

def main():
    N = int(input())
    A = list(map(int, input().split()))

    checked_prime = [0] * 1000001

    for a in A:
        if a != 1:
            fac_a = factorization(a)
            for f in fac_a:
                if checked_prime[f] == 0:
                    checked_prime[f] = 1
                else:
                    if gcd(A) == 1:
                        print("setwise coprime")
                        exit()
                    else:
                        print("not coprime")
                        exit()
    print("pairwise coprime")

if __name__ == "__main__":
    main()