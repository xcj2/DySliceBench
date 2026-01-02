import sys

def LI(): return([int(x) for x in sys.stdin.readline().split()])
def LI_(): return([int(x)-1 for x in sys.stdin.readline().split()])

def main():
    N,M = LI()
    keys = []
    for _ in range(M):
        a,b = LI()
        C = LI_()
        key_bit = 0
        for c in C:
            key_bit += (1 << c)
        keys.append([a,key_bit])

    dp = [10**10] * (1 << N)
    dp[0] = 0
    for i in range(0,M):
        for key_bit in range(1 << N):
            dp[key_bit|keys[i][1]] = min(dp[key_bit|keys[i][1]],dp[key_bit]+keys[i][0])
    if(dp[(1<<N)-1] == 10**10):
        return(-1)
    return(dp[(1<<N)-1])


if __name__ == "__main__":
    print(main())
