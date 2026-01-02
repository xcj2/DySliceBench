H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

# chocoのj列目の0(white)の個数を数える
def count_col_whites(choco, j):
    res = 0
    for c in choco:
        if c[j]=="1":
            res += 1
    return res

# チョコレートをヨコ方向にカットする
def cut_chocolate(i):
    if i == 0:
        return [S]
    else:
        res = []
        pre = 0
        tmp = 0
        while i > 0:
            tmp += 1
            if i%2 == 1:
                res.append(S[pre:tmp])
                pre = tmp
            i //= 2
        res.append(S[pre:len(S)])
        return res

def is_less_than_or_equal_to_K(cut):
    for c in cut:
        for j in range(W):
            tmp = 0
            for i in range(len(c)):
                if c[i][j] == "1":
                    tmp += 1
            if tmp > K:
                return False
    return True

ans = 10**10
for i in range(2**(H-1)):
    # 横方向にカットしたときのかたまりをcutに格納
    cut = cut_chocolate(i)
    tmp_ans = len(cut)-1
    # 縦方向にみていって、1列中の白チョコの個数がK個より大きければそもそも無理
    if not is_less_than_or_equal_to_K(cut):
        continue
    # 縦方向にみていって、白チョコがK個以下のかたまりになるようカットする
    current_white_nums = [0 for _ in range(len(cut))]
    for j in range(W):
        for i in range(len(cut)):
            white_num = count_col_whites(cut[i], j)
            if white_num + current_white_nums[i] <= K:
                current_white_nums[i] += white_num
            else:
                current_white_nums = [count_col_whites(cut[_], j) for _ in range(len(cut))]
                tmp_ans += 1
                break
    ans = min(ans, tmp_ans)
print(ans)


