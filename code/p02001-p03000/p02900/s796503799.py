import sys
def input():
    return sys.stdin.readline()[:-1]

#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

# 素因数分解
def prime_factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            while tmp % i == 0:
                arr.append(i)
                tmp //= i
    if(tmp != 1):
        arr.append(tmp)
    if not arr:
        arr.append(n)
    return arr 

def main():
    A, B = map(int, input().split())
    tmp = gcd(A, B)
    if tmp == 1:
        print(1)
    else:
        print(1 + len(set(prime_factorization(tmp))))

if __name__ == "__main__":
    main()