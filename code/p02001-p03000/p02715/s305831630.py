import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

MOD = 1000000007

def smax(a,b):
    if a>b:
        return a
    else:
        return b

def smin(a,b):
    if a<b:
        return a
    else:
        return b


def main():
    N,K = list(map(int,readline().split()))
    DP = [0]*(K+1)
    ans = 0
    pow_list = [pow(i,N,MOD) for i in range(1,K+1)]
    for i in range(K):
        x = K-i
        DP[x] = pow_list[int(K/x)-1]
    #print(DP)
    for s in range(K):
        i = K-s
        x = int(K/i)
        #checked = [False]*x
        val = DP[i]
        #print(ans,i)
        for j in range(1,x):
            val += MOD - DP[i*(j+1)]
            val %= MOD
            """
            if checked[j]==False:
                ans += MOD - (DP[i*(j+1)]*i)%MOD
                ans %= MOD
                #print(ans,j,checked)
                k = j+1
                while k < x+1:
                    if checked[k-1]:
                        print(k)
                        ans += DP[i*k]*i
                        ans %= MOD
                    checked[k-1] = True
                    k += j+1
            """
        ans += val*i
        ans %= MOD
        DP[i] = val
    print(ans)
        

if __name__ == '__main__':
    main()