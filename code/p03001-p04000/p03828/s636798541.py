def main():
    N = input()
    N = int(N)

    k = 1
    s = []
    #lst = list(range(1,N+1))
    primes = prime(N+1)
    num = len(primes)

    # N=1
    lst = [0] * N
    if N ==1:
        print(1)
        exit()

    # N>=2
    for i in range(2,N+1):
        b =[]
        b = bunkai(i)
        for i in b:
            lst[primes.index(i)] += 1

    ans = 1
    for i in lst:
        if i is not 0:
            ans = ans * (i+1)
    print(ans%1000000007)


def prime(n):
    primes = []
    for i in range(2,n):
        flag = True
        for j in range(2,i):
            if i%j == 0:
                flag = False
        if flag:
            primes.append(i)
    return primes

def bunkai(i):
    bunkai =[]
    s =0
    while s ==0:
        for j in range(2,i+1):
            if i % j ==0:
                bunkai.append(j)
                i = int(i/j)
                if i ==1:
                   s=1
                break
    return bunkai

if __name__ == "__main__":
        main()
