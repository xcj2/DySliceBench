import sys,bisect,heapq

mod = 10**9+7
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(input())
def IR(n): return([I() for _ in range(n)])

def GCD(a,b):
    while(a%b != 0):
        a,b = b,a%b
    return b

def LCM(a,b):
    return a*b//GCD(a,b)

def main():
    N = I()
    s = S()

    cSum = [0]
    for i in range(N):
        if s[i] == "#":
            cSum.append(cSum[-1]+1)
        else:
            cSum.append(cSum[-1])

    ans = N
    for i in range(N+1):
        ans_tmp = cSum[i] + (N-i-(cSum[N]-cSum[i]))
        ans = min(ans,ans_tmp)
    return(ans)

if __name__ == "__main__":
    print(main())
