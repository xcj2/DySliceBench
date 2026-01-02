import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K = MI()

black = [[0]*K for _ in range(K)]
white = [[0]*K for _ in range(K)]
for _ in range(N):
    x,y,c = map(str,S().split())
    x,y = int(x),int(y)
    if ((x//K + y//K) % 2 == 0 and c == 'B') or ((x//K + y//K) % 2 == 1 and c == 'W'):
        black[x % K][y % K] += 1
    else:
        white[x % K][y % K] += 1

black_accumulate = [[0]*(K+1)] + [[0]+black[i] for i in range(K)]  # black の2次元累積和
white_accumulate = [[0]*(K+1)] + [[0]+white[i] for i in range(K)]  # white の2次元累積和
for i in range(1,K+1):
    for j in range(1,K+1):
        black_accumulate[i][j] += black_accumulate[i][j-1]
        white_accumulate[i][j] += white_accumulate[i][j-1]
for i in range(1,K+1):
    for j in range(1,K+1):
        black_accumulate[i][j] += black_accumulate[i-1][j]
        white_accumulate[i][j] += white_accumulate[i-1][j]

def f(s,t,u,v):  # black の (s,t]×(u,v] の区間和
    return black_accumulate[t][v]-black_accumulate[t][u]-black_accumulate[s][v]+black_accumulate[s][u]
def g(s,t,u,v):  # white の (s,t]×(u,v] の区間和
    return white_accumulate[t][v]-white_accumulate[t][u]-white_accumulate[s][v]+white_accumulate[s][u]

ans = 0
for i in range(1,K+1):  # 区切る位置
    for j in range(1,K+1):  # 区切る位置
        ans = max(ans,f(0,i,0,j) + f(i,K,j,K) + g(0,i,j,K) + g(i,K,0,j))
        ans = max(ans,g(0,i,0,j) + g(i,K,j,K) + f(0,i,j,K) + f(i,K,0,j))
print(ans)
