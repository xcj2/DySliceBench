def attack(table, i, j):
    table[i][j] = 1 - table[i][j]
    table[i-1][j] = 1 - table[i-1][j]
    table[i+1][j] = 1 - table[i+1][j]
    table[i][j-1] = 1 - table[i][j-1]
    table[i][j+1] = 1 - table[i][j+1]

def printans(ans):
    for i in range(1, 11):
        for j in range(1, 11):
            print(ans[i][j], end="")
            if j < 10:
                print(" ", end="")
        print("")

def solve(table, i, j, ans):

    #print(i,j)
    if i == 11:
        flag = True
        for k in range(1,11):
            if table[10][k] == 1:
                flag = False
                break
        if flag:
            printans(ans)
        return

    if table[i-1][j] == 1:
        ans[i][j] = 1
        attack(table, i, j)
        if j == 10:
            solve(table, i+1, 1, ans)
        else:
            solve(table, i, j+1, ans)
        attack(table, i, j)
        ans[i][j] = 0
    else:
        ans[i][j] = 0
        if j == 10:
            solve(table, i+1, 1, ans)
        else:
            solve(table, i, j+1, ans)


def check(table, i, ans):

    if i == 11:
        solve(table, 2, 1, ans)
        return

    ans[1][i] = 0
    check(table, i+1, ans)

    ans[1][i] = 1
    attack(table, 1, i)
    check(table, i+1, ans)
    attack(table, 1, i)

N = int(input())

for l in range(N):
    table= [[0 for i in range(12)] for j in range(12)]
    ans= [[0 for i in range(12)] for j in range(12)]
    for i in range(1, 11):
        nums = [int(k) for k in input().split()]
        for j in range(1, 11):
            table[i][j] = nums[j-1]

    check(table, 1, ans)
