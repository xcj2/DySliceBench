import sys
import heapq
import bisect
 
mod = 10**9+7
 
def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(list(sys.stdin.readline())[:-1])
 
def main():
    N = I()
    A = LI()
    ans = 0
    count = [0]*62

    for i in range(62):
        mask = 1<<i
        for a in A:
            if a&mask:
                count[i]+=1

    for i in range(62):
        ans += (count[i] * (N-count[i]))*(1<<i)%mod
        ans %= mod


    return(ans)
 
if __name__ == "__main__":
    print(main())
