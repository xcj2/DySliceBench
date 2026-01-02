from collections import deque

ans_list = []

def solve():
    H = int(input())
    if H == 0:
        return "end"
    grid = [list(map(int,input().split())) for _ in range(H)]
    
    def erase(i):
        res = 0
        a = grid[i]
        dq = deque()
        for j in range(5):
            if not dq:
                dq.append(a[j])
            elif dq[-1] == a[j] and a[j] != 0:
                dq.append(a[j])
            else:
                if len(dq) >= 3:
                    res += dq[-1] * len(dq)
                    # 消したところを0に書き換える
                    for nj in range(j-len(dq),j):
                        grid[i][nj] = 0
                dq.clear()
                dq.append(a[j])
        if len(dq) >= 3:
            res += dq[-1] * len(dq)
            # 消したところを0に書き換える
            for nj in range(j+1-len(dq),j+1):
                grid[i][nj] = 0
        return res
    
    def drop(j):
        b = [grid[i][j] for i in range(H)]
        dq = deque()
        for i in range(H)[::-1]:
            # 下から詰めていく 左から取り出して下から詰める
            if b[i] != 0:
                dq.append(b[i])
        for ni in range(H)[::-1]:
            if dq:
                num = dq.popleft()
            else:
                num = 0
            grid[ni][j] = num

    score = 0

    while True:
        res = 0
        for i in range(H):
            res += erase(i)
        score += res
        if res == 0:
            break
        for j in range(5):
            drop(j)
    
    return score

while True:
    ans = solve()
    if ans == "end":
        break
    ans_list.append(ans)

for ans in ans_list:
    print(ans)
