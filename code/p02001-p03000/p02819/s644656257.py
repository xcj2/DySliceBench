import math


def seachPrimeNum(N):
    max = int(math.sqrt(N))
    seachList = [i for i in range(2, N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum


def isPrime(n, prime_numbers):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    m = math.floor(math.sqrt(n))
    for p in prime_numbers:
        if n % p == 0:
            return False
        if p > m:
            # 素数がnの平方根を超えたら終了
            break
    return True


def main():
    A = int(input())
    primeNum = seachPrimeNum(A)
    while True:
        if isPrime(A, primeNum) is True:
            print(A)
            break
        A += 1


if __name__ == "__main__":
    main()
