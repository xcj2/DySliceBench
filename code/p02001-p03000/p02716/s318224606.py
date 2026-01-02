import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print(' '.join(map(str, l)))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

n = n_in()

A = l_in()

if n <= 3:
    print(max(A))
    exit()




if n%2 == 0:
    res = sum(A[::2])
    dp = [[0,0] for _ in range(n)]
    #dp[i][k]は k回スキップして，i番目を使う確定した時の最大

    dp[0][0] = A[0]
    dp[1][1] = A[1]
    dp[2][0] = A[0]+A[2]

    for i in range(3,n):
        dp[i][0] = dp[i-2][0] + A[i]
        dp[i][1] = max(dp[i-3][0] + A[i], dp[i-2][1] + A[i])

    print(max(res, dp[n-1][1]))
    exit()

res = sum(A[::2])-A[-1]
dp = [[0,0] for _ in range(n)]
#dp[i][k]は k回スキップして，i番目を使う確定した時の最大

dp[0][0] = A[0]
dp[1][1] = A[1]
dp[2][0] = A[0]+A[2]

for i in range(3,n-1):
    dp[i][0] = dp[i-2][0] + A[i]
    dp[i][1] = max(dp[i-3][0] + A[i], dp[i-2][1] + A[i])

#print(dp)    
res = max(res, dp[n-2][1])

dp = [[0,0,0] for _ in range(n)]
#dp[i][k]は k回スキップして，i番目を使う確定した時の最大

dp[0][0] = A[0]
dp[1][1] = A[1]
dp[2][2] = A[2]
dp[2][0] = A[0]+A[2]
dp[3][1] = max(A[0],A[1])+A[3]

for i in range(4,n):
    dp[i][0] = dp[i-2][0] + A[i]
    dp[i][1] = max(dp[i-3][0] + A[i], dp[i-2][1] + A[i])
    dp[i][2] = max(
        dp[i-4][0] + A[i],
        dp[i-3][1] + A[i],
        dp[i-2][2] + A[i]
    )

#print(dp)    
print(max(res, dp[n-1][2]))
