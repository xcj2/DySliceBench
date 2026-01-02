INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp():
    '''
    一つの整数
    '''
    return int(input())
def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))
def inpl_str():
    '''
    一行に複数の文字
    '''
    return list(input().split())

n=inp()
a = inpl()
sorted_a = sorted(a,reverse=True)
place=dict()
for i in range(n):
    if a[i] not in place:
        place[a[i]]=[i+1]
    else:
        place[a[i]].append(i+1)
ans = 0
dp=[[-INF]*(n+1) for i in range(n+1)]
dp[0][0] = 0
for i in range(n):
    if i!=0 and sorted_a[i] == sorted_a[i - 1]:
        index += 1
    else:
        index = 0
    for j in range(n):
        _place = place[sorted_a[i]][index]
        #右
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + sorted_a[i] * abs(n - (i - j) - _place))
        #左
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + sorted_a[i] *  abs(_place - j - 1))

print(max(dp[n]))
