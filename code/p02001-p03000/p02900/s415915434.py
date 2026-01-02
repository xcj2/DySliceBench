import math

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
  
  # nの平方根まで計算する
    m = math.floor(math.sqrt(n)) + 1
    for p in range(3, m, 2):
        if n % p == 0:
            return False
    return True

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def main():
    A, B = [int(i) for i in input().split()]
    count = 0
    a = []
    prime = []
    if A > B:
        temp = A
        A = B
        B = temp
    a = make_divisors(A)
    
    for i in a:
        if isPrime(i) == True:
            prime.append(i)
    for i in prime:
        if B % i == 0:
            count += 1

    print(count)

if __name__ == "__main__":
    main()