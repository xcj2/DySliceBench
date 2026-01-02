import sys
sys.setrecursionlimit(10 ** 6)  # 再帰関数の再帰の深さを設定
to_index = lambda x: int(x) - 1  # 入力した数字に1を引いたものを返す
print_list_in_2D = lambda x: print(*x, sep="\n")  # リストの要素を改行を挟んで表示する関数

# 入力を整数に変換して受け取る
def input_int():
    return int(input())

def map_int_input():
    return map(int, input())

MII = map_int_input

def MII_split():
    return map(int, input().split())

def MII_to_index():
    return map(to_index, input())

def MII_split_to_index():
    return map(to_index, input().split())

# 入力全てを整数に変換したものの配列を受け取る
def list_int_inputs():
    return list(map(int, input()))

LII = list_int_inputs

def LII_split():
    return list(map(int, input().split()))

# 2次元リスト化
def LII_2D(rows_number):
    return [LII() for _ in range(rows_number)]

def LII_split_2D(rows_number):
    return [LII_split() for _ in range(rows_number)]

N = input_int()
a_list = LII_split()

ans = 0
# pre_idx = 0  # 前の数字のindex
current_idx = 0
continuous_cnt = 0

for i in range(1, N + 2):

    while current_idx < N:
        if a_list[current_idx] == i:
            continuous_cnt += 1
            break
        else:
            current_idx += 1
    if i == 1 and continuous_cnt == 0:
        break

print(N - continuous_cnt if continuous_cnt > 0 else -1)