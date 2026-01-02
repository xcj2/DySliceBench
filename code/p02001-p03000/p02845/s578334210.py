import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    A=list(mi())
    MOD = 1000000007

    count=[0]*(N+1)
    zero = 0
    ans = 1
    for i in range(N):
        a = A[i]
        if a == 0:
            ans *= (3-zero) % MOD
            zero += 1
        else:
            b = a-1
            ans *= count[b] % MOD
            # print(count[b])
            count[b] -= 1
        
        count[a] += 1
        ans %= MOD

    ans %= MOD
    print(ans)




if __name__ == "__main__":
    main()