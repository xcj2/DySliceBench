import collections
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
def myAnswer(N: int, A: list) -> int:
    odds = [a for a in A if a % 2 == 0]
    counter = 0
    for odd in odds:
        dic = collections.Counter(prime_factorize(odd))
        counter += dic[2]
    return counter




def modelAnswer():
    tmp = 1


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(myAnswer(N, A[:]))


if __name__ == '__main__':
    main()
