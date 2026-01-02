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

    h_count = [[-1 for w in range(W)] for h in range(H)]
    w_count = [[-1 for w in range(W)] for h in range(H)]

    # w_countを埋める
    for h in range(H):
        row = s_arr[h]
        clearFlag = True
        for w, s in enumerate(row):
            if clearFlag:
                start = w
                end = w
            if s == 0:
                end = w
                clearFlag = False
            else:
                if clearFlag:
                    h_count[h][w] = -1
                else:
                    for iw in range(start, end+1):
                        w_count[h][iw] = end - start + 1
                clearFlag = True
        if clearFlag == False:
            for iw in range(start, max(end + 1, W)):
                w_count[h][iw] = end - start + 1

    # h_countを埋める
    for w in range(W):
        col = [row[w] for row in s_arr]
        clearFlag = True
        for h, s in enumerate(col):
            if clearFlag:
                start = h
                end = h
            if s == 0:
                end = h
                clearFlag = False
            else:
                if clearFlag:
                    h_count[h][w] = -1
                else:
                    for ih in range(start, end+1):
                        h_count[ih][w] = end - start + 1
                clearFlag = True
        if clearFlag == False:
            for ih in range(start, max(end+1, H)):
                h_count[ih][w] = end - start + 1

    dmatprint(h_count)
    dmatprint(w_count)
    mx_ans = 0
    for h in range(H):
        for w in range(W):
            if s_arr[h][w] == 0:
                ans = h_count[h][w] + w_count[h][w] - 1
                if ans >= mx_ans:
                    mx_ans = ans

    print(mx_ans)
    dmatprint(s_arr)
solve()