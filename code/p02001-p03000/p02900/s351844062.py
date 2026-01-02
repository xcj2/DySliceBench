from collections import Counter
def get_primes(targ):
    '''
    素因数分解
    '''
    primes = Counter()

    target = targ
    i = 2
    cnt = 0

    while (i * i) <= target:
        while(target % i) == 0:
            target //= i
            primes[i] += 1
        i += 1

    if target > 1:
        primes[target] += 1

    return primes;

def ABC142D_DisjointSetOf():
    A, B = list(map(int, input().strip().split()))

    prA = get_primes(A)
    prB = get_primes(B)

    ans = 0
    for i in prA.keys():
        if i in prB.keys():
            ans += 1

    print(ans + 1)



def main():
    ABC142D_DisjointSetOf()

if __name__ == "__main__":
    main()
