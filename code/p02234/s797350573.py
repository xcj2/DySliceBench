import sys
sys.setrecursionlimit(10**7)
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

# n = int(input())
# a, b = map(int, input().split())
# int_list = list(map(int, input().split()))
# l = list(input().split())



def solve():
    n = int(input())
    mat_list = []
    for i in range(n):
        mat_list.append(list(map(int, input().split())))
    dprint(mat_list)

    # 掛け始めのidxと掛け終わりのidxをi, jとし、計算回数を持つメモ
    memo = [[0 for i in range(n)] for i in range(n)]

    def calc(start, end):
        dprint("*", start, end)
        # 1つの行列なら0
        if end == start:
            return 0

        # メモがあれば返す
        if memo[start][end] != 0:
            return memo[start][end]

        # 2つの行列なら、答えを計算しメモ追記
        if end - start == 1:
            cost = mat_list[start][0] * mat_list[start][1] * mat_list[end][1]
            memo[start][end] = cost
            dprint(start, end, cost)
            return cost

        # 3つ以上なら、再帰
        min_cost = -1
        if end - start >= 2:
            for right_start in range(start+1, end+1):
                left = calc(start, right_start-1)
                right = calc(right_start, end)
                cost = left + right + mat_list[start][0] * mat_list[right_start][0] * mat_list[end][1]
                if min_cost == -1 or min_cost > cost:
                    min_cost = cost
                dprint(start, end, right_start, min_cost, cost)

        memo[start][end] = min_cost
        return min_cost

    ans = calc(0, n-1)
    dprint(memo)
    print(int(ans))

solve()
