num = 10**9+7

def modpow(a, n, p):
    if n==1:
        return a%p
    if n%2 == 1:
        return (a*modpow(a, n-1, p))%p
    else:
        temp = modpow(a, n//2, p)
        return (temp*temp)%p

def combi(x, y):
    numer = 1
    denom = 1
    for i in range(y):
        numer *= x-i
        denom *= i+1
        numer %= num
        denom %= num
    return (numer*modpow(denom, num-2, num))%num

def main():
    n, a, b = map(int, input().split())
    out1 = modpow(2, n, num)
    print((out1 - combi(n, a) - combi(n, b) - 1)%num)

if __name__=='__main__':
    # import time
    # start = time.time()
    main()
    # print(f"{time.time()-start}[s]")
