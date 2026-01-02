"""
learn M algorithms
all start at level 0
N books on algorithms
i-th book sold for C_i yen
understanding increase by A_i_j where j is the j-th algorithm

Goal: X or higher understanding for all M algorithms
MINIMIZE YEN USED
"""

def x_satisfied(cur_und, x):
    for val in cur_und:
        if val < x:
            return False
    return True

def copy_update(cur_und, matrix, item_num):
    cur_und = cur_und[::]

    for i, lvl in enumerate(matrix[item_num]):
        cur_und[i] += lvl
    
    return cur_und




def solve(n, m, x, cost, matrix):
    def rec_solve(item_num, cur_cost, cur_und):
        nonlocal cost, matrix, n, m, x

        if x_satisfied(cur_und, x):
            return cur_cost
        elif item_num == n:
            return float("inf")
        
        #print(item_num, cur_cost, cur_und)
        #print(cost[item_num])
        take = rec_solve(item_num + 1, cur_cost + cost[item_num], copy_update(cur_und, matrix, item_num))
        dont = rec_solve(item_num + 1, cur_cost, cur_und)

        return min(take, dont)

    return rec_solve(0,0, [0] * m)


N, M, X = map(int, input().split())
cost = []
matrix = []

for _ in range(N):
    row = []
    inp = map(int, input().split())
    cost.append(next(inp))
    for i in inp:
        row.append(i)
    matrix.append(row)

res = solve(N, M, X, cost, matrix)
if res == float("inf"):
    print(-1)
else:
    print(res)