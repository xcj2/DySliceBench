import itertools

def factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n

def matome(ls):
    new = []
    num = []
    for l in ls:
        if not l in new:
            new.append(l)
            num.append(1)
        else:
            num[new.index(l)] += 1
    return num

def mod_combination(n, k, mod):
    # nCk (mod m)
    def mod_permutation(n, k, mod):
        if n<=k:
            return 1
        else:
            return (n * mod_permutation(n-1,k,mod))%mod

    def mod_inv_permutation(k, mod):
        k, mod = int(k), int(mod)
        if k<=1:
            return 1
        else:
            return (pow(k,mod-2,mod) * mod_inv_permutation(k-1, mod))%mod

    return (mod_permutation(n,n-k,mod) * mod_inv_permutation(k, mod))%mod

def main():
    n,m = map(int, input().split())
    l = list(factors(m))
    y = matome(l)
    x = 1
    for i in y:
        x *= mod_combination(n+i-1,i,10**9+7)
        x = x%(10**9+7)
    print(x)
if __name__ == '__main__':
    main()