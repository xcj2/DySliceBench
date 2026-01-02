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
    N = int(readline())
    A = list(map(int,readline().split()))
    if N%2==0:
        A.append(0)
        DP = [[[-10**27]*2 for j in range(2)] for i in range(N+2)]
        DP[0][0][0] = 0
        for i in range(N+1):
            DP[i+1][0][0] = DP[i][0][1]
            DP[i+1][1][0] = smax(DP[i][0][0],DP[i][1][1])
            DP[i+1][0][1] = DP[i][0][0]+A[i]
            DP[i+1][1][1] = DP[i][1][0]+A[i]
            #print(DP[i+1][1][0])
        print(DP[N+1][1][0])

    else:
        A.append(0)
        DP = [[[-10**27]*2 for j in range(3)] for i in range(N+2)]
        DP[0][0][0] = 0
        for i in range(N+1):
            DP[i+1][0][0] = DP[i][0][1]
            DP[i+1][1][0] = smax(DP[i][0][0],DP[i][1][1])
            DP[i+1][2][0] = smax(DP[i][1][0],DP[i][2][1])
            DP[i+1][0][1] = DP[i][0][0]+A[i]
            DP[i+1][1][1] = DP[i][1][0]+A[i]
            DP[i+1][2][1] = DP[i][2][0]+A[i]
            #print(DP[i+1][1][0])
        print(DP[N+1][2][0])

if __name__ == '__main__':
    main()