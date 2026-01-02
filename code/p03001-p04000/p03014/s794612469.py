import sys
sys.setrecursionlimit(10**7)

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)
def dmatprint(mat):

    if debug == True:
        for row in mat:
            for col in row:
                print("{0:2d} ".format(col), end="")
            print("")
        print("")

def solve():
    H, W = map(int, input().split())
    s_arr = [[-1 for w in range(W)] for h in range(H)]
    for h in range(H):
        s_row = input()
        for w in range(W):
            if s_row[w] == ".":
                s_arr[h][w] = 0
            else:
                s_arr[h][w] = 1

    # 上下左右の配列
    r_arr = [[0 for w in range(W)] for h in range(H)]
    l_arr = [[0 for w in range(W)] for h in range(H)]
    u_arr = [[0 for w in range(W)] for h in range(H)]
    d_arr = [[0 for w in range(W)] for h in range(H)]

    # 左から
    for h in range(H):
        for w in range(W):
            if s_arr[h][w] == 1:
                continue
            else:
                if w == 0:
                    val = 1
                else:
                    val = l_arr[h][w-1] + 1
            l_arr[h][w] = val

    # 上から
    for w in range(W):
        for h in range(H):
            if s_arr[h][w] == 1:
                continue
            else:
                if h == 0:
                    val = 1
                else:
                    val = u_arr[h-1][w] + 1
            u_arr[h][w] = val

    # 右から
    for h in range(H):
        for w in reversed(range(W)):
            if s_arr[h][w] == 1:
                continue
            else:
                if w == W-1:
                    val = 1
                else:
                    val = r_arr[h][w+1] + 1
            r_arr[h][w] = val

    # 下から
    for w in range(W):
        for h in reversed(range(H)):
            if s_arr[h][w] == 1:
                continue
            else:
                if h == H-1:
                    val = 1
                else:
                    val = d_arr[h + 1][w] + 1
            d_arr[h][w] = val

    mx_ans = 0
    for h in range(H):
        for w in range(W):
            ans = l_arr[h][w] + r_arr[h][w] + u_arr[h][w] + d_arr[h][w] - 3
            if ans >= mx_ans:
                mx_ans = ans

    print(mx_ans)
    dmatprint(s_arr)
solve()