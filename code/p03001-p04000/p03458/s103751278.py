import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

def cum_2d(field:list):
    row = len(field)
    col = len(field[0])
    
    # 横方向に累積和
    for r in range(row):
        for c in range(col-1):
            field[r][c+1] += field[r][c]
    
    # 縦方向に累積和
    for c in range(col):
        for r in range(row-1):
            field[r+1][c] += field[r][c]
            
    return field

n,k = li()

wishes = []
# mod K をとり、すべての希望を黒に変換
for _ in range(n):
    x,y,c = ls()
    x = int(x) % (2*k)
    y = int(y) % (2*k)
    
    if c == "B":
        if x >= k and y >= k:
            x -= k
            y -= k
        
        elif y >= k:
            x += k
            y -= k
    
    if c == "W":
        if x >= k and y >= k:
            y -= k
        
        elif x >= k:
            x -= k
            
        elif y >= k:
            y -= k
            
        else:
            x += k
        
    wishes.append((x,y))

imos = [[0 for _ in range(2*k+1)] for _ in range(2*k+1)]

for x, y in wishes:
    
    # xが K 未満のとき
    if x < k:
        # 左上
        imos[0][y+k+1] += 1
        imos[0][2*k] -= 1
        imos[x+1][y+k+1] -= 1
        imos[x+1][2*k] += 1
            
        # 左下
        imos[0][0] += 1
        imos[x+1][0] -= 1
        imos[0][y+1] -= 1
        imos[x+1][y+1] += 1
            
        # 中央
        imos[x+1][y+1] += 1
        imos[x+1][y+k+1] -= 1
        imos[x+k+1][y+1] -= 1
        imos[x+k+1][y+k+1] += 1
        
        # 右下
        imos[x+k+1][0] += 1
        imos[x+k+1][y+1] -= 1
        imos[2*k][0] -= 1
        imos[2*k][y+1] += 1
            
        # 右上
        imos[x+k+1][y+k+1] += 1
        imos[x+k+1][2*k] -= 1
        imos[2*k][y+k+1] -= 1
        imos[2*k][2*k] += 1

    # xが K 以上のとき
    else:
        #左
        imos[0][y+1] += 1
        imos[x-k+1][y+1] -= 1
        imos[0][y+k+1] -= 1
        imos[x-k+1][y+k+1] += 1
        
        # 下
        imos[x-k+1][0] += 1
        imos[x-k+1][y+1] -= 1
        imos[x+1][0] -= 1
        imos[x+1][y+1] += 1
        
        # 右
        imos[x+1][y+1] += 1
        imos[2*k][y+1] -= 1
        imos[x+1][y+k+1] -= 1
        imos[2*k][y+k+1] += 1
        
        # 上
        imos[x-k+1][y+k+1] += 1
        imos[x-k+1][2*k] -= 1
        imos[x+1][y+k+1] -= 1
        imos[x+1][2*k] += 1
    

# 累積和
imos = cum_2d(imos)

ans = 0
for i in range(2*k):
    for j in range(2*k):
        if imos[i][j] > ans:
            ans = imos[i][j]
        

print(ans)