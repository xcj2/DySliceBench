import sys
import heapq
import bisect

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(sys.stdin.readline()[:-1])
def IR(n): return([I() for _ in range(n)])

def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def LCM(a,b):
    return a * b // GCD(a,b)

def Eratosthenes(N):
    r = [True]*(N+1)
    r[0] = False
    r[1] = False
    i = 2
    while i*i<=N:
        if r[i]: 
            j = i
            while i*j<=N:
                r[i*j]=False
                j+=1
        i+=1
    return(r)

def main():
    prime = Eratosthenes(10**5)
    prime_2017 = [False]*(10**5+1)
    for i in range(3,10**5+1,2):
        if prime[i]:
            prime_2017[i] = prime[(i+1)//2]

    cnt = [0]*(10**5+1)
    nxt = 0

    for i in range(1,10**5+1):
        if prime_2017[i]:
            nxt += 1
        cnt[i] = nxt

    Q = I()
    for _ in range(Q):
        l,r = LI()
        print(cnt[r] - cnt[l-1])

            


if __name__ == "__main__":
    main()
