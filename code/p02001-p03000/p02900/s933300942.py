
def get_primes(targ):
    '''
    素因数分解
    '''
    primes = []

    target = targ
    i = 2
    cnt = 0

    while (i * i) <= target:
        if(target % i) == 0:
            while(target % i) == 0:
                target //= i
                cnt += 1
            primes.append([i, cnt])
            cnt = 0
        else:
            i += 1

    if target != 1:
        primes.append([target, 1])

    return primes;

def ABC142D_DisjointSetOf():
    A, B = list(map(int, input().strip().split()))

    prA = get_primes(A)
    prB = get_primes(B)

    prAlist = [num[0] for num in prA]
    ans = 0
    for num in prB:
        if(num[0] in prAlist):
            ans += 1

    print(ans + 1)

def main():
    ABC142D_DisjointSetOf()

if __name__ == "__main__":
    main()
