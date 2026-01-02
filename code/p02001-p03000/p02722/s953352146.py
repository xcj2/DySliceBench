
def make_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    divisors.append(n)
    return divisors

def check(N,K):
    try:
        if N == K:
            return True
        if N % K ==1:
            return True
        if N<K:
            return False
        
        if N % K ==0:
            return check(N//K,K)
        else:
            return False
    except:
        return False

def resolve():
    N = int(input())
    ys= set(make_divisors(N))
    ys2= set([i for i in make_divisors(N-1) if check(N,i)])

    x =set([i for i in ys if check(N,i)])

    print(len(x | ys2))


if __name__ == "__main__":
    resolve()
